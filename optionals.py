#!/usr/bin/env python
# coding: utf-8

# # optional: add weekly habits

# ## the user should get the chance to add weekly habits f. e. to track personal goals on a weekly basis

# In[4]:


import json
import datetime

class HabitTrackerWeekly:
    def __init__(self, file_name="weekly_habit_data.json"):
        """Initialize the weekly habit tracker."""
        self.weekly_entries = {}  # Store weekly habits {week_number: {'habit1': value, 'habit2': value, ...}}
        self.habit_list = []  # List of user-defined weekly habits
        self.file_name = file_name  # File to store and load data
    
    def add_habit(self, habit_name):
        """Add a new weekly habit."""
        if habit_name in self.habit_list:
            print(f"Habit '{habit_name}' already exists.")
        else:
            self.habit_list.append(habit_name)
            print(f"Habit '{habit_name}' has been added.")
    
    def remove_habit(self, habit_name):
        """Remove an existing habit."""
        if habit_name in self.habit_list:
            self.habit_list.remove(habit_name)
            print(f"Habit '{habit_name}' has been removed.")
        else:
            print(f"Habit '{habit_name}' does not exist.")
    
    def add_weekly_entry(self, week_number, **kwargs):
        """Add or update values for habits for a specific week."""
        if week_number not in self.weekly_entries:
            self.weekly_entries[week_number] = {}
        for habit, value in kwargs.items():
            if habit not in self.habit_list:
                print(f"Habit '{habit}' is not in the list of habits. Please add it first.")
            elif not (0 <= value <= 10):
                print(f"Value for habit '{habit}' must be between 0 and 10.")
            else:
                self.weekly_entries[week_number][habit] = value
        print(f"Weekly data for week {week_number} has been updated.")
    
    def show_habits(self):
        """Display the list of weekly habits."""
        if not self.habit_list:
            print("No habits have been added yet.")
        else:
            print("Tracked Weekly Habits:")
            for habit in self.habit_list:
                print(f"- {habit}")
    
    def show_weekly_data(self):
        """Display all recorded weekly habit data."""
        if not self.weekly_entries:
            print("No weekly entries have been recorded yet.")
        else:
            print("\n--- Weekly Habit Data ---")
            for week, habits in sorted(self.weekly_entries.items()):
                print(f"Week {week}: {habits}")
    
    def calculate_weekly_average(self, week_number):
        """Calculate the average score for a specific week."""
        if week_number not in self.weekly_entries:
            print(f"No data found for week {week_number}.")
            return None
        habits = self.weekly_entries[week_number]
        return sum(habits.values()) / len(habits)
    
    def save_to_file(self):
        """Save weekly habit data to a file."""
        data = {
            'habit_list': self.habit_list,
            'weekly_entries': self.weekly_entries
        }
        with open(self.file_name, 'w') as file:
            json.dump(data, file)
        print(f"Weekly data saved to {self.file_name}.")
    
    def load_from_file(self):
        """Load weekly habit data from a file."""
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
            self.habit_list = data.get('habit_list', [])
            self.weekly_entries = data.get('weekly_entries', {})
            print(f"Weekly data loaded from {self.file_name}.")
        except FileNotFoundError:
            print(f"No existing data file found. Starting fresh.")


# In[5]:


# converts the single notebook to a python file
get_ipython().system('jupyter nbconvert --to script optionals.ipynb')


# In[ ]:




