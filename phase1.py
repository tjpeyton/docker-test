from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import os
import subprocess
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    program = TextField('Enter Program:', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)


    print(form.errors)
    if request.method == 'POST':
        program = request.form['program']
        print(program)
        p = subprocess.run(['docker', 'run', program], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.decode('utf-8')

        if form.validate():
            # Save the comment here.
            flash('Command: docker run ' + program)
            flash('Terminal Output: ' + p)
        else:
            flash('Please enter a program to run.  ')

    return render_template('home.html', form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
