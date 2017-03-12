from flask import Flask
from flask import render_template
from random import randint

app = Flask('myApp')

@app.route('/')
def hello():
    return '<style> h1 { color: red; text-align: center; } </style> <h1>Hello World</h1>'

# app.run()

# '@app.route()' = a decorator
# a decorator (lines 7-9) !== a function

@app.route('/<name>')
def hello_someone(name):
    adjective = ['fantastic', 'awesome', 'amazing']
    randAdj = randint(0, len(adjective)-1)

    exaggerate = ['pretty', 'freaking', 'totally']
    randEx = randint(0, len(exaggerate)-1)

    return '<h1>Hello {0}, you are {1} {2}!</h1>'.format(name.title(), exaggerate[randEx], adjective[randAdj])

### use 'render_template' (imported on line 2)
# @app.route('/<name>')
# def hi_there(name):
#     return render_template('hello.html', name=name.title())
### Look into further >> need to set up an hello.html file to call on?

# Set up Python for 'contact.html'
# URL extension & sign up function
@app.route('/signup', methods=['POST'])
def sign_up():
    form_data = request.form
    print form_data['name']
    print form_data['email']
    return 'All OK'
### Need to link the 'contact.html' file

# insert 'debug=True' within 'app.run()' to avoid having to stop/rerunning the Python through the terminal
app.run(
    debug=True
)

# {% ... %} used within the examples in the session notes pdf >> Jinja (a templating language for Python) (like Liquid, Django, etc(?))
