from flask import Flask, render_template, request
import requests



#___________________________________________________________________________________________________________________________________________________

#Used for the Calculator Page
WINS = 29
LOSSES = 15
total_games = WINS + LOSSES

def get_calc_value(unit_value):
    input = float(unit_value)
    total_won = float(WINS) * input
    total_winnings = float(total_won * 0.90909)
    total_loss = float(LOSSES * input)
    total_win_loss = total_winnings - total_loss
    return total_win_loss

ratio = WINS/total_games
ratio = ratio * 100
ratio = "{:.3f}".format(ratio)

record = {'wins': WINS, 'losses': LOSSES}


# v2 Calculator

WINS_v2 = 20
LOSSES_v2 = 38
total_games_v2 = WINS_v2 + LOSSES_v2

def get_calc_value_v2(unit_value):
    input = float(unit_value)
    total_won = float(WINS_v2) * input
    total_winnings = float(total_won * 0.90909)
    total_loss = float(LOSSES_v2 * input)
    total_win_loss = total_winnings - total_loss
    return total_win_loss

ratio_v2 = WINS_v2/total_games_v2
ratio_v2 = ratio_v2 * 100
ratio_v2 = "{:.3f}".format(ratio_v2)

record_v2 = {'wins': WINS_v2, 'losses': LOSSES_v2}




# -------------------------------------------------------------------------- STARTING FLASK APP -------------------------------------------------------------

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

# Current Week V1 page
@app.route("/current_week_v1")
def current_week_v1():
    return render_template("current_week_v1.html")

# Current Week V2 page
@app.route("/current_week_v2")
def current_week_v2():
    return render_template("current_week_v2.html")

# History page
@app.route("/history")
def history():
    return render_template("history.html")

# Calculator page
@app.route("/calculator/", methods=["POST", "GET"])
def calculator():
    if request.method == "POST":
        unit_value = request.form["unit_price"]
        solution = get_calc_value(unit_value)
        solution = "{:.2f}".format(solution)
        is_positive = False
        if float(solution) > 0:
            is_positive = True
        return render_template("calculator.html", record = record, solution = solution, is_positive = is_positive, ratio = ratio)
    else:
        return render_template("calculator.html", record = record )
    

# Calculator v2page
@app.route("/calculator_v2/", methods=["POST", "GET"])
def calculator_v2():
    if request.method == "POST":
        unit_value = request.form["unit_price"]
        solution = get_calc_value_v2(unit_value)
        solution = "{:.2f}".format(solution)
        is_positive = False
        if float(solution) > 0:
            is_positive = True
        return render_template("calculator_v2.html", record = record_v2, solution = solution, is_positive = is_positive, ratio = ratio_v2)
    else:
        return render_template("calculator_v2.html", record = record_v2 )

if __name__ == "__main__":
    app.run(debug=True)
