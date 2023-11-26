
"""
Create the class Person with the following characterises:
    Attributes:
▪ Last Name
▪ First Name
▪ Phone type
"""

class Person:

    ## parameterized constructor
    def __init__(self, last_name, first_name, phone_type):
        self._last_name = last_name
        self._first_name = first_name
        self._phone_type = phone_type

    ## getters
    def getLastName(self):
        return self._last_name
    
    def getFirstName(self):
        return self._first_name
    
    def getPhoneType(self):
        return self._phone_type
    
    ## setters

    def setLastName(self, lastName):
        self._last_name = lastName

    def setFirstName(self, firstName):
        self._first_name = firstName

    def setPhoneType(self, phoneType):
        self._phone_type = phoneType
    
    ## toString method
    def __str__(self):
        return f"First Name: {self._first_name}, Last Name: {self._last_name}, Phone: {self._phone_type}"
    
"""
Create the class CertificationExam with the following characterises:
 Attributes:
▪ id
▪ title
▪ successMark
▪ number of days wait.

"""

class CertificationExam:
    __seq = 100
    ## parameterized constructor
    def __init__(self, title, success_mark, days_wait):
        self._id = CertificationExam.__seq
        CertificationExam.__seq += 1
        self._title = title
        self._success_mark = int(success_mark)
        self._days_wait = int(days_wait)

    
    ## getters

    def getId(self):
        return self._id
    
    def getTitle(self):
        return self._title
    
    def getSuccessMark(self):
        return self._success_mark
    
    def getDaysWait(self):
        return self._days_wait
    
    ## setters

    def setTitle(self, title):
        self._title = title

    def setDaysWait(self, daysWait):
        self._days_wait = daysWait

    def setSuccessMark(self, successMark):
        self._success_mark = successMark

    
    ## toString method
    def __str__(self):
        return f"ID: {self._id}, Title: {self._title}, Success Mark: {self._success_mark}, Numbers of Days to Wait: {self._days_wait}"
    

"""
Create the class Candidate that inherits from Person with the following characterises:

Attributes:
▪ certificationExam (type CertificationExam)
▪ examDate
▪ examMark
▪ grade
▪ nbDaysToWait

the class candidate hinrerit from Person and the class provides access methods and modifies the attributes for
examDate, examMark and certificationExam

"""

class Candidate(Person):
    
    __seqCandidate = 1000
    def __init__(self, last_name, first_name, phone, certificationExam, examDate):
        super().__init__(last_name, first_name, phone)
        self.__id = Candidate.__seqCandidate
        Candidate.__seqCandidate += 1
        self._certificationExam = certificationExam
        self._examDate = examDate
        self._examMark = None ##will be initialized by the doCertificationExam class
        self._grade = None ##will be initialized by the doCertificationExam class
        self._nbDaysToWait = None ##will be initialized by the doCertificationExam class

    ## getters and setters
    ##The class provides access methods and modifies the attributes for
    ##examDate, examMark and certificationExam
    def getCertificationExam(self):
        return self._certificationExam
    
    def getExamDate(self):
        return self._examDate
    
    def getExamMark(self):
        return self._examMark
    
    def getGrade(self):
        return self._grade
    
    def getNumberDaysToWait(self):
        return self._nbDaysToWait
    
    def setCertificationExam(self):
        return self._certificationExam
    
    def setExamDate(self, examDate): 
        self._examDate = examDate
    
    def setExamMark(self, examMark): ##will be initialized by the doCertificationExam class
        self._examMark = examMark

    
    ## methods
    def serviceSuccess(self, grade):
        self._grade = grade
            
    def serviceFail(self, nod):
        self._nbDaysToWait = nod

    ## toString method

    def __str__(self):
        if self._grade != None:
            return f"Pass Certification exam: {self.getFirstName()} {self.getLastName()} Certification Exam id: {self._certificationExam.getId()} Exam Title: {self._certificationExam.getTitle()} Mark: {self._examMark}"
        else:
            self.serviceFail(self._certificationExam.getDaysWait())
            return f"Fails Certification exam: {self.getFirstName()} {self.getLastName()} Certification Exam id: {self._certificationExam.getId()} Exam Title: {self._certificationExam.getTitle()} Mark: {self._examMark} Number Of Days to Wait {self._nbDaysToWait}" 
        


class DoCertificationExam:
    ## parameterized constructor that receives a candidate object

    def __init__(self, candidate):
        self._candidate = candidate
        self._Java = CertificationExam("Java", 60, 30)
        self._Python = CertificationExam("Python", 70, 20)
       
    ## gethers and setters
    def getCandidate(self):
        return self._candidate
    
    def getJava(self):
        return self._Java
    
    def getPython(self):
        return self._Python
    
    def setCandidate(self, candidate):
        self._candidate = candidate

    
    ##read file txt with the candidates and their marks

    @staticmethod
    def readFile():
        candidateMarks = []
        with open("./Mark.txt", "r") as rf:
            candidateLine = rf.read().split("\n")
            for candidate in candidateLine:
                candidate = candidate.split(",")
                examId = candidate[0]
                lastName = candidate[1]
                examMark = candidate[2]
                ##create a dictionary with the examId and the lastName as key and the examMark as value
                candidateMark = {(examId, lastName): examMark}
                candidateMarks.append(candidateMark)

        return (candidateMarks)
        
    ##get the mark of the candidate using the examId and the lastName as parameters
    def getMark(examId, lastName):
        candidateMarks = DoCertificationExam.readFile()
        for candidateMark in candidateMarks:
            for key, value in candidateMark.items():
                if key[0] == examId and key[1] == lastName:
                    return value
    


    @staticmethod
    def getGrade(examMark):
        if examMark >= 95:
            return "A+"
        elif examMark >= 90:
            return "A"
        elif examMark >= 85:
            return "B+"
        elif examMark >= 80:
            return "B"
        elif examMark >= 75:
            return "C+"
        elif examMark >= 70:
            return "C"
        elif examMark >= 65:
            return "D+"
        elif examMark >= 60:
            return "D"
        else:
            return "E"
    
    
    
    def validateCertification(self):
        ##if the candidate's certification exam is Java
        if self._candidate.getCertificationExam().getTitle() == 'Java':
            ##if the candidate's mark is greater or equal to the success mark
            if self._candidate.getExamMark() >= self._Java.getSuccessMark():
                ##set the grade
                self._candidate.serviceSuccess(self.getGrade(self._candidate.getExamMark()))
            else:
                ##set the number of days to wait
                self._candidate.serviceFail(self._Java.getDaysWait())
        else:
            if self._candidate.getExamMark() >= self._Python.getSuccessMark():
                self._candidate.serviceSuccess(self.getGrade(self._candidate.getExamMark()))
            else:
                self._candidate.serviceFail(self._Python.getDaysWait())

    ## toString method

    def __str__(self):

        self.validateCertification()

        return f"{self._candidate}"
        



        
    

                    
