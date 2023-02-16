from data import data_questions

class Question:
    def __init__(self, text, hard_level, tru_answer):
        self.text = text
        self.hard_level = hard_level
        self.tru_answer = tru_answer

        self.is_answer = False
        self.answer_user = None
        self.points = int(hard_level) * 10

    def get_points(self):
        return self.points

    def is_correct(self):
        return self.answer_user == self.tru_answer

    def build_quastion(self):
        return f"\n{self.text} \nСложность {self.hard_level}/5"

    def build_positive_feedback(self):
        return f"Ответ верный, получено {self.points} баллов"

    def build_negative_feedback(self):
        return f"Ответ не верный. Верный ответ - {self.tru_answer}"

    def __repr__(self):
        return f"{self.text} - {self.hard_level} - {self.tru_answer}"