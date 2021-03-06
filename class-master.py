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
            infoLine = infoLine.strip()
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
        print("\n")
        if self.dueDate == 1 or self.dueDate == 21 or self.dueDate == 31: numberThing = "st"
        elif self.dueDate == 2 or self.dueDate == 22: numberThing = "nd"
        elif self.dueDate == 3 or self.dueDate == 23: numberThing = "rd"
        else: numberThing = "th"
        print(f"Name: {self.assignmentName}\n   {self.shortDescription}\n\nUrl: {self.assignmentURL}\n\nClass: {self.className}\n\nDue on the {self.dueDate}{numberThing}")
        input("\nPress enter to continue")
        os.system('cls')


class ClassMegaList:
    def __init__(self, classFile, assignmentFile):
        self.classFile = classFile
        self.assignmentFile = assignmentFile
        self.classList = self.addSavedClasses(classFile)
        self.assnList = self.addSavedAssignments(assignmentFile)

    def addSavedClasses(self, classInfo: str):
        allClasses = []
        with open(classInfo) as clsMegaList:
            for classData in clsMegaList.readlines():
                if classData[0] == "#" or len(classData) < 3: continue
                else: allClasses.append(ClassInfo(classData))
        return allClasses

    def addNewClass(self):
        os.system('cls')
        print()
        self.classList.append(ClassInfo())

    def addSavedAssignments(self, assignInfo: str):
        allAssn = []
        with open(assignInfo) as assnInfo:
            for classData in assnInfo.readlines():
                if classData[0] == "#": continue
                else: allAssn.append(ClassAssignment(classData))
        return allAssn

    def addNewAssignment(self):
        os.system('cls')
        print()
        self.assnList.append(ClassAssignment())

    def printAllAssignments(self):
        if len(self.assnList) == 0:
            print("No assignments right now!\n")
        else:
            print("Assignments coming up:\n")
            for assn in self.assnList:
                if assn.dueDate == 1 or assn.dueDate == 21 or assn.dueDate == 31: numberThing = "st"
                elif assn.dueDate == 2 or assn.dueDate == 22: numberThing = "nd"
                elif assn.dueDate == 3 or assn.dueDate == 23: numberThing = "rd"
                else: numberThing = "th"
                print(f"{assn.assignmentName} : Due on the {assn.dueDate}{numberThing}")

    def printAllClasses(self):
        if len(self.assnList) == 0:
            print("No classes yet!")
        else:
            print("Classes:")
            for cls in self.classList:
                print(f"{cls.className}")

        input("Press enter to continue")

    def removeAssignment(self):
        while True:
            os.system('cls')
            print(f"Please type the assignment you would like to remove: (or type stop)")
            self.printAllAssignments()
            chosenAssignment = input()
            if chosenAssignment == "stop":
                break
            else:
                for assn in self.assnList:
                    if chosenAssignment == assn.assignmentName:
                        self.assnList.remove(assn)

    def saveQuit(self):
        print("Saving...\n")
        with open(self.classFile, "w") as f:
            f.seek(0)
            f.truncate(0)
            for cls in self.classList:
                print(cls.formatForSaving(), file=f)
        with open(self.assignmentFile, "w") as f:
            f.seek(0)
            f.truncate(0)
            for assn in self.assnList:
                print(assn.formatForSaving(), file=f)

        input("Saved\nPress enter to close program")
        exit()

    def mainLoop(self):
        running = True
        validChoices = ["add class", "add assignment", "all classes", "all assignments", "class info", "assignment info", "remove assignment", "quit"]
        while running:
            print("\n")
            self.printAllAssignments()
            choice = input(f"\n\nPlease choose an option:\n\t{validChoices[0]}\n\t{validChoices[1]}\n\t{validChoices[2]}\n\t{validChoices[3]}\n\t{validChoices[4]}\n\t{validChoices[5]}\n\t{validChoices[6]}\n\t{validChoices[7]}\n").lower()
            if choice in validChoices:
                if choice == validChoices[0]:
                    self.addNewClass()
                elif choice == validChoices[1]:
                    self.addNewAssignment()
                elif choice == validChoices[2]:
                    self.printAllClasses()
                elif choice == validChoices[3]:
                    self.printAllAssignments()
                elif choice == validChoices[4]:
                    os.system('cls')
                    self.printAllClasses()
                    chosenClass = input(f"\nPlease type the class name you want more info about:")

                    validClass = False
                    for cls in self.classList:
                        if chosenClass == cls.className:
                            cls.printClassInfo()
                            validClass = True
                    if not validClass: print("That class does not exist")
                elif choice == validChoices[5]:
                    os.system('cls')
                    print()
                    self.printAllAssignments()
                    chosenAssn = input(f"\nPlease type the assignment name you want more info about:\n")

                    validAssn = False
                    for assn in self.assnList:
                        if chosenAssn == assn.assignmentName:
                            assn.printAssignmentInfo()
                            validAssn = True
                    if not validAssn: print("That assignment does not exist")
                elif choice == validChoices[6]:
                    self.removeAssignment()
                elif choice == validChoices[7]:
                    self.saveQuit()
            else:
                os.system('cls')
                print("Invalid Choice\n")


if __name__=="__main__":
    os.system('cls')
    classMaster = ClassMegaList("classes.txt", "assignments.txt")
    classMaster.mainLoop()