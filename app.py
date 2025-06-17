from flask import Flask, request, redirect, url_for, render_template
import json
from typing import List, Dict, Optional

app = Flask(__name__)


def load_posts() -> List[Dict]:
    """Load blog posts from the JSON file."""
    with open('blog_posts.json', 'r') as f:
        return json.load(f)


def save_posts(posts: List[Dict]) -> None:
    """Save blog posts to the JSON file."""
    with open('blog_posts.json', 'w') as f:
        json.dump(posts, f, indent=4)


@app.route('/')
def index():
    """Display all blog posts."""
    posts = load_posts()
    return render_template('index.html', posts=posts)


@app.route('/add', methods=['GET'])
def add_form():
    """Render form to create a new blog post."""
    return render_template('add.html')


@app.route('/add', methods=['POST'])
def add_post():
    """Handle form submission and add a new blog post."""
    author = request.form.get('author')
    title = request.form.get('title')
    content = request.form.get('content')

    posts = load_posts()
    new_id = max((post['id'] for post in posts), default=0) + 1

    posts.append({
        'id': new_id,
        'author': author,
        'title': title,
        'content': content,
        'likes': 0
    })

    save_posts(posts)
    return redirect(url_for('index'))


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id: int):
    """Delete the blog post with the given ID."""
    posts = load_posts()
    updated_posts = [post for post in posts if post['id'] != post_id]
    save_posts(updated_posts)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET'])
def update_form(post_id: int):
    """Render the update form for a specific post."""
    posts = load_posts()
    post = next((p for p in posts if p['id'] == post_id), None)

    if not post:
        return "Post not found", 404

    return render_template('update.html', post=post)


@app.route('/update/<int:post_id>', methods=['POST'])
def update_post(post_id: int):
    """Handle submission of the update form."""
    posts = load_posts()
    post = next((p for p in posts if p['id'] == post_id), None)

    if not post:
        return "Post not found", 404

    post['author'] = request.form.get('author')
    post['title'] = request.form.get('title')
    post['content'] = request.form.get('content')

    save_posts(posts)
    return redirect(url_for('index'))


@app.route('/like/<int:post_id>', methods=['POST'])
def like_post(post_id: int):
    """Increment the like counter for a blog post."""
    posts = load_posts()
    post = next((p for p in posts if p['id'] == post_id), None)

    if not post:
        return "Post not found", 404

    post['likes'] = post.get('likes', 0) + 1
    save_posts(posts)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
