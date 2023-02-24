from main import Student

try:
    user_student_name = input("Enter student name \n")
    user_student_id = input("Enter student id \n")
    user_student_class = input("Enter student class \n")

    Student.create(student_name=user_student_name, student_id=user_student_id, student_class=user_student_class)
    print("Student created successfully")

except:
    print("Failed to created student details")
