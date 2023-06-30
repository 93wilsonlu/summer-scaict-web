from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)


def check(s):
    blacklist = ['()', 'class', 'base', 'globals', 'init', 'import', 'os', 'system', 'read', '|', 'getitem', 'popen',
                 'flag.txt', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=', '+', ':', 'config', 'self', '%', '#']
    for b in blacklist:
        if b in s:
            return False

    return len(s) <= 70


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'name' in request.form and check(request.form['name']):
        return render_template_string('<h1>Hello ' + request.form['name'] + '</h1>')

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8303, debug=False)
