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
    def __init__(self, id, title, success_mark, days_wait):
        self._id = id
        self._title = title
        self._success_mark = success_mark
        self._days_wait = days_wait

    
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
    

