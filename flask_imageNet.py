# -*- coding: utf-8 -*-
from flask import Flask, request, render_template

from image_classify.classify_api import classify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')#渲染主html。flask可以通过render_template，直接把同目录的templates文件里的html文件渲染出来


@app.route('/classify', methods=['POST'])
def cls():
    if request.files.get('file'):
        file = request.files.get('file')
        data = file.read()
        results = classify(data)
        # return jsonify({'res': classify(data)})
        return render_template('result.html', **locals())
    else:
        return index()


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)