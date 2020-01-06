from classes import *

if __name__ == "__main__":
    myStudentStack = Stack()
    
menu = input("What would you like to do?\n1. Add a student\n2. Remove students from stack.\n3. Return the top of the text.\n4. Exit")
while menu == '1':
    firstName = input("What is the first name of the student you are entering?")
    lastName = input("What is the last name of the student you are entering?")
    age = input("What is the age of the student you are entering?")
    level = input("What level is the student at?")
    student1 = student()

    student1.setFirstName(firstName)
    student1.setLastName(lastName)
    student1.setAge(age)
    student1.setLevel(level)
    myStudentStack.push(student1)
    myStudentStack.display()

    menu = input("What would you like to do?\n1. Add a student\n2. Remove students from stack.\n3. Return the top of the text.\n4. Exit")
while menu == '2':
    myStudentStack.pop()
    myStudentStack.display()
    menu = input("What would you like to do?\n1. Add a student\n2. Remove students from stack.\n3. Return the top of the text.\n4. Exit")
while menu == '3':
    myStudentStack.top()
    menu = input("What would you like to do?\n1. Add a student\n2. Remove students from stack.\n3. Return the top of the text.\n4. Exit")
while menu == '4':
    exit()
