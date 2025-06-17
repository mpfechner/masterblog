from flask import Flask, request, redirect, url_for, render_template
import json


app = Flask(__name__)


def load_posts():
    with open('blog_posts.json', 'r') as f:
        return json.load(f)


@app.route('/')
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)


@app.route('/add', methods=['GET'])
def add_form():
    return render_template('add.html')


@app.route('/add', methods=['POST'])
def add_post():
    author = request.form.get('author')
    title = request.form.get('title')
    content = request.form.get('content')

    posts = load_posts()
    new_id = max((post['id'] for post in posts), default=0) + 1

    posts.append({
        'id': new_id,
        'author': author,
        'title': title,
        'content': content
    })

    with open('blog_posts.json', 'w') as f:
        json.dump(posts, f, indent=4)

    return redirect(url_for('index'))





if __name__ == '__main__':
    app.run(debug=True, port=5000)
