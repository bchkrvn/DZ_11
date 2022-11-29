class Candidate:
    """
    Класс кандидатов
    """
    def __init__(self, id_, name, picture, position, gender, age, skills):
        self.id_ = id_
        self.name = name
        self.picture = picture
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills.lower().split(', ')

    def get_id(self):
        """
        Позволяет получить id кандидата
        :return: id
        """
        return self.id_

    def get_name(self):
        """
        Позволяет получить имя и фамилию кандидата
        :return: name and surname
        """
        return self.name

    def get_skills(self):
        """
        Позволяет получить список скиллов кандидата
        :return: list with skills
        """
        return self.skills

    def get_picture(self):
        """
        Позволяет получить ссылку на фото кандидата
        :return: url
        """
        return self.picture

    def get_position(self):
        """
        Позволяет получить должность кандидата
        :return: position
        """
        return self.position

    def get_gender(self):
        """
        Позволяет получить пол кандидата
        :return: gender
        """
        return self.gender

    def get_age(self):
        """
        Позволяет получить возраст кандидата
        :return: age
        """
        return self.age

    def __repr__(self):
        return f"Candidate(id_='{self.id_}', name='{self.name}', picture='{self.picture}', position='{self.position}', " \
               f"gender='{self.gender}', age='{self.age}', skills='{self.skills}')"
