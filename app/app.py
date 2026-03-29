from flask import Flask, render_template, request
import sqlite3
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

DB_PATH = os.path.join(BASE_DIR, "feedback.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS feedback (name TEXT, message TEXT)')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO feedback VALUES (?, ?)", (name, message))
        conn.commit()
        conn.close()

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM feedback")
    data = c.fetchall()
    conn.close()

    return render_template('index.html', feedback=data)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
