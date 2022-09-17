class Location:
    def __init__(self, city='', country='', street='', location_zip=''):
        self.city: str = city
        self.country: str = country
        self.street: str = street
        self.zip: str = location_zip
