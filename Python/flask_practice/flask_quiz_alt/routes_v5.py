# https://github.com/mjhea0/thinkful-mentor/tree/master/python/flask-wtf-quiz
# 1/17/20 working added random feature
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, SelectMultipleField, SelectField, widgets, StringField, FieldList, FormField
from wtforms.validators import DataRequired, ValidationError
from random import randrange, sample

import json

def random_question():
    with open('questions.json') as fp:
        data = json.load(fp)
        questions = data["questions"]
        return sample(questions, k=3)

random_questions = random_question()
class CorrectAnswer(object):
    """
    Custom validator for WTForms to check
    if the correct answer was submitted
    """

    def __init__(self, answer):
        self.answer = answer

    def __call__(self, form, field):
        # List of error messages that are selected by random
        error_messages = ['Sorry, that\'s not the correct answer.',
                          'Try that again...',
                          'Incorrect answer.',
                          'Please check this answer...',
                          'Oops! Try again...',
                          'Nope! Sorry... try again!',
                          'No, not quite... try again!',
                          'Hmmm, not exactly right...']
        num = randrange(0, len(error_messages))
        message = error_messages[num]

        if field.data != self.answer:
            raise ValidationError(message)


def quiz(random_questions):
    class PopQuiz(FlaskForm):
        pass


    counter = 0
    for question in random_questions:
        print(question)
        print(question['answers'])
        if question['type'] == 'radio':
            setattr(PopQuiz, 'question_%d' % counter,
                (RadioField(
                question['question'],
                choices=[answer for answer in question["answers"]],
                validators=[CorrectAnswer(question['correct_answer'])]
            )
            ))
        else:
            setattr(PopQuiz,  'question_%d' % counter,SelectMultipleField(
                question['question'],
                choices=[answer for answer in question["answers"]],
                validators=[CorrectAnswer(question['correct_answer'])],

                # changes the choices into checkboxes instead of a dropdown list
                option_widget=widgets.CheckboxInput(),

                # puts the checkboxes in front of the label
                widget=widgets.ListWidget(prefix_label=False)
                ))
        counter = counter + 1


    setattr(PopQuiz, "submit", SubmitField('Submit'))

    return PopQuiz()

SECRET_KEY = 'this is a secret key'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET', 'POST'])
def wtf_quiz():

    form = quiz(random_questions)
    if form.validate_on_submit():
        print("Form submitted")
        return redirect(url_for('you_passed'))
    print("Form not sumbitted")
    return render_template('wtf_quiz.html', form=form)


@app.route('/you_passed')
def you_passed():
    return render_template('you_passed.html')


if __name__ == '__main__':
    app.run(debug=True)