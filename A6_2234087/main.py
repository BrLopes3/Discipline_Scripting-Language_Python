from basicClasses import Person
from basicClasses import CertificationExam
from basicClasses import Candidate
from basicClasses import DoCertificationExam

if __name__ == '__main__':
    
    p1 = Person("London", "John", "438555222")
    p2 = Person("Smith", "Jane", "438555333")
    p3 = Person("Jordan", "Michael", "438555444")
    print(p1)
    print(p2)
    print(p3)

    ##create the certification exam
    certification1 = CertificationExam("Java", 60, 30)
    certification2 = CertificationExam("Python", 70, 20)
    print(certification1)
    print(certification2)

    

    ##call the method to read the file
    candidates = DoCertificationExam.readFile()
    print(candidates)

    ## candidate1
    mark1 = DoCertificationExam.getMark("1z0-151", "London")
    mark1 = int(mark1)
    print(mark1)
    grade1 = DoCertificationExam.getGrade(mark1)
    print(grade1)
    
    candidate1 = Candidate("London", "John", "438555222", certification1, 2023-3-21)
    candidate1.setExamMark(mark1)
    doexam1 = DoCertificationExam(candidate1)
    doexam1.validateCertification()
    print(candidate1)

    
    

    ## candidate2
    mark2 = DoCertificationExam.getMark("1z0-147", "Smith")
    mark2 = int(mark2)
    print(mark2)
    grade2 = DoCertificationExam.getGrade(mark2)
    print(grade2)
    candidate2 = Candidate("Smith", "Jane", "438555333", certification2, 2023-3-22)
    candidate2.setExamMark(mark2)
    doexam2 = DoCertificationExam(candidate2)
    doexam2.validateCertification()
    print(candidate2)


    ## candidate3
    mark3 = DoCertificationExam.getMark("1z0-151", "Jordan")
    mark3 = int(mark3)
    print(mark3)
    grade3 = DoCertificationExam.getGrade(mark3)
    print(grade3)
    candidate3 = Candidate("Jordan", "Michael", "438555444", certification1, 2023-3-23)
    candidate3.setExamMark(mark3)
    doexam3 = DoCertificationExam(candidate3)
    doexam3.validateCertification()
    print(candidate3)


    




