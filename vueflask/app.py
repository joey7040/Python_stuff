from flask import Flask, render_template


app =  Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return "<h1>Joey Rivera is a incredible software engineer!</h1>"

if __name__ == "__main__":
    print("Server is running on port 5000")
    app.run(debug=True)