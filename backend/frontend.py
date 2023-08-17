import tkinter as tk
from grading_system import GradingSystem

class GradingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Grading System GUI")
        
        self.grading_system = GradingSystem("students.csv")
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Grading System GUI")
        self.label.pack(pady=10)
        
        self.create_grade_table_button = tk.Button(self.root, text="Create Grade Table", command=self.create_grade_table)
        self.create_grade_table_button.pack()
        
        self.record_attempt_button = tk.Button(self.root, text="Record Attempt", command=self.record_attempt)
        self.record_attempt_button.pack()
        
        self.assign_grade_button = tk.Button(self.root, text="Assign Grade", command=self.assign_grade)
        self.assign_grade_button.pack()
        
        self.store_grades_button = tk.Button(self.root, text="Store Grades", command=self.store_grades)
        self.store_grades_button.pack()
        
        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy)
        self.quit_button.pack()
        
    def create_grade_table(self):
        self.grading_system.create_grade_table()
        self.show_message("Grade table created.")
        
    def record_attempt(self):
        student_name = self.get_input("Enter student name:")
        self.grading_system.record_attempt(student_name)
        self.show_message("Attempt recorded.")
        
    def assign_grade(self):
        student_name = self.get_input("Enter student name:")
        grade = self.get_input("Enter grade:")
        self.grading_system.assign_grade(student_name, grade)
        self.show_message("Grade assigned.")
        
    def store_grades(self):
        self.grading_system.store_grades()
        self.show_message("Grades stored in Excel file.")
        
    def get_input(self, prompt):
        return tk.simpledialog.askstring("Input", prompt)
    
    def show_message(self, message):
        tk.messagebox.showinfo("Message", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = GradingGUI(root)
    root.mainloop()
