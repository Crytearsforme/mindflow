from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/planner", methods=["GET", "POST"])
def planner():
    if request.method == "POST":
        task_text = request.form.get("task")
        if task_text:
            tasks.append(task_text)
        return redirect("/planner")

    stress_message = None
    stress_level = len(tasks)

    if stress_level >= 10:
        stress_message = ("high", "High stress detected schedule too heavy. Reduce tasks to avoid fatigue.")
    elif stress_level >= 8:
        stress_message = ("medium", "Today looks busy. Try spreading tasks out.")
    elif stress_level >= 5:
        stress_message = ("low", "Your schedule is getting full. Consider adding a break.")

    return render_template("planner.html", tasks=tasks, stress_message=stress_message)


@app.route("/clear_tasks", methods=["POST"])
def clear_tasks():
    tasks.clear()
    return redirect("/planner")

@app.route("/delete/<int:index>", methods=["POST"])
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect("/planner")

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