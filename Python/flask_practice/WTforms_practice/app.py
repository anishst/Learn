# https://stackoverflow.com/questions/46653424/flask-wtforms-fieldlist-with-booleanfield

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import BooleanField, FieldList, SubmitField, RadioField, SelectMultipleField, widgets

app = Flask(__name__)
app.config['SECRET_KEY']='asdfjlkghdsf'

filenames = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
questions = ["1. The answer to question one is False.", "tet", "test3"]



# class FileListFormBase(FlaskForm):
#     submit = SubmitField('Submit')
#
# def file_list_form_builder(filenames):
#     class FileListForm(FileListFormBase):
#         pass
#
#     for (i, filename) in enumerate(filenames):
#         setattr(FileListForm, 'filename_%d' % i, BooleanField(label=filename))
#
#     return FileListForm()

def select_form_builder(questions):
    class FileListForm(FlaskForm):
        pass

    counter = 0
    for question in questions:
        print(question)
        setattr(FileListForm, 'filename_%d' % counter, SelectMultipleField(
                "3. The correct answer is 1, 2 and 3.",
                choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four')],

                # changes the choices into checkboxes instead of a dropdown list
                option_widget=widgets.CheckboxInput(),

                # puts the checkboxes in front of the label
                widget=widgets.ListWidget(prefix_label=False)
                ))
        counter = counter +1

    setattr(FileListForm, 'submit', SubmitField('Submit'))
    return FileListForm()

def radio_form_builder(questions):
    class FileListForm(FlaskForm):
        pass

    counter = 0
    for question in questions:
        print(question)
        setattr(FileListForm, 'filename_%d' % counter, RadioField(label=question,
        choices=[('True', 'True'), ('False', 'False')]

        ))
        counter = counter +1

    setattr(FileListForm, 'submit', SubmitField('Submit'))
    return FileListForm()

def file_list_form_builder(filenames):
    class FileListForm(FlaskForm):
        pass

    for (i, filename) in enumerate(filenames):
        setattr(FileListForm, 'filename_%d' % i, BooleanField(label=filename))

    setattr(FileListForm, 'submit', SubmitField('Submit'))
    return FileListForm()

@app.route('/')
def listfiles():
    form = file_list_form_builder(filenames)
    radio_form = radio_form_builder(questions)
    select_form = select_form_builder(questions)
    return render_template('index.html', form=form, form2=radio_form, form3=select_form)


if __name__ == '__main__':
    app.run(debug=True, port=5001)