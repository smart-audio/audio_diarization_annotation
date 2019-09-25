# -*- coding: utf-8 -*-
import os
import sys

from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='')


@app.route('/')
def root():
    return send_from_directory('', 'index.html')


@app.route('/static/<path:path>')
def send_js(path):
    # default static_folder is `static`
    return app.send_static_file(path)


@app.route('/annotation/<path:path>')
def annotation(path):
    return send_from_directory(os.path.join(work_dir, 'annotation'), path)


@app.route('/audio/<path:path>')
def audio(path):
    return send_from_directory(os.path.join(work_dir, 'audio'), path)


if __name__ == "__main__":
    work_dir = os.path.realpath('../demo_dir')
    if len(sys.argv) > 1:
        work_dir = sys.argv[1]
        work_dir = os.path.realpath(work_dir)
    app.run(debug=True)
