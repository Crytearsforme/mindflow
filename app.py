from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []
meals = []
outfits = []

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

@app.route("/meals", methods=["GET", "POST"])
def meals_page():
    if request.method == "POST":
        meal_type = request.form.get("meal_type")
        meal_name = request.form.get("meal_name")

        if meal_type and meal_name:
            meals.append({"type": meal_type, "name": meal_name})

        return redirect("/meals")

    grouped = {
        "Breakfast": [],
        "Lunch": [],
        "Dinner": [],
        "Snack": []
    }

    for i, meal in enumerate(meals):
        grouped[meal["type"]].append({
            "index": i,
            "name": meal["name"]
        })

    return render_template("meals.html", meals_grouped=grouped)


@app.route("/delete_meal/<int:index>", methods=["POST"])
def delete_meal(index):
    if 0 <= index < len(meals):
        meals.pop(index)
    return redirect("/meals")


@app.route("/clear_meals", methods=["POST"])
def clear_meals():
    meals.clear()
    return redirect("/meals")

@app.route("/outfits", methods=["GET", "POST"])
def outfits_page():
    if request.method == "POST":
        outfit_type = request.form.get("outfit_type")
        outfit_name = request.form.get("outfit_name")

        if outfit_type and outfit_name:
            outfits.append({"type": outfit_type, "name": outfit_name})

        return redirect("/outfits")

    grouped = {
        "Top": [],
        "Bottom": [],
        "Full Outfit": [],
        "Accessory": []
    }

    for i, item in enumerate(outfits):
        grouped[item["type"]].append({
            "index": i,
            "name": item["name"]
        })

    return render_template("outfits.html", outfits_grouped=grouped)

@app.route("/delete_outfit/<int:index>", methods=["POST"])
def delete_outfit(index):
    if 0 <= index < len(outfits):
        outfits.pop(index)
    return redirect("/outfits")


@app.route("/clear_outfits", methods=["POST"])
def clear_outfits():
    outfits.clear()
    return redirect("/outfits")

@app.route("/calmhub")
def calmhub():
    videos = [
        {
            "title": "5-Minute Guided Breathing",
            "url": "https://youtu.be/TXNECaIJPDI?si=nNwORX8RE2jUF7e4"
        },
        {
            "title": "Relaxing Nature Sounds",
            "url": "https://www.youtube.com/embed/1ZYbU82GVz4"
        },
        {
            "title": "Quick Stress Relief Meditation",
            "url": "https://www.youtube.com/embed/ZToicYcHIOU"
        }
    ]

    tips = [
        "Take 5 slow breaths before starting a stressful task.",
        "Organize your clothes the night before to reduce morning decision fatigue.",
        "Use your meal planner to avoid last-minute food stress.",
        "Take a 2-minute stretch break every 45 minutes.",
        "Drink water — dehydration increases anxiety levels."
    ]

    return render_template("calmhub.html", videos=videos, tips=tips)

if __name__ == "__main__":
    app.run(debug=True)