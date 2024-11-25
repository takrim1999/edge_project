class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare(self,another):
        if self.age > another.age:
            print(f"{self.name} is elder")
            print("Age is: ", self.age)
        elif self.age < another.age:
            print(f"{another.name} is elder")
            print("Age is: ", another.age)
        else:
            print("Both are same!")

person1 = Person(input("Name: "),int(input("Age: ")))
person2 = Person(input("Name: "),int(input("Age: ")))
person1.compare(person2)