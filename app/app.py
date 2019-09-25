# -*- coding: utf-8 -*-
import json
import os
import sys

from flask import Flask, send_from_directory, render_template, request

app = Flask(__name__, static_url_path='')


@app.route('/')
def root():
    files = sorted(os.listdir(os.path.join(work_dir, 'audio')))
    return render_template('index.html', files=files)


@app.route('/annotate.html')
def annotate():
    name = request.args.get('audio', '')
    return render_template('annotate.html', name=name)


@app.route('/static/<path:path>')
def send_js(path):
    # default static_folder is `static`
    return app.send_static_file(path)


@app.route('/annotation/<path:path>', methods=['GET', 'POST'])
def annotation(path):
    if request.method == 'GET':
        return send_from_directory(os.path.join(work_dir, 'annotation'), path)
    else:
        data = request.data
        filename = path
        output_dir = os.path.join(work_dir, 'annotation')
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, filename), 'w') as f:
            data = data.decode('utf-8')
            data = json.loads(data)
            json.dump(data, f, indent=2)
        return 'ok'

@app.route('/audio/<path:path>')
def audio(path):
    return send_from_directory(os.path.join(work_dir, 'audio'), path)


if __name__ == "__main__":
    work_dir = os.path.realpath('../demo_dir')
    if len(sys.argv) > 1:
        work_dir = sys.argv[1]
        work_dir = os.path.realpath(work_dir)
    app.run(debug=True)
