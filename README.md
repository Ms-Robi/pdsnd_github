>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date created
27/7/2023

### Project Title
Bikeshare 

### Description
This Python script analyzes bike share data from three cities: Chicago, New York City and Washington. The user can input their preferred city, month, and day of the week to explore the data.

### Files used
Before running the script, make sure you have the following installed:

Python 3
pandas
numpy

### Important Notes
If you enter an invalid city, month, or day of the week, the script will prompt you to re-enter the information.

The script assumes that the CSV files have columns for "Start Time," "End Time," "Start Station," "End Station," "User Type," "Gender," and "Birth Year." If any of these columns are missing, the script will inform you that the information is not available.

The script uses the pandas library to load and manipulate the data, and the numpy library for numerical computations.

Make sure to check the terminal for any error messages or prompts while running the script.

### Credits
Stack Overflow - Finding start-time and end-time of events in a day - Pandas timeseries - such that end time does not fall into next day (https://stackoverflow.com/questions/67333038/finding-start-time-and-end-time-of-events-in-a-day-pandas-timeseries-such-th)

Earthly - How To Read A CSV File In Python (https://earthly.dev/blog/csv-python/)


### Steps on How to Use the Code

1. Download the CSV files for each city's bike share data: chicago.csv, new_york_city.csv, and washington.csv.
2. Place the CSV files in the same directory as the Python script.
3. Open your terminal or command prompt and navigate to the directory containing the script and CSV files.
4. Run the script using the following command, python bikeshare_analysis.py
5. Follow the instructions in the terminal to select the city, month, and day of the week for analysis.
6. The script will display various statistics and insights about the bike share data based on your input.
7. After viewing the statistics, the script will prompt you to see individual trip data. Type "yes" or "no" to view or skip this option.
8. If you choose to see individual trip data, you can specify the number of rows to display at a time.
9. The script will continue asking if you want to view more trip data until you type "no."
10. After exploring the data, you can choose to restart the analysis or exit the program.
