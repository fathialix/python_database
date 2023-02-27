from main import User
from main import Student
from main import People

myusers = User.select()
for user in myusers:
    print(user.name, user.email, user.password)

mystudents = Student.select()
for student in mystudents:
    print(student.student_name, student.student_id, student.student_class)

mypeoples = People.select()
for people in mypeoples:
    print(people.name, people.phone_number, people.email, people.county, people.gender, people.religion, people.password)
