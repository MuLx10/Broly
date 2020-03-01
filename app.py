import os
from flask import Flask, render_template, send_file, Response
from flask_bootstrap import Bootstrap
import shlex, subprocess

command_line = "python Broly.py"
args = shlex.split(command_line)
p = subprocess.Popen(args)

app = Flask(__name__)
bootstrap = Bootstrap(app)

lines = ['Workflow', 'Productivity', 'Social']


@app.route('/')
def index():
    global lines
    lines = lines[:20]
    return render_template('index.html', lines=lines)
    

if __name__ == "__main__":
    app.run(debug=True, port = os.getenv('PORT'))