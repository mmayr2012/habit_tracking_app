# First: Installation 

Before installing the Habit Tracking App, make sure you have the following prerequisites:

- Python 3.8 or higher is installed on your computer.

- A package manager such as pip is available.

- Git is installed in case you want to clone the code directly from a repository.

If not, install the required Python libraries:
- pandas
- matplotlib

# Next: Clone repository & run app

# Documentation for the `HabitTrackerDaily` Class

The `HabitTrackerDaily` class allows users to track their daily habits, calculate self-care scores, monitor streaks, and receive rewards based on their consistency. It includes methods for adding and updating daily habit entries, calculating streaks, visualizing habit data, and saving/loading data from a file.

## Table of Contents
1. Imports
2. Class-Overview
3. Constructor
4. Methods

---

### Imports
- `datetime`: For handling dates and timestamps.
- `random`: For generating random values for demo data.
- `matplotlib.pyplot`: For creating plots and visualizations.
- `json`: For saving and loading data from a file.
- `os`: For file operations.
- `pandas`: For handling data and creating DataFrames.

---

### Class Overview
This class enables users to track five daily habits:
- **Food**
- **Sport**
- **Sleep**
- **Fun**
- **Rest**

The class provides methods to add, update, and display entries, calculate self-care ratings, track streaks, and visualize progress. It also supports saving and loading data from a file and displays rewards based on streaks achieved.

---

### Constructor

- **`file_name`** (Default: `"habit_data.json"`): The name of the file used to store and load habit data.

The constructor initializes:
- `entries`: A dictionary that stores daily habit data.
- `previous_successes`: A list that stores previously achieved reward streaks.
- `REWARD_MESSAGES`: A dictionary containing reward messages for different streak milestones (e.g., 7, 14, 30 days).

---

### Methods

#### `add_entry`
- Adds a new habit entry for the current day. It checks if an entry already exists for the day and ensures that all values are within the valid range (0-10).
- Raises a `ValueError` if the entry already exists or if any value is out of range.

#### `update_entry`
- Updates the habit entry for the current day, if it exists. Ensures that all values are within the valid range.
- Raises a `ValueError` if the entry does not exist or if the values are invalid.

#### `calculate_streak`
- Calculates the current streak (the number of consecutive days with entries).
- Returns the length of the streak.

#### `calculate_selfcare`
- Calculates the self-care score for a given date based on the values of the five habits (food, sport, sleep, fun, rest).
- Returns the self-care score as a float, or `None` if no entry exists for the given date.

#### `calculate_weekly_selfcare`
- Calculates the average self-care score for each week and returns the values in a Pandas DataFrame, sorted by week.

#### `check_rewards`
- Checks if the current streak has reached a reward milestone (e.g., 7, 14, 30 days) and prints the corresponding reward message if achieved.

#### `show_previous_successes`
- Displays all previously achieved rewards, including the length of the streak and the corresponding reward message.

#### `show_all_data`
- Displays all recorded data for each day, including the self-care score for that day.

#### `add_demo_data`
- Adds demo data for the past four weeks with random values. Useful for testing and demonstration purposes.

#### `calculate_statistics`
- Calculates statistics (average, best, and worst values) for each habit and the self-care score based on all recorded entries.

#### `plot_selfcare`
- Generates a line plot of the self-care values over time.

#### `save_to_file`
- Saves the current data (`entries` and `previous_successes`) to a JSON file.

#### `load_from_file`
- Loads the habit data and previous rewards from a JSON file. If the file does not exist or is empty, it uses default values.

#### `test_add_entry_duplicate`
- A test method that ensures the `add_entry` method raises a `ValueError` when trying to add the same entry for the same day again.

# As an addition, the user can enter weekly habits, to track personal growth on individual habits.

---

### Weekly Habit Tracker

The HabitTrackerWeekly class allows users to track weekly habits, such as personal goals. Key functionalities include:

* add_habit(habit_name): Add a new weekly habit to track.

* remove_habit(habit_name): Remove an existing weekly habit.

* add_weekly_entry(week_number, kwargs): Add or update weekly entries for specific habits. You can provide values for each habit by passing them as keyword arguments (e.g., food=7, sport=8).

* show_habits(): Display the list of currently tracked weekly habits.

* show_weekly_data(): Display all recorded weekly habit data.

* calculate_weekly_average(week_number): Calculate the average score for the specified week.

* save_to_file(): Save weekly habit data to a file.

* load_from_file(): Load weekly habit data from a file.
