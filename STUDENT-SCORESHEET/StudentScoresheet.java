import java.util.Scanner;

public class StudentScoresheet {
    public static void main(String[] args) {
        // SCANNER
        Scanner scanner = new Scanner(System.in);

        // INPUT SCHOOL DETAILS
        System.out.println("Enter school's name:");
        String schoolName = scanner.nextLine();

        System.out.println("Enter teacher's name:");
        String teacherName = scanner.nextLine();

        System.out.println("Enter the grade:");
        int grade = scanner.nextInt();

        System.out.println("Enter the year:");
        int year = scanner.nextInt();
        scanner.nextLine();

        System.out.println("Key in the number of students:");
        int studentsNo = scanner.nextInt();
        scanner.nextLine();

        // FIXED SUBJECT NAMES - ARRAY
        String[] subjects = {"English", "Math", "History", "Geography", "Science", "Programming"};
        int subjectsNo = subjects.length;

        // ARRAYS FOR STUDENT DATA
        String[] students = new String[studentsNo];
        double[][] marks = new double[studentsNo][subjectsNo];

        // INPUT STUDENT NAMES - LOOP
        for (int i = 0; i < studentsNo; i++) {
            System.out.println("Enter student name " + (i + 1) + ":");
            students[i] = scanner.nextLine();
        }

        // INPUT MARKS FOR EACH STUDENT - NESTED LOOP
        for (int i = 0; i < studentsNo; i++) {
            System.out.println("\nEnter marks for " + students[i] + ":");
            for (int j = 0; j < subjectsNo; j++) {
                System.out.println(subjects[j] + ":");
                marks[i][j] = scanner.nextDouble();
            }
            scanner.nextLine();
        }

        // CALCULATE TOTALS AND GRADES - ARRAYS
        double[] totals = new double[studentsNo];
        String[] grades = new String[studentsNo];

        // LOOP TO CALCULATE TOTAL MARKS FOR EACH STUDENT
        for (int i = 0; i < studentsNo; i++) {
            double sum = 0;
            for (int j = 0; j < subjectsNo; j++) {
                sum += marks[i][j];
            }
            totals[i] = sum;

            // ASSIGN LETTER GRADES - CONTROL STATEMENTS
            if (sum >= 540) {
                grades[i] = "A";
            } else if (sum >= 480) {
                grades[i] = "B";
            } else if (sum >= 420) {
                grades[i] = "C";
            } else if (sum >= 360) {
                grades[i] = "D";
            } else {
                grades[i] = "F";
            }
        }

        // CALCULATE SUBJECT STATISTICS - ARRAYS
        double[] subjectTotals = new double[subjectsNo];
        double[] subjectAverages = new double[subjectsNo];

        // LOOP TO CALCULATE TOTALS AND AVERAGES PER SUBJECT
        for (int j = 0; j < subjectsNo; j++) {
            double sum = 0;
            for (int i = 0; i < studentsNo; i++) {
                sum += marks[i][j];
            }
            subjectTotals[j] = sum;
            subjectAverages[j] = sum / studentsNo;
        }

        // COUNT LETTER GRADES - SWITCH STATEMENT
        int countA = 0, countB = 0, countC = 0, countD = 0, countF = 0;
        for (int i = 0; i < studentsNo; i++) {
            switch (grades[i]) {
                case "A":
                    countA++;
                    break;
                case "B":
                    countB++;
                    break;
                case "C":
                    countC++;
                    break;
                case "D":
                    countD++;
                    break;
                case "F":
                    countF++;
                    break;
            }
        }

        // CALCULATE GRAND TOTAL
        double grandTotal = 0;
        for (int i = 0; i < studentsNo; i++) {
            grandTotal += totals[i];
        }

        // OUTPUT SECTION - FORMATTED REPORT
        System.out.println("\n==========================================================================================================================================================");
        System.out.printf("%30sSchool Name: %s\n", "", schoolName);
        System.out.printf("%30sTeacher: %s\n", "", teacherName);
        System.out.printf("%30sGrade: %d\n", "", grade);
        System.out.printf("%30sYear: %d\n", "", year);
        System.out.println("==========================================================================================================================================================");

        // HEADER ROW
        System.out.printf("%-20s", "Student Name");
        for (String subject : subjects) {
            System.out.printf("%12s", subject);
        }
        System.out.printf("%12s%8s\n", "Total", "Rank");
        System.out.println("==========================================================================================================================================================");

        // STUDENT DATA ROWS - LOOP
        for (int i = 0; i < studentsNo; i++) {
            System.out.printf("%-20s", students[i]);
            for (int j = 0; j < subjectsNo; j++) {
                System.out.printf("%12.2f", marks[i][j]);
            }
            System.out.printf("%12.2f%8s\n", totals[i], grades[i]);
        }
        System.out.println("----------------------------------------------------------------------------------------------------------------------------------------------------------");

        // SUBJECT TOTALS ROW
        System.out.printf("%-20s", "");
        for (int j = 0; j < subjectsNo; j++) {
            System.out.printf("%12.2f", subjectTotals[j]);
        }
        System.out.printf("%12.2f\n", grandTotal);
        System.out.println("----------------------------------------------------------------------------------------------------------------------------------------------------------");

        // SUBJECT AVERAGES ROW
        System.out.printf("%-20s", "");
        for (int j = 0; j < subjectsNo; j++) {
            System.out.printf("%12.2f", subjectAverages[j]);
        }
        System.out.printf("%12.2f\n", grandTotal / studentsNo);
        System.out.println("==========================================================================================================================================================");

        // GRADE DISTRIBUTION
        System.out.printf("%50s A's: %d   B's: %d   C's: %d   D's: %d   F's: %d\n",
                "Ranks", countA, countB, countC, countD, countF);
        System.out.println("==========================================================================================================================================================");

        // CLOSE SCANNER
        scanner.close();
    }
}