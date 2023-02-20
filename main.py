import random
from data import data_questions
from questions import Question


def main():
    questions = []
    for quastion in data_questions:
        questions.append(Question(quastion["q"],
                                  int(quastion["d"]),
                                  quastion["a"]
                                  ))
    random.shuffle(questions)

    for quast in questions:
        print(quast.build_quastion())
        user_answer = input()
        quast.answer_user = user_answer

        if quast.is_correct():
            print(quast.build_positive_feedback())
        else:
            print(quast.build_negative_feedback())


    count_tru = 0
    count_ball = 0

    for corr in questions:
        if corr.is_correct():
            count_tru += 1
            count_ball += corr.get_points()

    print("Вот и всё!")
    print(f"Правильных ответов - {count_tru}/5")
    print(f"Очков получено {count_ball}")

main()