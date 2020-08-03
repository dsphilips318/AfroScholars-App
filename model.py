answers_1 = {
    'answer1': 'Ookan',
    'answer2': 'Eeji',
    'answer3': 'Eeta',
    'answer4': 'Eerin',
    'answer5': 'Aarun',
    'answer6': 'One',
    'answer7': 'Two',
    'answer8': 'Three',
    'answer9': 'Four',
    'answer10': 'Five'
}

answers_2 = {
    'answer1': 'Eefa',
    'answer2': 'Eeje',
    'answer3': 'Eejo',
    'answer4': 'Eesan',
    'answer5': 'Eewa',
    'answer6': 'Ten',
    'answer7': 'Seven',
    'answer8': 'Six',
    'answer9': 'Nine',
    'answer10': 'Eight'
}


def getGrade1(props):
    answers_right = 0
    for answer in props:
        if props[answer] == answers_1[answer]:
            answers_right += 1
    return answers_right


def getGrade2(props):
    answers_right = 0
    for answer in props:
        if props[answer] == answers_2[answer]:
            answers_right += 1
    return answers_right


feedback_message1 = {
    'percentage': '',
    'message': ''
}

feedback_message2 = {
    'percentage': '',
    'message': ''
}


def feedback1(props):
    questions_right = getGrade1(props)
    # percent = f'{str(questions_right*10)}%'
    percent = str(questions_right*10) + '%'
    feedback_message1.update({'percentage': percent})
    if questions_right >= 8:
        feedback_message1.update({'message': f'Wow! You scored a {percent}. Great Job! Come back again soon for more practice.'})
    if questions_right >= 6 and questions_right <= 7:
        feedback_message1.update({'message': f'You scored a {percent}. Not bad. Practice this lesson more and you can get an even better score.'})
    if questions_right < 6:
        feedback_message1.update({'message': f'Unfortunately, you scored a {percent}. Don\'t worry. Practice this lesson again and again and you can get an even better score.'})
    return feedback_message1


def feedback2(props):
    questions_right = getGrade2(props)
    # percent = f'{str(questions_right*10)}%'
    percent = str(questions_right*10) + '%'
    feedback_message2.update({'percentage': percent})
    if questions_right >= 8:
        feedback_message2.update({'message': f'Wow! You scored a {percent}. Great Job! Come back again soon for more practice.'})
    if questions_right >= 6 and questions_right <= 7:
        feedback_message2.update({'message': f'You scored a {percent}. Not bad. Practice this lesson more and you can get an even better score.'})
    if questions_right < 6:
        feedback_message2.update({'message': f'Unfortunately, you scored a {percent}. Don\'t worry. Practice this lesson again and again and you can get an even better score.'})
    return feedback_message2
