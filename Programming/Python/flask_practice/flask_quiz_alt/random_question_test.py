import json
import random

def random_question_specific_category():
    with open('questions.json') as fp:
        data = json.load(fp)
        questions = data["questions"]

        questions_list = []
        number_of_questions = 2
        for question in questions:
            if question['category'] == 'General Knowledge':
                questions_list.append(question)

        if len(questions_list)  < number_of_questions:
            number_of_questions = len(questions_list)

        # print(number_of_questions)
        # print(questions_list)
        return random.sample(questions_list, k=number_of_questions)

def random_question():
    with open('questions.json') as fp:
        data = json.load(fp)
        questions = data["questions"]
        return random.sample(questions, k=2)

# print(random_question())

random_questions = random_question_specific_category()
for quesion in random_questions:
    print(quesion)