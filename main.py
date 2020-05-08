# [START gae_python37_app]
from flask import Flask, render_template, request
from werkzeug.datastructures import ImmutableMultiDict

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('student.html')

def sum_upper(text):
    return sum(1 for c in text if c.isupper())

def sum_lower(text):
    return sum(1 for c in text if c.islower())


@app.route('/result', methods=['POST'])
def hello():
    """Return a friendly HTTP greeting."""

    if request.method == 'POST':
        result: ImmutableMultiDict = request.form
        data = dict(result.lists())
        sum_up = sum_upper(data['dane'][0])
        sum_low = sum_lower(data['dane'][0])
        results = {"Capital letters": sum_up, "Small letters": sum_low}

        return render_template("result.html", result=results)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
