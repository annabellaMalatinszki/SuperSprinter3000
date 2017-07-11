from flask import Flask, url_for, redirect, render_template
import data_manager


app = Flask(__name__)


@app.route("/")
@app.route("/list")
def get_story_list():
    return render_template("list.html")


@app.route("/story")
@app.route("/story/<story_id>")
def get_story():
    return render_template("form.html")


if __name__ == "__main__":
    main(debug=True)
