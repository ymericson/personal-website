from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/projects/")
def projects():
    return render_template('projects.html', title='Projects')

@app.route("/projects/<proj_name>") 
def proj(proj_name): 
    return render_template('projects/%s.html' % proj_name)
    
if __name__ == '__main__':
    app.run(debug=True)
