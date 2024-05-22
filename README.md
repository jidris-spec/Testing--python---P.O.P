Grade Tracker
This Python application is a simple Grade Tracker system. It allows users to add courses along with their corresponding scores, display their grades for each course, and calculate the total score of all courses through a console-based interface.

Features
Add Courses: Users can add courses and their corresponding scores.
Display Grades: Users can display their grades for each course.
Calculate Total Grade: Users can calculate the total score of all courses.
Exit: Users can exit the program.
Usage
Clone the repository to your local machine.
Navigate to the directory where the code is located.
Run the code using Python.
bash
Copy code
git clone <repository-url>
cd <repository-directory>
python grade_tracker.py
Code Overview
The GradeTracker class manages the functionality of the grade tracking system.
__init__: Initializes the grade tracker with an empty dictionary for storing course grades.
add_courses: Prompts the user to enter a course name and score, and then stores this information in the grade dictionary.
display_grade: Displays the grades for each course stored in the grade dictionary.
calculate_Total_grade: Calculates and displays the total score of all courses.
start: Starts the program, providing a menu for the user to add courses, display grades, calculate the total grade, or exit the program.
This implementation provides a basic console-based interface for managing course grades, and can be extended or modified for more advanced features as needed.

