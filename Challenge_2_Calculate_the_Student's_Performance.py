# Problem statement#
# Implement a class - Student - that has four properties and two methods. All these attributes (properties and methods) should be public. This problem can be broken down into three tasks.
#
# Task 1#
# Implement a constructor to initialize the values of four properties: name, phy, chem, and bio.
#
# Task 2#
# Implement a method – totalObtained – in the Student class that calculates total marks of a student.
#
# Sample properties
#
# name = Mark
# phy  = 80
# chem = 90
# bio  = 40
# Sample method output
#
# obj1.Total()=210
# Task 3#
# Using the totalObtained method, implement another method, percentage, in the Student class that calculates the percentage of students marks. Assume that the total marks of each subject are 100. The combined marks of three subjects are 300.
#
# The formula for calculating the percentage is given below.
#
# Percentage=Percentage= (MarksObtained/TotalMarks)X 100
# Sample input
#
# phy  = 80
# chem = 90
# bio  = 40
# Sample output
# 70

class Student:
    def __init__(self,name,phy,chem,bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio
    def totalObtained(self):
        return  (self.phy+self.chem+self.bio)

    def percentage(self):
        total = self.totalObtained()
        total= (total/300) * 100
        return total

obj = Student('Mark',80,90,40)
print(obj.percentage())