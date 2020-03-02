import os
from flask import Flask, render_template, send_file, Response
from flask_bootstrap import Bootstrap
import shlex, subprocess


cron_process = subprocess.Popen(shlex.split("python Cron.py"))
chatbot_process = subprocess.Popen(shlex.split("python ChatBot.py"))

app = Flask(__name__)
bootstrap = Bootstrap(app)

lines = ['Workflow', 'Productivity', 'Social']


@app.route('/')
def index():
    global lines
    lines = lines[:20]
    return render_template('index.html', lines=lines)
    

if __name__ == "__main__":
    app.run(os.getenv('LISTEN_HOST', '0.0.0.0'), int(os.environ.get("PORT", 5000)))
