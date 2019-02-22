from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author':'cory schafer',
        'title':'blog post 1',
        'content':'some content',
        'date_posted':'April 20, 2018'
    },
        {
        'author':'Jake Bamforth',
        'title':'blog post 2',
        'content':'some content',
        'date_posted':'April 24, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About The Canteen')

if __name__ == '__main__':
    app.run(debug=True)