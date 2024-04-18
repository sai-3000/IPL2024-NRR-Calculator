from flask import Flask, render_template, request
import math
from decimal import Decimal
import sqlite3

app = Flask(__name__)

# Function to get the sum of runs scored by a team from the database
def get_runs_sum(team_name):
    conn = sqlite3.connect('ipl.db')
    c = conn.cursor()
    c.execute("SELECT runs_scored FROM teams WHERE team_name=?", (team_name,))
    result = c.fetchone()[0]  # Get the first column value (sum of runs scored)
    conn.close()
    return result

# Function to get the sum of overs faced by a team from the database
def get_overs_sum(team_name):
    conn = sqlite3.connect('ipl.db')
    c = conn.cursor()
    c.execute("SELECT overs_faced FROM teams WHERE team_name=?", (team_name,))
    result = c.fetchone()[0]  # Get the first column value (sum of overs faced)
    conn.close()
    return result

# Function to get the sum of runs scored by an opponent team from the database
def get_opponent_runs_sum(team_name):
    conn = sqlite3.connect('ipl.db')
    c = conn.cursor()
    c.execute("SELECT runs_scored FROM teams_opp WHERE team_name=?", (team_name,))
    result = c.fetchone()[0]  # Get the first column value (sum of runs scored)
    conn.close()
    return result

# Function to get the sum of overs faced by an opponent team from the database
def get_opponent_overs_sum(team_name):
    conn = sqlite3.connect('ipl.db')
    c = conn.cursor()
    c.execute("SELECT overs_faced FROM teams_opp WHERE team_name=?", (team_name,))
    result = c.fetchone()[0]  # Get the first column value (sum of overs faced)
    conn.close()
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_nrr', methods=['POST'])
def calculate_nrr():
    if request.method == 'POST':
        team_name_input = request.form['team_name'].upper()
        runs_sum = get_runs_sum(team_name_input)
        overs_sum = get_overs_sum(team_name_input)
        opponent_runs_sum = get_opponent_runs_sum(team_name_input)
        opponent_overs_sum = get_opponent_overs_sum(team_name_input)

        # Calculate decimal part of overs and convert to overs
        decimal_part_runs = (Decimal(str(overs_sum)) % 1) * 10
        overs = math.trunc(overs_sum) + (decimal_part_runs / 6)

        decimal_part_opponent_runs = (Decimal(str(opponent_overs_sum)) % 1) * 10
        opponent_overs = math.trunc(opponent_overs_sum) + (decimal_part_opponent_runs / 6)

        # Calculate Net Run Rate (NRR)
        team_nrr = (runs_sum / overs) - (opponent_runs_sum / opponent_overs)
        team_nrr_rounded = round(team_nrr, 3)

        # Return HTML with NRR result in larger font size
        return f'''<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <link rel="stylesheet" href="static/styles.css">
                        <title>NRR Calculator</title>
                    </head>
                    <body>
                        <div class="nrr-result">
                            Net run rate of {team_name_input} is: <span style="font-size: 32px;">{team_nrr_rounded}</span>
                        </div>
                        <div class="back-button">
                            <a href="/">Back</a>
                        </div>
                    </body>
                    </html>'''
    else:
        return 'Method not allowed.'

if __name__ == '__main__':
    app.run(debug=True)
