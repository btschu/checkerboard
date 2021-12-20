from flask import Flask, render_template

app = Flask(__name__)

# 8x8 checkerboard
@app.route('/')
def index():
    return render_template("index.html", num1 = 8, num2 = 8)

# 8x4 checkerboard
@app.route('/4')
def changeSize():
    return render_template("index.html", num1 = 4, num2 = 8)

# specify the size of the checkerboard
@app.route('/<int:num1>/<int:num2>')
def specifySize(num1, num2):
    return render_template('index.html', num1 = num1, num2 = num2)

# specify size and color of checkerboard
@app.route('/<int:num1>/<int:num2>/<color1>/<color2>')
def specifySizeColor(num1, num2, color1, color2):
    return render_template('index.html', num1 = num1, num2 = num2, color1 = color1, color2 = color2 )

# no page found
@app.errorhandler(404)
def pageNotFound(missing):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)
