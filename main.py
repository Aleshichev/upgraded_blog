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


@app.route('/post<int:n>')
def goto(n):
    cur_page = None
    num_image = ''
    for item in all_posts:
        if item['id'] == n:
            cur_page = item
            num_image = str(item['id'])
            return render_template('post.html', post=cur_page, image=num_image)


if __name__ == "__main__":
    app.run(debug=True)