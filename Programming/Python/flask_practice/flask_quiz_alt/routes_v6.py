# https://github.com/mjhea0/thinkful-mentor/tree/master/python/flask-wtf-quiz
# https://opentdb.com/api_config.php
# 1/18/20 working added reading from internet - WORKING

# TODO : Create landing page with  url build; use number of qeustions, category and difficult value to build custom quizes

# <select name="trivia_category" class="form-control">
# 			<option value="any">Any Category</option>
# 			<option value="9">General Knowledge</option><option value="10">Entertainment: Books</option><option value="11">Entertainment: Film</option><option value="12">Entertainment: Music</option><option value="13">Entertainment: Musicals &amp; Theatres</option><option value="14">Entertainment: Television</option><option value="15">Entertainment: Video Games</option><option value="16">Entertainment: Board Games</option><option value="17">Science &amp; Nature</option><option value="18">Science: Computers</option><option value="19">Science: Mathematics</option><option value="20">Mythology</option><option value="21">Sports</option><option value="22">Geography</option><option value="23">History</option><option value="24">Politics</option><option value="25">Art</option><option value="26">Celebrities</option><option value="27">Animals</option><option value="28">Vehicles</option><option value="29">Entertainment: Comics</option><option value="30">Science: Gadgets</option><option value="31">Entertainment: Japanese Anime &amp; Manga</option><option value="32">Entertainment: Cartoon &amp; Animations</option>		</select>
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, SelectMultipleField, SelectField, widgets, StringField, FieldList, FormField
from wtforms.validators import DataRequired, ValidationError
from random import randrange, sample

def random_question():
    import urllib.request, json
    with urllib.request.urlopen("https://opentdb.com/api.php?amount=5&category=18") as url:
        data = json.loads(url.read().decode())
        print(data['results'])
        return data['results']


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
        # print(question)
        print(question['question'])
        print(question['correct_answer'])
        # print(question['incorrect_answers'])
        # print(question['type'])

        #  make answers fit format for WTF choices fields - [ ['choice_value',choice_label']]
        # WTF validators = ['value','value','...']
        answers = []
        answers.append([question['correct_answer'],question['correct_answer']])
        correct_answer = question['correct_answer']
        [answers.append([question,question]) for question in question['incorrect_answers']]

        # shuffle choices list
        import random
        random.shuffle(answers)

        if question['type'] == 'boolean' or question['type'] == 'multiple':

            setattr(PopQuiz, 'question_%d' % counter,
                (RadioField(
                question['question'],
                choices=answers,
                validators=[CorrectAnswer(correct_answer)]
            )
            ))
        else:
            setattr(PopQuiz,  'question_%d' % counter,SelectMultipleField(
                question['question'],
                choices=answers,
                validators=[CorrectAnswer([correct_answer])],

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