from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, Yuvraj!'

# Additional routes
@app.route('/about')
def about():
    return 'This is the About Page.'

@app.route('/contact')
def contact():
    return 'Contact us at contact@example.com.'

@app.route('/services')
def services():
    return 'Our services include web development, consulting, and more.'



if __name__ == '__main__':
    app.run(debug=True)