from flask import Flask, render_template, request
import requests

app = Flask(__name__)
response = requests.get("https://api.npoint.io/e9a89bf4721efb55088d").json()


@app.route('/')
def home():
    return render_template("index.html", posts=response)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/<int:post_id>")
def get_post(post_id):
    requested_post = None
    for post in response:
        if post["id"] == post_id:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
