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
  

# Second time solution

# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/')
# def index():
#     context = {
#         "num" : 3,
#         "color1" : "black",
#         "color2" : "red"
#     }
#     return render_template("index.html", **context)

# @app.route('/<int:num1>/<int:num2>')
# def num_of_boxes(num1, num2):
#     context = {
#         "num1" : int(num1/2),
#         "num2" : int(num2/2),
#         "color1" : "black",
#         "color2" : "red"
#     }
#     return render_template("index.html", **context)

# @app.route('/<int:num1>/<int:num2>/<string:color1>/<string:color2>')
# def num_of_boxes_define_color(num1, num2, color1, color2):
#     context = {
#         "num1" : int(num1/2),
#         "num2" : int(num2/2),
#         "color1" : color1,
#         "color2" : color2
#     }
#     return render_template("index.html", **context)

# if __name__=="__main__":
#     app.run(debug=True)
