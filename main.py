from flask import Flask, url_for, redirect, render_template


app = Flask(__name__)


if __name__ == "__main__":
    main(debug=True)
