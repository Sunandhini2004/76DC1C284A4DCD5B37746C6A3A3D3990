class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage:
if __name__ == "__main__":
    # Create a list of student objects
    students = [
        Student("Alice", "A123", 3.8),
        Student("Bob", "B456", 3.5),
        Student("Charlie", "C789", 3.9),
        # Add more students as needed
    ]

    # Sort the list of students by CGPA in descending order
    sorted_students = sort_students(students)

    # Print the sorted list of students
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")