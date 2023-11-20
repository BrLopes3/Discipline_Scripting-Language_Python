"""
Create the class DoCertificationExam with the following characterises:
• Attributes:
▪ candidate type Candidate
▪ Two objects from CertificationExam class {1z0-151: Java and 1z0-
147: Python)

1z0-151,Jordan,66
1z0-151,London,90
1z0-147,Smith,59

"""
from certificationExam import CertificationExam
from candidate import Candidate

class DoCertificationExam:

    def __init__(self, candidate):
        self._candidate = candidate
        self._Java = CertificationExam("1z0-151","Java", 60, 30)
        self._Python = CertificationExam("1z0-147","Python", 70, 20)
        self._validateCertification()
    ## gethers and setters
    def getCandidate(self):
        return self._candidate
    
    def getJava(self):
        return self._Java
    
    def getPython(self):
        return self._Python
    
    def setCandidate(self, candidate):
        self._candidate = candidate

    ##methods

   ## def getGrade(self, examMark):
   ##     Candidate.setExamMark(examMark)

    
    ##read file txt with the candidates and their marks
    
    def readFile():
        fd = open("Mark.txt", "r")
        candidates = fd.readlines() ##return a list of strings
        candidateMark = ()
        for candidate in candidates:
            candidate = candidate.strip()
            candidate.split(",")
            if len(candidate)==3:
                examId = candidate[0]
                lastName = candidate[1]
                mark = candidate[2]
                candidateMark[examId, lastName] = int(mark)
        fd.close()
        return candidateMark


    def getMark(self, examId, lastName):
        candidateMarks = self.readFile()
        return candidateMarks.get((examId, lastName), -1)
    
    def getGrade(self, examMark):
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
        javaMark = self.getMark(self._Java.getId(), self._candidate.getLastName())
        
        if javaMark >= self._Java.getSuccessMark():
            examGrade = self.getGrade(javaMark)
            self._candidate.serviceSuccess(examGrade)
        else:
            self.candidate.serviceFail(self._Java.getDaysWait())
    
        pythonMark = self.getMark(self._Python.getId(), self._candidate.getLastName())
        
        if pythonMark >= self._Python.getSuccessMark():
            examGrade = self.getGrade(pythonMark)
            self._candidate.serviceSuccess(examGrade)
        else:
            Candidate.serviceFail(self._Python.getDaysWait())
    ## toString method

    def __str__(self):

        return f"{self._candidate}"
        


        
    

        