# Masterblog 📝

A simple but functional Flask-based blog application with full CRUD support – plus a Like feature! Built as part of a Masterschool project.

## 🔧 Features

- 🏠 Display all blog posts  
- ➕ Add new posts  
- ✏️ Update existing posts  
- 🗑️ Delete posts  
- ❤️ Like posts (with counter)  
- 📦 Data stored in `blog_posts.json`  
- 🎨 Templating with Jinja2 and custom CSS

## 🗂️ Project Structure

```
masterblog/
├── app.py
├── blog_posts.json
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   ├── add.html
│   └── update.html
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/masterblog.git
cd masterblog
```

### 2. Create virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Run the app

```bash
python app.py
```

App will be available at: [http://localhost:5000](http://localhost:5000)

## 📄 Notes

- Make sure `blog_posts.json` is present and writable.
- Uses `port=5000` as required by Codio – do not change it!
- Feel free to customize templates and styles to make it your own.

## 🤓 Author

Michael Fechner – with technical guidance by ChatGPT aka *Botti the Dev-Sidekick*

## 🏁 Next Steps (optional ideas)

- ✅ Pagination or reverse sort  
- ✅ Sticky Add button  
- ✅ Markdown support  
- ✅ Basic authentication  
- ✅ Save to SQLite instead of JSON

## 🧠 License

This project is for educational purposes – feel free to fork and improve!
