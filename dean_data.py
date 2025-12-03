# faq_data.py

from dataclasses import dataclass
from typing import List, Dict

# Categories as strings for simplicity
CATEGORIES = [
    "Academic", "Administrative", "Financial", "Registration",
    "Graduation", "Appeals", "Documents", "Schedule", "Policies",
]

@dataclass
class FAQEntry:
    question: str
    answer: str
    keywords: List[str]
    cat: str  # category

# Synonym map (lowercase only)
SYNONYMS: Dict[str, List[str]] = {
    "gpa": ["grade", "grades", "average", "score"],
    "graduate": ["finish", "complete", "graduation", "degree"],
    "major": ["program", "programs", "course of study", "specialization"],
    "tuition": ["fees", "payment", "cost", "money"],
    "register": ["enroll", "registration", "sign up", "enrollment"],
    "transcript": ["records", "grades", "academic record"],
    "appeal": ["challenge", "dispute", "contest"],
    "withdraw": ["drop", "leave", "quit"],
    "financial aid": ["scholarship", "bursary", "grant", "funding"],
    "probation": ["academic warning", "poor performance"],
}

# Knowledge base (port from Isabelle)
KNOWLEDGE_BASE: List[FAQEntry] = [
    FAQEntry(
        question="What is the minimum GPA required to graduate?",
        answer="The minimum cumulative GPA required for graduation is 2.0 on a 4.0 scale. Some programs may require higher GPAs.",
        keywords=["gpa", "graduate", "minimum", "requirement"],
        cat="Academic",
    ),
    FAQEntry(
        question="How do I change my major?",
        answer="To change your major, you must: 1) Meet with your academic advisor, 2) Fill out the Change of Major form available at the Dean's office, 3) Get approval from both your current and new department heads, 4) Submit the form to the Registrar's office.",
        keywords=["change", "major", "switch", "program"],
        cat="Academic",
    ),
    FAQEntry(
        question="Can I take courses from other departments?",
        answer="Yes, you can take elective courses from other departments. However, you must ensure they don't conflict with your core requirements and that you have met any prerequisites.",
        keywords=["elective", "other", "department", "courses", "cross-department"],
        cat="Academic",
    ),
    FAQEntry(
        question="What is academic probation?",
        answer="Academic probation occurs when your GPA falls below 2.0. You will have one semester to raise your GPA above 2.0, or face academic suspension.",
        keywords=["probation", "academic", "gpa", "suspension"],
        cat="Academic",
    ),
    FAQEntry(
        question="How do I apply for academic leave?",
        answer="Submit an Academic Leave of Absence form to the Dean's office at least two weeks before the semester starts. You must provide valid reasons and may need supporting documentation.",
        keywords=["leave", "absence", "defer", "postpone"],
        cat="Academic",
    ),

    # Registration
    FAQEntry(
        question="When is the registration period?",
        answer="Registration typically opens 4 weeks before the semester begins. Priority registration is given to seniors, then juniors, sophomores, and finally freshmen. Check the academic calendar for exact dates.",
        keywords=["registration", "enroll", "when", "period", "dates"],
        cat="Registration",
    ),
    FAQEntry(
        question="How do I add or drop a course?",
        answer="You can add courses during the first week of the semester through the online portal. Courses can be dropped without penalty during the first two weeks. After that, you need instructor and dean approval.",
        keywords=["add", "drop", "course", "withdraw"],
        cat="Registration",
    ),
    FAQEntry(
        question="What is the maximum course load per semester?",
        answer="Full-time students can take 12-18 credit hours per semester. If you wish to take more than 18 credits, you need special permission from the Dean's office and must have a GPA of at least 3.0.",
        keywords=["credit", "load", "maximum", "overload"],
        cat="Registration",
    ),
    FAQEntry(
        question="Can I register for a closed class?",
        answer="If a class is full, you can join the waitlist. Contact the instructor to request permission to enroll, or check daily for openings as students may drop.",
        keywords=["closed", "full", "waitlist", "class"],
        cat="Registration",
    ),
    FAQEntry(
        question="What are prerequisites and how do I waive them?",
        answer="Prerequisites are courses you must complete before enrolling in advanced courses. To waive a prerequisite, you must demonstrate equivalent knowledge and get written approval from the course instructor and department head.",
        keywords=["prerequisite", "waive", "requirement", "prior"],
        cat="Registration",
    ),

    # Financial
    FAQEntry(
        question="When are tuition fees due?",
        answer="Tuition fees are due two weeks before the start of each semester. Late payment incurs a penalty fee and may result in course deregistration.",
        keywords=["tuition", "fees", "payment", "due", "deadline"],
        cat="Financial",
    ),
    FAQEntry(
        question="How do I apply for financial aid?",
        answer="Submit the Financial Aid Application form available on the university website or at the Financial Aid office. The deadline is usually three months before the semester starts. You must provide income documentation and maintain a minimum GPA of 2.5.",
        keywords=["financial aid", "scholarship", "bursary", "apply"],
        cat="Financial",
    ),
    FAQEntry(
        question="Can I get a tuition refund if I withdraw?",
        answer="Refunds are provided on a sliding scale: 100% refund if you withdraw before classes start, 75% in the first week, 50% in the second week, and no refund after the second week.",
        keywords=["refund", "withdraw", "tuition", "money back"],
        cat="Financial",
    ),
    FAQEntry(
        question="Are payment plans available?",
        answer="Yes, you can request an installment payment plan through the Bursar's office. You must apply before the semester starts and may need to pay a processing fee.",
        keywords=["payment plan", "installment", "pay", "monthly"],
        cat="Financial",
    ),
    FAQEntry(
        question="How do I appeal a financial aid decision?",
        answer="Submit a written appeal to the Financial Aid Appeals Committee within 10 days of the decision. Include any new documentation supporting your case.",
        keywords=["appeal", "financial", "decision", "challenge"],
        cat="Financial",
    ),

    # Graduation
    FAQEntry(
        question="How do I apply for graduation?",
        answer="Submit a Graduation Application form to the Registrar's office at least one semester before your expected graduation date. There is an application fee, and you must have completed all degree requirements.",
        keywords=["graduation", "apply", "graduate", "degree"],
        cat="Graduation",
    ),
    FAQEntry(
        question="What is the deadline for graduation application?",
        answer="The graduation application deadline is October 1st for December graduation, February 1st for May graduation, and June 1st for August graduation.",
        keywords=["deadline", "graduation", "apply", "when"],
        cat="Graduation",
    ),
    FAQEntry(
        question="Can I graduate early?",
        answer="Yes, if you have completed all degree requirements including the minimum 120 credit hours and all major-specific courses. Consult with your academic advisor to ensure all requirements are met.",
        keywords=["early", "graduate", "finish", "complete"],
        cat="Graduation",
    ),
    FAQEntry(
        question="How do I obtain my diploma?",
        answer="Diplomas are mailed to your address on record 6-8 weeks after graduation. You can also pick it up in person from the Registrar's office after that period.",
        keywords=["diploma", "certificate", "degree", "obtain"],
        cat="Graduation",
    ),
    FAQEntry(
        question="What are graduation honors requirements?",
        answer="Cum Laude requires a GPA of 3.5-3.69, Magna Cum Laude requires 3.7-3.89, and Summa Cum Laude requires 3.9-4.0. You must also complete at least 60 credit hours at this institution.",
        keywords=["honors", "cum laude", "distinction", "gpa"],
        cat="Graduation",
    ),

    # Administrative + Documents + Appeals + Schedule + Policies
    FAQEntry(
        question="How do I get a transcript?",
        answer="Official transcripts can be requested through the Registrar's office or online portal. There is a processing fee per copy, and it takes 3-5 business days for processing.",
        keywords=["transcript", "records", "official", "grades"],
        cat="Documents",
    ),
    FAQEntry(
        question="How do I update my personal information?",
        answer="Log into the student portal to update your address, phone number, and email. For name changes, you must submit legal documentation to the Registrar's office.",
        keywords=["update", "information", "address", "name", "change"],
        cat="Administrative",
    ),
    FAQEntry(
        question="What is a Letter of Good Standing?",
        answer="A Letter of Good Standing confirms you are enrolled, in good academic standing, and have no disciplinary issues. Request it from the Dean's office with 3 days notice.",
        keywords=["letter", "good standing", "enrollment", "verification"],
        cat="Documents",
    ),
    FAQEntry(
        question="How do I get an enrollment verification letter?",
        answer="Enrollment verification letters can be requested through the Registrar's office or generated instantly through the online portal if you are currently enrolled.",
        keywords=["enrollment", "verification", "letter", "proof"],
        cat="Documents",
    ),
    FAQEntry(
        question="What are the Dean's office hours?",
        answer="The Dean's office is open Monday through Friday, 8:00 AM to 5:00 PM. We are closed on weekends and university holidays. Appointments are recommended for complex matters.",
        keywords=["hours", "open", "office", "time", "appointment"],
        cat="Administrative",
    ),

    FAQEntry(
        question="How do I appeal a grade?",
        answer="First, discuss the grade with your instructor within one week of receiving it. If unresolved, submit a Grade Appeal form to the Dean's office within 30 days, including documentation supporting your case.",
        keywords=["appeal", "grade", "challenge", "dispute"],
        cat="Appeals",
    ),
    FAQEntry(
        question="Can I appeal an academic dismissal?",
        answer="Yes, you can appeal academic dismissal within 10 days of notification. Submit a written appeal explaining extenuating circumstances with supporting documentation to the Academic Standards Committee.",
        keywords=["appeal", "dismissal", "suspension", "expelled"],
        cat="Appeals",
    ),
    FAQEntry(
        question="How long does the appeal process take?",
        answer="Grade appeals typically take 2-4 weeks. Academic dismissal appeals are reviewed within 15 business days. You will be notified of the decision in writing.",
        keywords=["appeal", "how long", "time", "process"],
        cat="Appeals",
    ),
    FAQEntry(
        question="Can I appeal a denied transfer credit?",
        answer="Yes, submit a Transfer Credit Appeal form with your course syllabus, transcripts, and any other relevant materials to the Dean's office for review.",
        keywords=["appeal", "transfer", "credit", "course"],
        cat="Appeals",
    ),

    FAQEntry(
        question="Where can I find the academic calendar?",
        answer="The academic calendar is available on the university website under Academics > Academic Calendar. It includes all important dates for registration, add/drop, holidays, and exams.",
        keywords=["calendar", "dates", "schedule", "semester"],
        cat="Schedule",
    ),
    FAQEntry(
        question="When are final exams?",
        answer="Final exams are held during the last week of each semester. The detailed exam schedule is published four weeks before the exam period on the Registrar's website.",
        keywords=["final", "exam", "test", "when", "schedule"],
        cat="Schedule",
    ),
    FAQEntry(
        question="Are classes held on holidays?",
        answer="No classes are held on official university holidays. Check the academic calendar for the complete list of holidays including national holidays and university-specific breaks.",
        keywords=["holiday", "break", "classes", "closed"],
        cat="Schedule",
    ),
    FAQEntry(
        question="What is reading week?",
        answer="Reading week is a one-week break before final exams with no classes scheduled. It gives students time to prepare for exams and complete final projects.",
        keywords=["reading week", "study", "break", "exams"],
        cat="Schedule",
    ),

    FAQEntry(
        question="What is the attendance policy?",
        answer="Students are expected to attend all classes. Individual instructors set specific attendance policies. Missing more than 25% of classes may result in automatic failure.",
        keywords=["attendance", "policy", "absence", "classes"],
        cat="Policies",
    ),
    FAQEntry(
        question="What is the academic honesty policy?",
        answer="Academic dishonesty including plagiarism, cheating, and unauthorized collaboration is strictly prohibited. Violations result in penalties ranging from failing grades to expulsion.",
        keywords=["honesty", "plagiarism", "cheating", "policy"],
        cat="Policies",
    ),
    FAQEntry(
        question="Can I audit a course?",
        answer="Yes, with instructor permission. Audited courses appear on your transcript but do not count toward degree requirements or GPA. You pay reduced fees and are not required to complete assignments or exams.",
        keywords=["audit", "course", "non-credit"],
        cat="Policies",
    ),
    FAQEntry(
        question="What is the grade grievance procedure?",
        answer="Students have the right to understand grading criteria and challenge grades they believe are unfair. Follow the appeals process outlined in the student handbook.",
        keywords=["grade", "grievance", "policy", "challenge"],
        cat="Policies",
    ),
]

TOTAL_FAQS = len(KNOWLEDGE_BASE)