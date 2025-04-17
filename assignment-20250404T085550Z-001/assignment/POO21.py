class Students:
    #Attributes:
    #Constructor:
    def __init__(self, id, student_name, semester, course_name):
        self.id=id
        self.student_name=student_name
        self.semester=semester
        self.course_name=course_name
    #Methods:
    def create(self):
        for dem2 in range(1, len(self.student_name) + 1):
            print(f"Tên học sinh {dem2}: {self.student_name}\n\t"
                  f"- id: {self.id}\n\t- Kỳ học: {self.semester}\n\t"
                  f"- Tên khóa học: {self.course_name}")
    def find_and_sort(self):
        print(self.student_name.split())