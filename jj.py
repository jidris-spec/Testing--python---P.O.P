class GradeTracker:
        def __init__(self):
            self.grade = {}
        def add_courses(self):
            course_name = input("Enter your preffered course: ")
            score = float(input("Enter your score: "))
            if course_name in self.grade:
                self.grade[course_name] += score
            else:
                self.grade[course_name] = score
            print(f"You scored {score} in {course_name}.")

        def display_grade(self):
            print("Here are your grade")
            for course_name, score in self.grade.items():
                print(f"Your overall score in {course_name} is {score}.")
        def calculate_Total_grade(self):
             total = sum(self.grade.values())
             print(f"Total score: {total}")
        def start (self):
             self.calculate_Total_grade()
             while True:
                print("\n1. Add courses\n2. Display Grade\n3. Calculate Total Grade\n4. Exit ")
                choice = input("Choose an option ")
                if choice == "1":
                    self.add_courses()
                elif choice == "2":
                    self.display_grade()
                elif choice == "3":
                    self.calculate_Total_grade()
                elif choice == "4":
                    print("Exiting program can't wait to see you again")
                    break
                else:
                    print("invalid option kindly try again")
grade_tracker = GradeTracker()
grade_tracker.start()                    

