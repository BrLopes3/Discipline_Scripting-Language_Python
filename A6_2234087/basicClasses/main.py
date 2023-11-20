from certificationExam import CertificationExam
from person import Person
from candidate import Candidate
from doCertificationExam import DoCertificationExam

if __name__ == '__main__':
    
    p1 = Person("London", "John", "438555222")
    p2 = Person("Smith", "Jane", "438555333")
    p3 = Person("Jordan", "Michael", "438555444")
    print(p1)
    print(p2)
    print(p3)

    certification1 = CertificationExam("1z0-151","Java", 60, 30)
    certification2 = CertificationExam("1z0-147","Python", 70, 20)
    print(certification1)
    print(certification2)

    ## testing creating the objects candidate with the hard coded values
    candidate1 = Candidate("London", "John", "438555222", certification1, "2020-12-01")
    candidate2 = Candidate("Smith", "Jane", "438555333", certification1, "2020-12-02")
    candidate3 = Candidate("Jordan", "Michael", "438555444", certification2, "2020-12-03")
    ##return fail because we do not have the grade yet
    print(candidate1)
    print(candidate2)
    print(candidate3)

    ## testing the method serviceSuccess
    candidate1.setExamMark(66)
    




