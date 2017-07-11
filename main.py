from flask import Flask, url_for, redirect, render_template
import data_manager


app = Flask(__name__)


@app.route("/")
@app.route("/list")
def get_story_list():
    stories = data_manager.open_file("stories.csv")
    return render_template("list.html", stories=stories)


@app.route("/story")
@app.route("/story/<story_id>")
def get_story(story_id=None):
    if story_id:
        stories = data_manager.open_file("stories.csv")
        for story in stories:
            if str(story_id) in story:
                return render_template("form.html", story_id=story_id, story=story)
    return render_template("form.html")


if __name__ == "__main__":
    main(debug=True)
