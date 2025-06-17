from flask import Flask, render_template, request
import json


app = Flask(__name__)


def load_posts():
    with open('blog_posts.json', 'r') as f:
        return json.load(f)



def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
