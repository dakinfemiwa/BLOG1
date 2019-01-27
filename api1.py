from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '6ad5ead913d7417f1dd906e63b42c41810e56db43d5b38ec1d08ae69d79f6112'

posts = [
    {
        'author': 'David Akinfemiwa',
        'title': 'The meaning of life',
        'content': 'La la al a',
        'date_posted': 'July 18 2018'
    },
    {
        'author': 'David Akinfemiwa',
        'title': 'Life pt2',
        'content': 'lasladsada',
        'date_posted': 'August 23 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', )

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admim@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True)