import pandas as pd

class GradingSystem:
    def __init__(self, csv_filename):
        self.csv_filename = csv_filename
        self.load_students()

    def load_students(self):
        try:
            self.students_df = pd.read_csv(self.csv_filename)
        except FileNotFoundError:
            print(f"CSV file '{self.csv_filename}' not found.")
            self.students_df = pd.DataFrame(columns=['Name', 'Email', 'Attempts', 'Grade'])
            
    def create_grade_table(self):
        self.students_df['Grade'] = None
        self.students_df['Attempts'] = 0

    def store_grades(self):
        excel_filename = "grades.xlsx"
        self.students_df.to_excel(excel_filename, index=False, engine='openpyxl')

    def record_attempt(self, student_name):
        if student_name in self.students_df['Name'].values:
            idx = self.students_df.index[self.students_df['Name'] == student_name][0]
            self.students_df.at[idx, 'Attempts'] += 1
        else:
            print(f"Student '{student_name}' not found.")

    def assign_grade(self, student_name, grade):
        if student_name in self.students_df['Name'].values:
            idx = self.students_df.index[self.students_df['Name'] == student_name][0]
            self.students_df.at[idx, 'Grade'] = grade
        else:
            print(f"Student '{student_name}' not found.")

if __name__ == "__main__":
    csv_filename = input("Enter the CSV filename with student names and email addresses: ")
    grading_system = GradingSystem(csv_filename)
    
    while True:
        print("\nOptions:")
        print("1. Create Grade Table")
        print("2. Record Attempt")
        print("3. Assign Grade")
        print("4. Store Grades")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            grading_system.create_grade_table()
            print("Grade table created.")
        elif choice == "2":
            student_name = input("Enter student name: ")
            grading_system.record_attempt(student_name)
        elif choice == "3":
            student_name = input("Enter student name: ")
            grade = input("Enter grade: ")
            grading_system.assign_grade(student_name, grade)
        elif choice == "4":
            grading_system.store_grades()
            print("Grades stored in Excel file.")
        elif choice == "5":
            break

  
