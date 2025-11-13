class Student:
    """Represents a student with basic identifying information."""

    def __init__(self, name: str, age: int, student_id: str) -> None:
        """Initialize a new Student instance."""
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_details(self) -> None:
        """Print the stored student details."""
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")


if __name__ == "__main__":
    demo_student = Student("Alice Johnson", 20, "S12345")
    demo_student.display_details()

