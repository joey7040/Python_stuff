from flask import Flask, render_template


app =  Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return "<h1>Joey Rivera is a incredible software engineer!</h1>"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/forgotpassword')
def forgot_password():
    return render_template('forgot_password.html')


@app.route('/usertable')
def tables():
    return render_template('usertable.html')

@app.route('/credituniontable')
def creditunion():
    return render_template('credituniontable.html')

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/404')
def fourohfour():
    return render_template('404.html')


if __name__ == "__main__":
    print("Server is running on port 5000")
    app.run(debug=True)