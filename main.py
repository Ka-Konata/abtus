from flask import Flask, render_template
import icons as avatares

app = Flask(__name__)


@app.route("/icons")
def icons():
    avatares.actualize_icons()
    return avatares.get_icons()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/k")
def ka():
    return render_template("Ka.html")


@app.route("/k/friends")
def ka_friends():
    return render_template("Ka-friends.html")


@app.route("/d")
def dudu():
    return render_template("Dudu.html")


@app.route("/d/friends")
def dudu_friends():
    return render_template("Dudu-friends.html")


if __name__ == "__main__":
    app.run(debug=True)