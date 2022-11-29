class Candidate:
    def __init__(self, id_, name, picture, position, gender, age, skills):
        self.id_ = id_
        self.name = name
        self.picture = picture
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills.lower().split(', ')

    def get_id(self):
        return self.id_

    def get_name(self):
        return self.name

    def get_skills(self):
        return self.skills

    def get_picture(self):
        return self.picture

    def get_position(self):
        return self.position

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def __repr__(self):
        return f"Candidate(id_='{self.id_}', name='{self.name}', picture='{self.picture}', position='{self.position}', " \
               f"gender='{self.gender}', age='{self.age}', skills='{self.skills}')"
