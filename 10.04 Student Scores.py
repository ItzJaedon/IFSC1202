class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = scores
    def RunningAverage(self):
        non_blank_scores = [int(score) for score in self.Grades if score != '']
        return sum(non_blank_scores) / len(non_blank_scores)
    def TotalAverage(self):
        scores = [int(score) if score != '' else 0 for score in self.Grades]
        return sum(scores) / len(scores)
    def LetterGrade(self):
        avg_score = self.TotalAverage()
        if avg_score >= 90:
            return 'A'
        elif avg_score >= 80:
            return 'B'
        elif avg_score >= 70:
            return 'C'
        elif avg_score >= 60:
            return 'D'
        else:
            return 'F'
students = [
    Student('Jim', 'Evans', 'T123456', ['80', '85', '']),
    Student('Joe', 'Smith', 'T654321', ['90', '85', '85']),
    Student('Jane', 'Doe', 'T121212', ['100', '', '70']),
]
print(f"{'First Name':<12} {'Last Name':<12} {'ID':<12} {'Running Average':<16} {'Semester Average':<16} {'Letter Grade':<10}")
print("-" * 76)
for student in students:
    running_avg = f"{student.RunningAverage():.2f}" if student.RunningAverage() else ""
    semester_avg = f"{student.TotalAverage():.2f}" if student.TotalAverage() else ""
    letter_grade = student.LetterGrade()
    print(f"{student.FirstName:<12} {student.LastName:<12} {student.TNumber:<12} {running_avg:<16} {semester_avg:<16} {letter_grade:<10}")
