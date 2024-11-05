class student:

    def __init__(self, name, age):
        print("college info")
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name} age is {self.age}")

class college(student):
    def showclg(self):
        print(f"sycet student")



a = college("Sakshi", 21)
b = college("Sumit", 26)  
c = student("gfh",5)

#a = student()
#a.name = "sumit"
#a.age = 26

#b = student()
#b.name = "renuka"
#b.age = 20

a.info()
b.info()
a.showclg()
b.showclg()
c.info()

