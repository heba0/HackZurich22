class LinkedinExperienceEntry:
    def __init__(self, title='', employment_type='', company_name='', start_date=None, end_date=None):
        self.title: str = title
        self.employment_type: str = employment_type
        self.company_name: str = company_name
        self.start_date: Union[None, str] = start_date
        self.end_date: Union[None, str] = end_date

    def return_description(self):
        return self.title + self.employment_type + self.company_name
