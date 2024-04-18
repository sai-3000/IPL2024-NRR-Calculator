# IPL Net Run Rate (NRR) Calculator

This Flask web application calculates the Net Run Rate (NRR) for cricket teams based on the runs scored and overs faced.

## Getting Started

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Make sure you have a SQLite database named `ipl.db` with the required tables (`teams` and `teams_opp`) and data.
4. Run the Flask application using `python app.py`.
5. Access the application in your web browser at `http://localhost:5000`.

## Usage

1. Enter the name of the team for which you want to calculate the NRR.
2. Submit the form to view the calculated NRR.
3. Click on the "Back" button to go back to the home page.

## File Structure

- `app.py`: Contains the Flask application code.
- `static/`: Contains CSS stylesheets (`styles.css`).
- `templates/`: Contains HTML templates (`index.html`) for the web pages.

## Dependencies

- Flask
- SQLite3
- math
- decimal

## Database Schema

- Table `teams`:
  - Columns: `team_name`, `runs_scored`, `overs_faced`

- Table `teams_opp`:
  - Columns: `team_name`, `runs_scored`, `overs_faced`

## Credits

This project is created by Sai Smaran Panda and is inspired by the Net Run Rate calculation used in cricket tournaments like the Indian Premier League (IPL).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
