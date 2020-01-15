class Students_room():
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def students_info(self):
        print(f"name: {self.name}, age: {self.age}, major: {self.major}")

student1 = Students_room("Steve", "23", "English")
student1.students_info()
student2 = Students_room("Johnny", "24", "Biology")
student2.students_info()
student3 = Students_room("Penny", "21", "Physics")
student3.students_info()