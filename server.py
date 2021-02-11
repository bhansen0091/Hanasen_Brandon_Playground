from flask import Flask, render_template
app = Flask(__name__)

# @app.route("/")
# def index(num = 3):
#     return render_template("index.html", times = num)

# @app.route("/play/<int:num>")
# def play_x_times(num = 3):
#     return render_template("index.html", times = num)

@app.route("/")
@app.route("/play/<int:num>")
@app.route("/play/<int:num>/<string:color>")
def play_x_times(num = 3, color = 'blue'):
    return render_template("index.html", times = num, background_color = color)

if __name__=="__main__":
    app.run(debug=True)