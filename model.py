answers = {
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

props_test = {
    'answer1': 'Ookan',
    'answer2': 'Eeji',
    'answer3': 'Eeta',
    'answer4': 'Eerin',
    'answer5': 'Aarun',
    'answer6': 'One',
    'answer7': 'Two',
    'answer8': 'Six',
    'answer9': 'Four',
    'answer10': 'Five'
}


def getGrade(props):
    answers_right = 0
    for answer in props:
        if props[answer] == answers[answer]:
            answers_right += 1
    return answers_right


feedback_message = {
    'percentage': '',
    'message': ''
}


def feedback(props):
    questions_right = getGrade(props)
    # percent = f'{str(questions_right*10)}%'
    percent = str(questions_right*10) + '%'
    feedback_message.update({'percentage': percent})
    if questions_right >= 8:
        feedback_message.update({'message': f'Wow! You scored a {percent}. Great Job! Come back again soon for more practice.'})
    if questions_right >= 6 and questions_right <= 7:
        feedback_message.update({'message': f'You scored a {percent}. Not bad. Practice this lesson more and you can get an even better score.'})
    if questions_right < 6:
        feedback_message.update({'message': f'Unfortunately, you scored a {percent}. Don\'t worry. Practice this lesson again and again and you can get an even better score.'})
    return feedback_message


print(feedback(props_test))