from flask import Flask, render_template, request
import requests
import smtplib
import os

data_api = 'https://api.npoint.io/51ed2c42d3aa45cb61a9'
all_posts = requests.get(data_api).json()      # список объектов
MY_EMAIL = os.environ.get('MYMY_EMAIL')
PASSWORD = os.environ.get('MY_PASSWORD')

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("index.html", data_posts=all_posts)

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/post<int:n>')
def goto(n):
    cur_page = None
    num_image = ''
    for item in all_posts:
        if item['id'] == n:
            cur_page = item
            num_image = str(item['id'])
            return render_template('post.html', post=cur_page, image=num_image)

@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["username"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)


def send_email(username, email, phone, message):
    email_message = f"Subject:New Messaga\n\nName: {username}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()       # защита письма
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=email_message)



if __name__ == "__main__":
    app.run(debug=True)