from flask import Flask, render_template
import requests

data_api = 'https://api.npoint.io/51ed2c42d3aa45cb61a9'
all_posts = requests.get(data_api).json()      # список объектов


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("index.html", data_posts=all_posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def show_post(index):
    # requested_post = None
    for blog_post in all_posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)