class Person:
    def __init__(self,name,age,height): 
        self.name = name;
        self.age = age;
        self.height = height;
    
    def sayHello(self):
        print("Hello " + str(self.name) + ", Nice to meet you")
        
    def ride(self):
        self.sayHello()
        if self.age > 10 and self.height >= 100:
            print("Congratulation " + str(self.name) +"! You may ride a roller coaster")
        else:
            print("Sorry " + str(self.name) + ", You may not ride a roller coaster")
    
james = Person("James",10,140)
rose = Person("Rose",12,150)
dove = Person("Dove",12,150)
diva = Person("Diva",8,130)

while True:
    name = input("Enter name :")
    if name == "james":
        james.ride()
    elif name == "rose":
        rose.ride()
    elif name == "dove":
        dove.ride()
    elif name == "diva":
        diva.ride()
    else:
        print("Invalid input")
    ans = input("'y' to continue / 'n' to quit:")
    if ans == "n":
        break