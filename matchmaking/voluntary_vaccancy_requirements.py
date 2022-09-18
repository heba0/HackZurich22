class VoluntaryVaccancyRequirements:
    def __init__(self, name: str = '', hours: str = '', due_date: str = '', skills: str = '', duration: str = ''):
        self.name = name
        self.hours = hours
        self.due_date = due_date
        self.skills = skills
        self.duration = duration

    @staticmethod
    def read_from_dict(list_of_objs):
        return [VoluntaryVaccancyRequirements(**{k: elem.get(k, '') for k in elem.keys()}) for elem in list_of_objs]
