from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ap')
def ap():
    return render_template('ap.html')

@app.route('/acs')
def acs():
    return render_template('adv.html')

@app.route('/de')
def de():
    return render_template('de.html')

@app.route('/fun')
def fun():
    return render_template('fun.html')

@app.route('/web')
def web():
    return render_template('web.html')

@app.route('/is')
def ind():
    return render_template('is.html')

if __name__ == '__main__':
    app.run(debug=True)