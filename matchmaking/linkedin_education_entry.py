class LinkedinEducationEntry:
    def __init__(self, school: str = '', degree: str = '', start_date: str = '', end_date: str = ''):
        self.school: str = school
        self.degree: str = degree
        self.start_date: str = start_date
        self.end_date: str = end_date

    def return_description(self):
        return self.school + self.degree
