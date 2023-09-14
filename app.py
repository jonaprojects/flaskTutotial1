from flask import Flask, render_template
from waitress import serve

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=5000)
    #app.run(host='0.0.0.0')
    # serve(app, host='0.0.0.0', port=5000)
    # serve(app, host='0.0.0.0', port=8081)
    