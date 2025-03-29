class Student:
    def __init__(self, name, roll_no, marks: dict[str, int]):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def add_marks(self, subject, score):
        self.marks[subject] += score
    
    def calc_average(self):
        total_marks = 0
        for mark in self.marks.values():
            total_marks += mark
        return total_marks / len(self.marks.values())

    def show_student_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")
        for subject, marks in self.marks.items():
            print(f"Marks in subject {subject} are: {marks}.")


class Teacher:
    def __init__(self, name, teacher_id, subject):
        self.name = name
        self.teacher_id = teacher_id
        self.subject = subject
    
    def assign_marks_to_student(self, student: Student, marks):
        