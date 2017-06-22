from flask import Flask, request, redirect, render_template
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET' , 'POST'])
def signupForm():
    username = request.form['username']
    password = request.form['password']
    verifyPassword = request.form['verifyPassword']
    email = request.form['email']

    usernameError = ''
    passwordError = ''
    passwordError2 = ''
    verifyError = ''
    verifyError2 = ''
    emailError = ''
# USERNAME REQUIREMENTS
    if len(username) <3 or len(username) > 10:
        usernameError = "Username must be 3 to 10 characters"
        username = ''
    elif ' ' in username or '   ' in username:
        usernameError = 'Username cannot contain spaces.'

    if not password:
        passwordError = 'Please enter a password.'
    elif len(password) <3 or len(password) >20:
        passwordError = 'Passwords must be between 3 and 20 characters in length.'
    elif ' ' in password or '   ' in password:
        passwordError = 'Passwords cannot contain spaces.'

# PASSWORD ERROR - DO THE PASSWORDS MATCH
    if password != verifyPassword:
        passwordError = "Passwords do not match"
        password = ''
    else:
        password = password

# PASSWORD VERIFICATION
    if verifyPassword != password:
        verifyError = "Passwords do not match"
        password = ''
        verifyPassword = ''
    else:
        password = password
        verifyPassword = verifyPassword

# EMAIL VERIFICATION
    if email.count('@') == 1 and email.count('.') == 1 and email.count(' ') ==0:
        email = email
    else:
        emailError = 'You have entered an invalid email'
        email = ''

# RETURN CONTENT
    if not usernameError and not passwordError and not verifyError and not emailError:
        return redirect('/welcomePage?username={}'.format(username))
    else:
        return render_template('index.html', 
        username = username,
        usernameError = usernameError,
        password = password,
        passwordError = passwordError,
        verifyPassword = verifyPassword,
        verifyError = verifyError,
        email = email,
        emailError = emailError
        )

@app.route('/welcomePage', methods=['POST' , 'GET'])
def validate():
    username = request.args.get('username')
    return render_template('welcomePage.html', userNAME = username )

app.run()