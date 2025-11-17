from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/planner")
def planner():
    return render_template("planner.html")

@app.route("/meals")
def meals():
    return render_template("meals.html")

@app.route("/outfits")
def outfits():
    return render_template("outfits.html")

@app.route("/calmhub")
def calmhub():
    return render_template("calmhub.html")

if __name__ == "__main__":
    app.run(debug=True)