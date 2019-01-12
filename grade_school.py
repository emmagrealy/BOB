class School(object):

    school_name = ""
    members_in_grade = {}

    def __init__(self, school_name, grades=range(1,10)):
        self.school_name = school_name
        self.members_in_grade = {key: set() for key in grades}

    def grade(self, grade):
        return self.members_in_grade[grade]

    def add(self, student_to_add, grade):
        self.members_in_grade[grade].add(student_to_add)

    def sort(self):
        return [(k, tuple(sorted(v))) for k, v in self.members_in_grade.items() if v ]