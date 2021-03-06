from flask import Flask, render_template
import base64, os

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
def home():
    return render_template('home.html')

@app.route("/projects/")
def projects():
    return render_template('projects.html', title='Projects')

@app.route("/resume/", methods=["GET"])
def get_test_file():
    return render_template('resume.html', title='Resume')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)