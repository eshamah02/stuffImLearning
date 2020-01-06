class linkedList:
    head = None
    numberOfStudents = 0

    def _init_(self):
        self.head = None

    def insert(self, student):
        
        self.numberOfStudents = self.numberOfStudents + 1

        if self.numberOfStudents == 1:
            new = student
            new.next = None
            self.head=new
        else:
            new = student
            new.next = self.head
            self.head = new

    def delete(self, firstName, lastName):
        prev = None
        curr = self.head
        while curr.firstName != firstName and curr.lastName != lastName:
            prev = curr
            curr = curr.next
        else:
            prev.next = curr.next
            curr = None

        self.numberOfStudents = self.numberOfStudents - 1

    def displayAllNodes(self):
        curr = self.head
        while curr != None:
            print('First Name: ' + curr.firstName)
            print('Last Name: ' + curr.lastName)
            print('Age: ' + curr.age)
            print('Level: ' + curr.level)
            curr = curr.next

    def numberOfNodes(self):
        print('Number of Students: ' + str(self.numberOfStudents))

    def reverseLinkedList(self):
        prev = None
        while self.head != None:
            curr = self.head
            self.head = (self.head).next
            curr.next = prev
            prev = curr
            print(curr.firstName)
        self.head = curr


class student:
    firstName = ""
    lastName = ""
    age = ""
    level = ""

    def _init_(self):
        print("Created")
    
    def setFirstName(self, studentFirst):
        self.firstName = studentFirst

    def setLastName(self, studentLast):
        self.lastName = studentLast

    def setAge(self, studentAge):
        self.age = studentAge

    def setLevel(self, studentLevel):
        self.level = studentLevel


class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def top(self):
        lastItem = self.items[-1]
        print(lastItem.firstName)
        print(lastItem.lastName)
        print(lastItem.age)
        print(lastItem.level)

    def display(self):
        for item in self.items:
            print(item.firstName)
            print(item.lastName)
            print(item.age)
            print(item.level)
            

