import urllib.request, json
with urllib.request.urlopen("https://opentdb.com/api.php?amount=5&category=23") as url:
    data = json.loads(url.read().decode())
    print(data)
    print(len(data['results']))


    for item in data['results']:
        print(item['question'])
        print(item['correct_answer'])
        print(item['incorrect_answers'])
        print(item['type'])
        # answers = []
        # answers.append(item['correct_answer'])
        # [answers.append(item) for item in item['incorrect_answers']]

        #  format for WTF form fields - [ ['choice_value',choice_label']]
        answers = []
        answers.append([item['correct_answer'],item['correct_answer']])
        [answers.append([item,item]) for item in item['incorrect_answers']]

        import random
        random.shuffle(answers)
        print(answers)