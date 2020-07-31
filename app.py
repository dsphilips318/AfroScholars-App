# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import feedback

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/languages')
def languages():
    return render_template('languages.html')


@app.route('/yoruba-demo')
def yoruba_demo():
    return render_template('yoruba-demo.html')


@app.route('/sign-up')
def sign_up():
    return render_template('sign-up.html')


@app.route('/log-in')
def log_in():
    return render_template('log-in.html')

# --- Lesson 1 ---


@app.route('/yoruba/lesson1/questions')
def lesson1_question1():
    return render_template('yoruba-lesson1_copy/questions.html')


@app.route('/yoruba/lesson1/question2')
def lesson1_question2():
    return render_template('yoruba-lesson1/q2.html')


@app.route('/yoruba/lesson1/question3')
def lesson1_question3():
    return render_template('yoruba-lesson1/q3.html')


@app.route('/yoruba/lesson1/question4')
def lesson1_question4():
    return render_template('yoruba-lesson1/q4.html')


@app.route('/yoruba/lesson1/question5')
def lesson1_question5():
    return render_template('yoruba-lesson1/q5.html')


@app.route('/yoruba/lesson1/question6')
def lesson1_question6():
    return render_template('yoruba-lesson1/q6.html')


@app.route('/yoruba/lesson1/question7')
def lesson1_question7():
    return render_template('yoruba-lesson1/q7.html')


@app.route('/yoruba/lesson1/question8')
def lesson1_question8():
    return render_template('yoruba-lesson1/q8.html')


@app.route('/yoruba/lesson1/question9')
def lesson1_question9():
    return render_template('yoruba-lesson1/q9.html')


@app.route('/yoruba/lesson1/question10')
def lesson1_question10():
    return render_template('yoruba-lesson1/q10.html')


@app.route('/yoruba/lesson1/results', methods=['GET', 'POST'])
def lesson1_results():
    if request.method == 'POST':
        answer1 = request.form['answer_1']
        answer2 = request.form['answer_2']
        answer3 = request.form['answer_3']
        answer4 = request.form['answer_4']
        answer5 = request.form['answer_5']
        answer6 = request.form['answer_6']
        answer7 = request.form['answer_7']
        answer8 = request.form['answer_8']
        answer9 = request.form['answer_9']
        answer10 = request.form['answer_10']
        responses = {
            'answer1': answer1,
            'answer2': answer2,
            'answer3': answer3,
            'answer4': answer4,
            'answer5': answer5,
            'answer6': answer6,
            'answer7': answer7,
            'answer8': answer8,
            'answer9': answer9,
            'answer10': answer10
        }
        results = feedback(responses)
        percentage = results.get('percentage')
        message = results.get('message')
    return render_template('yoruba-lesson1_copy/results.html', percentage=percentage, message=message)

# Lesson 2


@app.route('/yoruba/lesson2/question1')
def lesson2_question1():
    return render_template('yoruba-lesson2/q1.html')


@app.route('/yoruba/lesson2/question2')
def lesson2_question2():
    return render_template('yoruba-lesson2/q2.html')


@app.route('/yoruba/lesson2/question3')
def lesson2_question3():
    return render_template('yoruba-lesson2/q3.html')


@app.route('/yoruba/lesson2/question4')
def lesson2_question4():
    return render_template('yoruba-lesson2/q4.html')


@app.route('/yoruba/lesson2/question5')
def lesson2_question5():
    return render_template('yoruba-lesson2/q5.html')


@app.route('/yoruba/lesson2/question6')
def lesson2_question6():
    return render_template('yoruba-lesson2/q6.html')


@app.route('/yoruba/lesson2/question7')
def lesson2_question7():
    return render_template('yoruba-lesson2/q7.html')


@app.route('/yoruba/lesson2/question8')
def lesson2_question8():
    return render_template('yoruba-lesson2/q8.html')


@app.route('/yoruba/lesson2/question9')
def lesson2_question9():
    return render_template('yoruba-lesson2/q9.html')


@app.route('/yoruba/lesson2/question10')
def lesson2_question10():
    return render_template('yoruba-lesson2/q10.html')


@app.route('/yoruba/lesson2/results')
def lesson2_results():
    return render_template('yoruba-lesson2/results.html')
