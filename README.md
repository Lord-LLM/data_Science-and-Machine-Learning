# Student Scoresheet Application

## 📋 Project Overview
The **Student Scoresheet Application** is a comprehensive Java program designed to manage and display student academic performance data. This application collects information about students, their marks across multiple subjects, and generates a professionally formatted scoresheet report with statistical analysis.

## 🎯 Purpose
This project demonstrates mastery of fundamental Java programming concepts including:
- User input handling with Scanner
- Arrays and multi-dimensional arrays
- Loops (for loops and nested loops)
- Control statements (if-else and switch)
- String formatting and output alignment
- Data processing and statistical calculations

## ✨ Features

### 1. **School Information Collection**
- School name
- Teacher name
- Grade level
- Academic year

### 2. **Student Data Management**
- Supports multiple students (minimum 12 recommended)
- Records marks for 6 subjects per student:
  - English
  - Math
  - History
  - Geography
  - Science
  - Programming

### 3. **Automated Calculations**
- **Total Marks**: Sum of all subject marks for each student
- **Letter Grades**: Automatic grade assignment based on total marks
- **Subject Totals**: Sum of all student marks per subject
- **Subject Averages**: Average performance per subject
- **Grand Total**: Total of all marks across all students
- **Overall Average**: Class average across all subjects
- **Grade Distribution**: Count of A's, B's, C's, D's, and F's

### 4. **Professional Report Generation**
- Formatted scoresheet with proper alignment
- Clear headers and separators
- Easy-to-read tabular format
- Statistical summary at the bottom

## 📊 Grading System

The application uses the following grading scale:

| Total Marks | Letter Grade |
|-------------|--------------|
| ≥ 540.0     | A            |
| ≥ 480.0     | B            |
| ≥ 420.0     | C            |
| ≥ 360.0     | D            |
| < 360.0     | F            |

**Note**: Maximum possible score is 600 points (100 points × 6 subjects)

## 🚀 How to Run

### Prerequisites
- Java Development Kit (JDK) 8 or higher
- Command line terminal or Java IDE (Eclipse, IntelliJ IDEA, VS Code, etc.)

### Compilation
```bash
javac StudentScoresheet.java
```

### Execution
```bash
java StudentScoresheet
```

## 📝 Usage Instructions

1. **Launch the program**
2. **Enter school details** when prompted:
   - School name
   - Teacher name
   - Grade level (numeric)
   - Year (numeric)
3. **Enter number of students** you want to record
4. **Input student names** one by one
5. **Enter marks** for each student across all 6 subjects (0-100 per subject)
6. **View the generated report** with all calculations and statistics

### Sample Input Flow
```
Enter school's name:
Ronald Reagan High School

Enter teacher's name:
Mr. Paul Swatz

Enter the grade:
10

Enter the year:
2018

Key in the number of students:
3

Enter student name 1:
Alice Arnold

Enter student name 2:
Cory Brown

Enter student name 3:
Sean Douglas

Enter marks for Alice Arnold:
English:
76.00
Math:
65.00
...
```

## 🔧 Technical Implementation

### Data Structures Used
- **1D String Array**: Store student names
- **2D Double Array**: Store marks (rows = students, columns = subjects)
- **1D Double Arrays**: Store totals, subject totals, and subject averages
- **1D String Array**: Store letter grades

### Key Algorithms
- **Grade Assignment**: Conditional statements to assign letter grades based on total marks
- **Statistical Calculations**: Nested loops to compute totals and averages
- **Grade Counting**: Switch statement to count grade distribution

### Programming Concepts Demonstrated
- ✅ Scanner for user input
- ✅ Arrays and multi-dimensional arrays
- ✅ For loops and nested loops
- ✅ If-else statements
- ✅ Switch statements
- ✅ String formatting with printf
- ✅ Mathematical calculations
- ✅ Data validation and processing

## 📸 Sample Output

The program generates a formatted report similar to this:

```
==========================================================================================================================================================
                              School Name: Ronald Reagan High School
                              Teacher: Mr. Paul Swatz
                              Grade: 10
                              Year: 2018
==========================================================================================================================================================
Student Name         English        Math     History   Geography     Science Programming       Total    Rank
==========================================================================================================================================================
Alice Arnold           76.00       65.00       91.00       89.00       98.00      100.00      519.00       B
Cory Brown             67.00       88.00       87.80       67.90       60.90       69.90      441.50       C
Sean Douglas           90.00       99.00       91.00       87.00       88.90       80.90      536.80       B
----------------------------------------------------------------------------------------------------------------------------------------------------------
                     1154.20     1205.50     1213.10     1244.90     1207.10      1180.70     7205.50
----------------------------------------------------------------------------------------------------------------------------------------------------------
                       76.95       80.37       80.87       82.99       80.47        78.71      480.37
==========================================================================================================================================================
