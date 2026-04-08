theory FAQ
  imports Main
begin

(* =========================================
   Production FAQ system for Dean's office
   - full FAQ database (from user)
   - tokenization (split on non-alphanumerics)
   - ASCII lowercase conversion (A..Z -> a..z)
   - synonyms mapping
   - scoring & best-match retrieval
   ========================================= *)

(* -------------------------
   Types & record
   ------------------------- *)

datatype category = 
  Academic | Administrative | Financial | Registration |
  Graduation | Appeals | Documents | Schedule | Policies

record faq_entry =
  question :: string
  answer :: string
  keywords :: "string list"
  cat :: category

(* -------------------------
   Helper: ASCII lowercase for chars
   (maps 'A'..'Z' to 'a'..'z'; leaves others unchanged)
   ------------------------- *)

fun ascii_lower_char :: "char \<Rightarrow> char" where
  "ascii_lower_char c =
     (if c \<ge> CHR ''A'' \<and> c \<le> CHR ''Z'' 
      then CHR (nat (c) + (nat (CHR ''a'') - nat (CHR ''A'')))
      else c)"

(* Safe, small function to lowercase ASCII letters.
   NOTE: CHR literal usage and nat conversions above are portable
   in Isabelle/HOL; this function only targets ASCII A..Z. *)

(* Lowercase a string (ASCII only) by mapping ascii_lower_char over its exploded char list. *)
definition to_lowercase :: "string \<Rightarrow> string" where
"to_lowercase s = String.implode (map ascii_lower_char (String.explode s))"

(* -------------------------
   Tokenization: split a string into words
   We split on any character that's not alphanumeric (letters/digits).
   Produces list of tokens (strings). Empty tokens ignored.
   ------------------------- *)

fun is_alnum_char :: "char \<Rightarrow> bool" where
  "is_alnum_char c = (let n = nat c in
                      ( (c \<ge> CHR ''0'' \<and> c \<le> CHR ''9'') \<longrightarrow> True
                    | (c \<ge> CHR ''a'' \<and> c \<le> CHR ''z'') \<longrightarrow> True
                    | (c \<ge> CHR ''A'' \<and> c \<le> CHR ''Z'') \<longrightarrow> True
                    | True \<longrightarrow> False))"

(* Because Isabelle/HOL function definitions must be total, but the above boolean expression style
   isn't directly accepted. We'll implement is_alnum_char with explicit cases: *)

fun is_alnum_char' :: "char \<Rightarrow> bool" where
  "is_alnum_char' c = (if c \<ge> CHR ''0'' \<and> c \<le> CHR ''9'' then True
                       else if c \<ge> CHR ''a'' \<and> c \<le> CHR ''z'' then True
                       else if c \<ge> CHR ''A'' \<and> c \<le> CHR ''Z'' then True
                       else False)"

fun split_on_non_alnum_aux :: "char list \<Rightarrow> char list \<Rightarrow> string list \<Rightarrow> string list" where
  "split_on_non_alnum_aux [] curr acc =
     (if curr = [] then rev acc else rev (String.implode (rev curr) # acc))" |
  "split_on_non_alnum_aux (c#cs) curr acc =
     (if is_alnum_char' c
      then split_on_non_alnum_aux cs (c#curr) acc
      else (* c is separator *)
         (if curr = [] then split_on_non_alnum_aux cs [] acc
          else split_on_non_alnum_aux cs [] (String.implode (rev curr) # acc)))"

definition tokenize :: "string \<Rightarrow> string list" where
"tokenize s = map to_lowercase (split_on_non_alnum_aux (String.explode s) [] [])"

(* tokenize: explode into chars, group runs of alnum chars into tokens, lowercases each token. *)

(* -------------------------
   Synonym map (keyword -> list of synonyms)
   Represented as list of (string * string list)
   ------------------------- *)

definition synonym_map :: "(string * string list) list" where
"synonym_map = [
  (''gpa'', [''grade'', ''grades'', ''average'', ''score'']),
  (''graduate'', [''finish'', ''complete'', ''graduation'', ''degree'']),
  (''major'', [''program'', ''programs'', ''course of study'', ''specialization'']),
  (''tuition'', [''fees'', ''payment'', ''cost'', ''money'']),
  (''register'', [''enroll'', ''registration'', ''sign up'', ''enrollment'']),
  (''transcript'', [''records'', ''grades'', ''academic record'']),
  (''appeal'', [''challenge'', ''dispute'', ''contest'']),
  (''withdraw'', [''drop'', ''leave'', ''quit'']),
  (''financial aid'', [''scholarship'', ''bursary'', ''grant'', ''funding'']),
  (''probation'', [''academic warning'', ''poor performance''])
]"

(* Helper: lookup synonyms for a (lowercased) keyword *)
fun get_synonyms :: "string \<Rightarrow> string list" where
"get_synonyms k = (case List.find (\<lambda> (x, _). x = k) synonym_map of
                     Some (_, s) \<Rightarrow> s
                   | None \<Rightarrow> [])"

(* -------------------------
   Matching primitives
   - check if any token equals keyword or any synonym
   - also accept substring matches (token contains keyword or keyword contains token)
   ------------------------- *)

fun token_eq_ci :: "string \<Rightarrow> string \<Rightarrow> bool" where
"token_eq_ci t k = (t = k)"

fun token_matches_keyword :: "astring \<Rightarrow> string \<Rightarrow> bool" where
"token_matches_keyword tok kw =
   (let syns = get_synonyms kw
    in (tok = kw) \<or> (List.exists (\<lambda>s. tok = s) syns) \<or>
       (String.isSubstring kw tok) \<or> (String.isSubstring tok kw))"

(* Compute score for a faq entry given tokenized query
   - each exact keyword hit: 3 points
   - each synonym hit: 2 points
   - token substring match: 1 point
   - question similarity: number of common tokens (1 each)
*)

fun keyword_hit_score :: "string \<Rightarrow> string \<Rightarrow> nat" where
"keyword_hit_score tok kw =
   (if tok = kw then 3
    else if List.exists (\<lambda>s. tok = s) (get_synonyms kw) then 2
    else if String.isSubstring kw tok \<or> String.isSubstring tok kw then 1
    else 0)"

fun score_entry :: "faq_entry \<Rightarrow> string list \<Rightarrow> nat" where
"score_entry f toks =
   (let ks = map to_lowercase (keywords f); (* keywords in FAQ; ensure lowercase *)
        keyword_scores = fold (\<lambda>kw acc. acc + (fold (\<lambda>tok acc2. acc2 + keyword_hit_score tok kw) toks 0)) ks 0;
        q_tokens = tokenize (question f);
        common = fold (\<lambda>t acc. if List.exists (\<lambda>u. u = t) toks then acc + 1 else acc) q_tokens 0
    in keyword_scores * 1 + common)"

(* find_best: iterate and pick highest scoring entry (ties -> first encountered) *)
fun find_best :: "faq_entry list \<Rightarrow> string list \<Rightarrow> nat \<Rightarrow> faq_entry option \<Rightarrow> faq_entry option" where
"find_best [] _ _ best = best" |
"find_best (f#fs) toks best_score best =
   (let sc = score_entry f toks in
    if sc > best_score then find_best fs toks sc (Some f)
    else find_best fs toks best_score best)"

(* -------------------------
   Knowledge base: cleaned versions of the user's FAQ entries
   (I kept content but normalized keywords to lowercase)
   ------------------------- *)

definition academic_faqs :: "faq_entry list" where
"academic_faqs = [
  (| question = ''What is the minimum GPA required to graduate?'',
     answer = ''The minimum cumulative GPA required for graduation is 2.0 on a 4.0 scale. Some programs may require higher GPAs.'',
     keywords = [''gpa'', ''graduate'', ''minimum'', ''requirement''],
     cat = Academic |),

  (| question = ''How do I change my major?'',
     answer = ''To change your major, you must: 1) Meet with your academic advisor, 2) Fill out the Change of Major form available at the Dean''s office, 3) Get approval from both your current and new department heads, 4) Submit the form to the Registrar''s office.'',
     keywords = [''change'', ''major'', ''switch'', ''program''],
     cat = Academic |),

  (| question = ''Can I take courses from other departments?'',
     answer = ''Yes, you can take elective courses from other departments. However, you must ensure they don''t conflict with your core requirements and that you have met any prerequisites.'',
     keywords = [''elective'', ''other'', ''department'', ''courses'', ''cross-department''],
     cat = Academic |),

  (| question = ''What is academic probation?'',
     answer = ''Academic probation occurs when your GPA falls below 2.0. You will have one semester to raise your GPA above 2.0, or face academic suspension.'',
     keywords = [''probation'', ''academic'', ''gpa'', ''suspension''],
     cat = Academic |),

  (| question = ''How do I apply for academic leave?'',
     answer = ''Submit an Academic Leave of Absence form to the Dean''s office at least two weeks before the semester starts. You must provide valid reasons and may need supporting documentation.'',
     keywords = [''leave'', ''absence'', ''defer'', ''postpone''],
     cat = Academic |)
]"

definition registration_faqs :: "faq_entry list" where
"registration_faqs = [
  (| question = ''When is the registration period?'',
     answer = ''Registration typically opens 4 weeks before the semester begins. Priority registration is given to seniors, then juniors, sophomores, and finally freshmen. Check the academic calendar for exact dates.'',
     keywords = [''registration'', ''enroll'', ''when'', ''period'', ''dates''],
     cat = Registration |),

  (| question = ''How do I add or drop a course?'',
     answer = ''You can add courses during the first week of the semester through the online portal. Courses can be dropped without penalty during the first two weeks. After that, you need instructor and dean approval.'',
     keywords = [''add'', ''drop'', ''course'', ''withdraw''],
     cat = Registration |),

  (| question = ''What is the maximum course load per semester?'',
     answer = ''Full-time students can take 12-18 credit hours per semester. If you wish to take more than 18 credits, you need special permission from the Dean''s office and must have a GPA of at least 3.0.'',
     keywords = [''credit'', ''load'', ''maximum'', ''overload''],
     cat = Registration |),

  (| question = ''Can I register for a closed class?'',
     answer = ''If a class is full, you can join the waitlist. Contact the instructor to request permission to enroll, or check daily for openings as students may drop.'',
     keywords = [''closed'', ''full'', ''waitlist'', ''class''],
     cat = Registration |),

  (| question = ''What are prerequisites and how do I waive them?'',
     answer = ''Prerequisites are courses you must complete before enrolling in advanced courses. To waive a prerequisite, you must demonstrate equivalent knowledge and get written approval from the course instructor and department head.'',
     keywords = [''prerequisite'', ''waive'', ''requirement'', ''prior''],
     cat = Registration |)
]"

definition financial_faqs :: "faq_entry list" where
"financial_faqs = [
  (| question = ''When are tuition fees due?'',
     answer = ''Tuition fees are due two weeks before the start of each semester. Late payment incurs a penalty fee and may result in course deregistration.'',
     keywords = [''tuition'', ''fees'', ''payment'', ''due'', ''deadline''],
     cat = Financial |),

  (| question = ''How do I apply for financial aid?'',
     answer = ''Submit the Financial Aid Application form available on the university website or at the Financial Aid office. The deadline is usually three months before the semester starts. You must provide income documentation and maintain a minimum GPA of 2.5.'',
     keywords = [''financial aid'', ''scholarship'', ''bursary'', ''apply''],
     cat = Financial |),

  (| question = ''Can I get a tuition refund if I withdraw?'',
     answer = ''Refunds are provided on a sliding scale: 100% refund if you withdraw before classes start, 75% in the first week, 50% in the second week, and no refund after the second week.'',
     keywords = [''refund'', ''withdraw'', ''tuition'', ''money back''],
     cat = Financial |),

  (| question = ''Are payment plans available?'',
     answer = ''Yes, you can request an installment payment plan through the Bursar''s office. You must apply before the semester starts and may need to pay a processing fee.'',
     keywords = [''payment plan'', ''installment'', ''pay'', ''monthly''],
     cat = Financial |),

  (| question = ''How do I appeal a financial aid decision?'',
     answer = ''Submit a written appeal to the Financial Aid Appeals Committee within 10 days of the decision. Include any new documentation supporting your case.'',
     keywords = [''appeal'', ''financial'', ''decision'', ''challenge''],
     cat = Financial |)
]"

definition graduation_faqs :: "faq_entry list" where
"graduation_faqs = [
  (| question = ''How do I apply for graduation?'',
     answer = ''Submit a Graduation Application form to the Registrar''s office at least one semester before your expected graduation date. There is an application fee, and you must have completed all degree requirements.'',
     keywords = [''graduation'', ''apply'', ''graduate'', ''degree''],
     cat = Graduation |),

  (| question = ''What is the deadline for graduation application?'',
     answer = ''The graduation application deadline is October 1st for December graduation, February 1st for May graduation, and June 1st for August graduation.'',
     keywords = [''deadline'', ''graduation'', ''apply'', ''when''],
     cat = Graduation |),

  (| question = ''Can I graduate early?'',
     answer = ''Yes, if you have completed all degree requirements including the minimum 120 credit hours and all major-specific courses. Consult with your academic advisor to ensure all requirements are met.'',
     keywords = [''early'', ''graduate'', ''finish'', ''complete''],
     cat = Graduation |),

  (| question = ''How do I obtain my diploma?'',
     answer = ''Diplomas are mailed to your address on record 6-8 weeks after graduation. You can also pick it up in person from the Registrar''s office after that period.'',
     keywords = [''diploma'', ''certificate'', ''degree'', ''obtain''],
     cat = Graduation |),

  (| question = ''What are graduation honors requirements?'',
     answer = ''Cum Laude requires a GPA of 3.5-3.69, Magna Cum Laude requires 3.7-3.89, and Summa Cum Laude requires 3.9-4.0. You must also complete at least 60 credit hours at this institution.'',
     keywords = [''honors'', ''cum laude'', ''distinction'', ''gpa''],
     cat = Graduation |)
]"

definition administrative_faqs :: "faq_entry list" where
"administrative_faqs = [
  (| question = ''How do I get a transcript?'',
     answer = ''Official transcripts can be requested through the Registrar''s office or online portal. There is a processing fee per copy, and it takes 3-5 business days for processing.'',
     keywords = [''transcript'', ''records'', ''official'', ''grades''],
     cat = Documents |),

  (| question = ''How do I update my personal information?'',
     answer = ''Log into the student portal to update your address, phone number, and email. For name changes, you must submit legal documentation to the Registrar''s office.'',
     keywords = [''update'', ''information'', ''address'', ''name'', ''change''],
     cat = Administrative |),

  (| question = ''What is a Letter of Good Standing?'',
     answer = ''A Letter of Good Standing confirms you are enrolled, in good academic standing, and have no disciplinary issues. Request it from the Dean''s office with 3 days notice.'',
     keywords = [''letter'', ''good standing'', ''enrollment'', ''verification''],
     cat = Documents |),

  (| question = ''How do I get an enrollment verification letter?'',
     answer = ''Enrollment verification letters can be requested through the Registrar''s office or generated instantly through the online portal if you are currently enrolled.'',
     keywords = [''enrollment'', ''verification'', ''letter'', ''proof''],
     cat = Documents |),

  (| question = ''What are the Dean''s office hours?'',
     answer = ''The Dean''s office is open Monday through Friday, 8:00 AM to 5:00 PM. We are closed on weekends and university holidays. Appointments are recommended for complex matters.'',
     keywords = [''hours'', ''open'', ''office'', ''time'', ''appointment''],
     cat = Administrative |)
]"

definition appeals_faqs :: "faq_entry list" where
"appeals_faqs = [
  (| question = ''How do I appeal a grade?'',
     answer = ''First, discuss the grade with your instructor within one week of receiving it. If unresolved, submit a Grade Appeal form to the Dean''s office within 30 days, including documentation supporting your case.'',
     keywords = [''appeal'', ''grade'', ''challenge'', ''dispute''],
     cat = Appeals |),

  (| question = ''Can I appeal an academic dismissal?'',
     answer = ''Yes, you can appeal academic dismissal within 10 days of notification. Submit a written appeal explaining extenuating circumstances with supporting documentation to the Academic Standards Committee.'',
     keywords = [''appeal'', ''dismissal'', ''suspension'', ''expelled''],
     cat = Appeals |),

  (| question = ''How long does the appeal process take?'',
     answer = ''Grade appeals typically take 2-4 weeks. Academic dismissal appeals are reviewed within 15 business days. You will be notified of the decision in writing.'',
     keywords = [''appeal'', ''how long'', ''time'', ''process''],
     cat = Appeals |),

  (| question = ''Can I appeal a denied transfer credit?'',
     answer = ''Yes, submit a Transfer Credit Appeal form with your course syllabus, transcripts, and any other relevant materials to the Dean''s office for review.'',
     keywords = [''appeal'', ''transfer'', ''credit'', ''course''],
     cat = Appeals |)
]"

definition schedule_faqs :: "faq_entry list" where
"schedule_faqs = [
  (| question = ''Where can I find the academic calendar?'',
     answer = ''The academic calendar is available on the university website under Academics > Academic Calendar. It includes all important dates for registration, add/drop, holidays, and exams.'',
     keywords = [''calendar'', ''dates'', ''schedule'', ''semester''],
     cat = Schedule |),

  (| question = ''When are final exams?'',
     answer = ''Final exams are held during the last week of each semester. The detailed exam schedule is published four weeks before the exam period on the Registrar''s website.'',
     keywords = [''final'', ''exam'', ''test'', ''when'', ''schedule''],
     cat = Schedule |),

  (| question = ''Are classes held on holidays?'',
     answer = ''No classes are held on official university holidays. Check the academic calendar for the complete list of holidays including national holidays and university-specific breaks.'',
     keywords = [''holiday'', ''break'', ''classes'', ''closed''],
     cat = Schedule |),

  (| question = ''What is reading week?'',
     answer = ''Reading week is a one-week break before final exams with no classes scheduled. It gives students time to prepare for exams and complete final projects.'',
     keywords = [''reading week'', ''study'', ''break'', ''exams''],
     cat = Schedule |)
]"

definition policy_faqs :: "faq_entry list" where
"policy_faqs = [
  (| question = ''What is the attendance policy?'',
     answer = ''Students are expected to attend all classes. Individual instructors set specific attendance policies. Missing more than 25% of classes may result in automatic failure.'',
     keywords = [''attendance'', ''policy'', ''absence'', ''classes''],
     cat = Policies |),

  (| question = ''What is the academic honesty policy?'',
     answer = ''Academic dishonesty including plagiarism, cheating, and unauthorized collaboration is strictly prohibited. Violations result in penalties ranging from failing grades to expulsion.'',
     keywords = [''honesty'', ''plagiarism'', ''cheating'', ''policy''],
     cat = Policies |),

  (| question = ''Can I audit a course?'',
     answer = ''Yes, with instructor permission. Audited courses appear on your transcript but do not count toward degree requirements or GPA. You pay reduced fees and are not required to complete assignments or exams.'',
     keywords = [''audit'', ''course'', ''non-credit''],
     cat = Policies |),

  (| question = ''What is the grade grievance procedure?'',
     answer = ''Students have the right to understand grading criteria and challenge grades they believe are unfair. Follow the appeals process outlined in the student handbook.'',
     keywords = [''grade'', ''grievance'', ''policy'', ''challenge''],
     cat = Policies |)
]"

definition administrative_all :: "faq_entry list" where
"administrative_all = administrative_faqs @ appeals_faqs"

definition knowledge_base :: "faq_entry list" where
"knowledge_base = 
  academic_faqs @ 
  registration_faqs @ 
  financial_faqs @ 
  graduation_faqs @ 
  administrative_all @
  schedule_faqs @
  policy_faqs"

(* -------------------------
   Public query function
   - preprocess query: lowercase + tokenize
   - find best FAQ entry by score
   ------------------------- *)

definition query_kb :: "string \<Rightarrow> faq_entry option" where
"query_kb q = find_best knowledge_base (tokenize q) 0 None"

fun get_answer :: "faq_entry option \<Rightarrow> string" where
"get_answer None = ''I''m sorry — I could not find a matching answer. Please rephrase your question or contact the Dean''s office.''" |
"get_answer (Some f) = answer f"

definition process_query :: "string \<Rightarrow> string" where
"process_query q = get_answer (query_kb q)"

(* -------------------------
   Utilities: list all questions and count
   ------------------------- *)

fun get_all_questions :: "faq_entry list \<Rightarrow> string list" where
"get_all_questions [] = []" |
"get_all_questions (f#fs) = question f # get_all_questions fs"

definition total_faqs :: nat where
"total_faqs = length knowledge_base"

(* -------------------------
   Example: values you can evaluate in Isabelle/jEdit
   ------------------------- *)

value "process_query ''GPA requirement''"
value "process_query ''minimum grade average needed for graduation''"
value "process_query ''how do i change my major''"
value "process_query ''when do i pay fees''"
value "process_query ''how to get transcript''"
value "process_query ''appeal grade''"
value "value total_faqs"

(* -------------------------
   Properties (light verification)
   - Every FAQ has at least one keyword
   - KB non-empty
   ------------------------- *)

lemma faq_has_keywords:
  "f \<in> set knowledge_base \<Longrightarrow> keywords f \<noteq> []"
  by (simp add: knowledge_base_def academic_faqs_def registration_faqs_def 
                financial_faqs_def graduation_faqs_def administrative_all_def
                appeals_faqs_def schedule_faqs_def policy_faqs_def)

lemma kb_non_empty:
  "knowledge_base \<noteq> []"
  by (simp add: knowledge_base_def academic_faqs_def)

end