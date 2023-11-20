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

when I define the type of certificationExam, I have to import the class CertificationExam from the file certificationExam.py and 
initialize the attribute certificationExam with the constructor of the class CertificationExam, that will bring the pass grade and the number of days to wait
"""
from person import Person
from certificationExam import CertificationExam

class Candidate(Person):
    ## when we create a candidate we do not have the examMark or grade yet
    ## parameterized constructor
    __seqCandidate = 1000
    def __init__(self, last_name, first_name, phone, certificationExam, examDate):
        super().__init__(last_name, first_name, phone)
        self.__id = Candidate.__seqCandidate
        Candidate.__seqCandidate += 1
        self._certificationExam = certificationExam
        self._examDate = examDate
        self._examMark = None
        self._grade = None
        self._nbDaysToWait = None

    ## getters and setters

    def getCertificationExam(self):
        return self._certificationExam
    
    def getExamDate(self):
        return self._examDate
    
    def getExamMark(self):
        return self._examMark
    
    def setCertificationExam(self):
        return self._certificationExam
    
    def setExamDate(self):
        return self._examDate
    
    def setExamMark(self, examMark):
        self._examMark = examMark
    
    
    ## methods
    ##set the grade of 
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
        


            
