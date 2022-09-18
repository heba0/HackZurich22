from typing import List
from matchmaking.linkedin_education_entry import LinkedinEducationEntry
from matchmaking.linkedin_experience_entry import LinkedinExperienceEntry


class LinkedinProfile:
    def __init__(self, education=None, experience=None):
        if education is None:
            education = []
        if experience is None:
            experience = []
        self.education: List[LinkedinEducationEntry] = education
        self.experience: List[LinkedinExperienceEntry] = experience

    @staticmethod
    def read_from_dict(obj):
        linkedin_profile = LinkedinProfile()
        linkedin_profile.education = [
            LinkedinEducationEntry(**{k: elem.get(k, '') for k in elem.keys()}) for elem in obj['education']]

        linkedin_profile.experience = [
            LinkedinExperienceEntry(**{k: elem.get(k, '') for k in elem.keys()}) for elem in obj['experience']]
        return linkedin_profile

    def return_description(self):
        description = ''
        for education_entry in self.education:
            description += education_entry.return_description()
        for experience_entry in self.experience:
            description += experience_entry.return_description()
        return description
