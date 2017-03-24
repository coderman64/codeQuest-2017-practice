from __future__ import print_function      

class Student(object):
    def __init__(self, fullInput):
        self.orgName = fullInput.translate(None, '\n')
        self.arrayName = fullInput.split(':')
        self.name = self.arrayName[0]
        self.credits = self.arrayName[1].split(',')
        self.gpa = 0
        self.totalCredits = 0
        for classTaken in self.credits:
            creditHours = 0
            if 'A' in classTaken:
                creditHours = int(classTaken.strip('A'))
                self.gpa += 4 * creditHours
            elif 'B' in classTaken:
                creditHours = int(classTaken.strip('B'))
                self.gpa += 3 * creditHours              
            elif 'C' in classTaken:
                creditHours = int(classTaken.strip('C'))
                self.gpa += 2 * creditHours        
            elif 'D' in classTaken:
                creditHours = int(classTaken.strip('D'))
                self.gpa += 1 * creditHours
            self.totalCredits += creditHours
        if self.totalCredits != 0:## prevents divison by 0 when Brendan(initial blank student) created
            self.gpa = float(self.gpa)/self.totalCredits
        ##print(self.name+' Gpa: '+str(self.gpa)+' Credits: '+str(self.totalCredits)) Debugging
        
f = open('Prob06CustomIn.txt', 'r')
numTests = int(f.readline())

## Could make this OOP, but instead just going iteratively for now, nevermind have to use OOP
for i in xrange(0, numTests):##For each high school
    highSchool = (f.readline()).strip('\n')
    numStudents = int(f.readline())
    
    students = []
    for x in xrange(0, numStudents):## For each student
        students.append(Student(f.readline()))
        
    valedictorian = Student('Brendan:')
    for student in students:
        if student.gpa > valedictorian.gpa:
            valedictorian = student
        elif student.gpa == valedictorian.gpa:## Tiebreaker is credithours
            if student.totalCredits > valedictorian.totalCredits:
                valedictorian = student
             
    print(highSchool+' = '+valedictorian.name)

f.close()