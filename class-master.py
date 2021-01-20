import os


class ClassInfo:
    def __init__(self, infoLine=""):
        self.className = ""
        self.instructor = ""
        self.contactInfo = ""
        self.whatToCallProf = ""
        self.classMainURL = ""
        self.applyInfo(infoLine)

    def formatForSaving(self) -> str:
        return f"{self.className}|{self.instructor}|{self.contactInfo}|{self.whatToCallProf}|{self.classMainURL}"

    def applyInfo(self, infoLine: str):
        if infoLine == "":
            print("This is a new class, please enter the following information: ")
            self.className = input("Please enter the class name: \n\t")
            self.instructor = input("Please enter the instructor's name: \n\t")
            self.contactInfo = input("Please enter the email to contact the instructor: \n\t")
            self.whatToCallProf = input("Please enter the preferred name of the professor (or . if unknown): \n\t")
            self.classMainURL = input("Please enter the URL for the class: \n\t")
        else:
            splitInfo = infoLine.split("|")
            self.className = splitInfo[0]
            self.instructor = splitInfo[1]
            self.contactInfo = splitInfo[2]
            self.whatToCallProf = splitInfo[3]
            self.classMainURL = splitInfo[4]

    def modifyClassInfo(self):
        validInfo = ["class name", "instructor", "contact info", "professor preferred name", "class url", "stop"]
        while True:
            infoToModify = input(
                f"What would you like to change? (lowercase ok)\n\tClass Name: {self.className}\n\tInstructor: {self.instructor}\n\tContact Info: {self.instructor}\n\tProfessor Preferred Name: {self.whatToCallProf}\n\tClass URL: {self.classMainURL}\n\tStop").lower()
            if infoToModify in validInfo:
                if infoToModify == validInfo[0]:  # changing class name
                    self.className = input("Please type the new class name:\n\t")
                elif infoToModify == validInfo[1]:
                    self.instructor = input("Please type the instructor name:\n\t")
                elif infoToModify == validInfo[2]:
                    self.contactInfo = input("Please type the professor's email:\n\t")
                elif infoToModify == validInfo[3]:
                    self.whatToCallProf = input("Please type the professor's preferred name:\n\t")
                elif infoToModify == validInfo[4]:
                    self.classMainURL = input("Please type the class URL:\n\t")
                elif infoToModify == validInfo[5]:
                    break
                os.system('cls')
                print("Value changed")
            else:
                os.system('cls')
                print("Invalid option, please select again")

    def printClassInfo(self):
        os.system('cls')
        print(
            f"Class Name: {self.className}\n\tInstructor: {self.instructor}\n\tContact Info: {self.instructor}\n\tProfessor Preferred Name: {self.whatToCallProf}\n\tClass URL: {self.classMainURL}")
        input("\nPress enter to continue")
        os.system('cls')


class ClassAssignment:
    def __init__(self, infoLine=""):
        self.assignmentName = ""
        self.shortDescription = ""
        self.assignmentURL = ""
        self.className = ""
        self.dueDate = 0
        self.applyInfo(infoLine)

    def formatForSaving(self) -> str:
        return f"{self.assignmentName}|{self.shortDescription}|{self.assignmentURL}|{self.className}|{self.dueDate}"

    def applyInfo(self, infoLine: str):
        if infoLine == "":
            print("This is a new assignment, please enter the following information: ")
            self.assignmentName = input("Please enter the assignment name: \n\t")
            self.shortDescription = input("Please enter a description: \n\t")
            self.assignmentURL = input("Please enter assignment URL: \n\t")
            self.className = input("Please enter the class this assignment is from: \n\t")
            self.dueDate = int(input("Please enter the day this assignment is due (ex: 23 for the 23rd): \n\t"))
        else:
            splitInfo = infoLine.split("|")
            self.assignmentName = splitInfo[0]
            self.shortDescription = splitInfo[1]
            self.assignmentURL = splitInfo[2]
            self.className = splitInfo[3]
            self.dueDate = int(splitInfo[4])

    def printAssignmentInfo(self):
        os.system('cls')
        if self.dueDate == 1 or self.dueDate == 21 or self.dueDate == 31: numberThing = "st"
        elif self.dueDate == 2 or self.dueDate == 22: numberThing = "nd"
        elif self.dueDate == 3 or self.dueDate == 23: numberThing = "rd"
        else: numberThing = "th"
        print(f"{self.assignmentName}\n\t{self.shortDescription}\n{self.assignmentURL}\n{self.className}\nDue on the {self.dueDate}{numberThing}")
        input("\nPress enter to continue")
        os.system('cls')


class ClassMegaList:
    def __init__(self, classFile, assignmentFile):
        self.classList = self.addSavedClasses(classFile)
        self.assnList = self.addSavedAssignments(assignmentFile)
        self.printAllAssignments()

    def addSavedClasses(self, classInfo: str):
        allClasses = []
        with open(classInfo) as clsMegaList:
            for classData in clsMegaList.readlines():
                if classData[0] == "#": continue
                else: allClasses.append(ClassInfo(classData))
        return allClasses

    def addNewClass(self):
        self.classList.append(ClassInfo())

    def addSavedAssignments(self, assignInfo: str):
        allAssn = []
        with open(assignInfo) as assnInfo:
            for classData in assnInfo.readlines():
                if classData[0] == "#": continue
                else: allAssn.append(ClassAssignment(classData))
        return allAssn

    def addNewAssignment(self):
        self.assnList.append(ClassAssignment())

    def printAllAssignments(self):
        if self.assnList.count() == 0:
            print("No assignments right now!")
        else:
            print("Assignments coming up:")
            for assn in self.assnList:
                if assn.dueDate == 1 or assn.dueDate == 21 or assn.dueDate == 31: numberThing = "st"
                elif assn.dueDate == 2 or assn.dueDate == 22: numberThing = "nd"
                elif assn.dueDate == 3 or assn.dueDate == 23: numberThing = "rd"
                else: numberThing = "th"
                print(f"{assn.assignmentName} : Due on the {assn.dueDate}{numberThing}")

    def removeAssignment(self):
        while True:
            os.system('cls')
            print(f"Please type the assignment you would like to remove: (or type stop)\n\t{self.printAllAssignments()}")
            chosenAssignment = input()
            if chosenAssignment == "stop":
                break
            else:
                for assn in self.assnList:
                    if chosenAssignment == assn.assignmentName:
                        self.assnList.remove(assn)
