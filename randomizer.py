from collections import defaultdict
import random
import uuid

test_file = '/home/garrett/soctest.txt'
answers_file = './example_answers.txt'
output_test_prefix = './output_test_'
output_answers_prefix = './output_answers_'

def randomize(mcq_file, answers_file, random_questions=True,random_answers=True):
    letter_list = ['a','b','c','d','e','f']

    with open(mcq_file, 'r') as test:
        test_dict = test_to_dict(test)
 #       for key, value in test_dict.items():
 #           print(key, test_dict[key]['question'])
 #           print("--------------")

    with open(answers_file, 'r') as answers:
        answers_dict = answers_to_dict(answers)

    answer_list = list(answers_dict)
    current_question = 1

    unique_id = uuid.uuid4().hex
    output_test_file = open(output_test_prefix + unique_id, 'w')
    output_answer_file = open(output_answers_prefix + unique_id, 'w')


    while len(answer_list):
        random_question = random.choice(answer_list)
        answer_list.remove(random_question)

        line = str(current_question) + '.  ' \
                        + test_dict[random_question]['question']+'\n'

        output_test_file.write(str(line))

        choice_dict = test_dict[random_question]
        del choice_dict['question']
        choice_list = list(choice_dict)

        print(choice_list)

        current_choice = 0

        while len(choice_list):
            new_answer = None

            random_choice = random.choice(choice_list)

            if answers_dict[random_question] == random_choice:
                new_answer = letter_list[current_choice]
                output_answer_file.write(
                    str(current_question) + ".  " + new_answer + '\n')

            choice_list.remove(random_choice)

            choice_line = '\t' + letter_list[current_choice] +'.  ' \
                            + choice_dict[random_choice]+'\n'
            output_test_file.write(str(choice_line))

            current_choice += 1

        output_test_file.write('\n')
        current_question += 1

    output_test_file.close()
    output_answer_file.close()

def test_to_dict(test):
    letters = {'a', 'b', 'c', 'd', 'e', 'f'}
    test_dict = defaultdict(lambda : dict())
    last_number = None

    for line in test:
        index = line.split('.')[0].strip()
        value = line.split('.', 1)[-1].strip()

        if index.isdigit():
            test_dict[index]['question'] = value
            last_number = index

        if index.lower() in letters and last_number:
            test_dict[last_number][index.lower()] = value

    return test_dict

def answers_to_dict(answers):
    answers_dict = dict()

    for line in answers:
        index = line.split('.')[0].strip()
        value = line.split('.')[1].strip()
        answers_dict[index] = value
    return answers_dict

randomize(test_file, answers_file)
