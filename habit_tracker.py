#!/usr/bin/env python
# coding: utf-8

# # HABIT TRACKER

# ### - Core functionality
# ### - Adding demo data, new entries and updating them
# ### - Rewards test of previous success is also included
# ### - Storing the data and saving the file finalize this file

# # CORE FUNCTIONALITY

# In[362]:


import datetime # import for timestamps
import random  # import for random values for default data (4 weeks)
import matplotlib.pyplot as plt # import for diagram / visualization
import json # import for storing the data
import os # import for storing the data
import pandas as pd


class HabitTrackerDaily:
    """Class to track daily habits with rewards and streaks."""
    
    def __init__(self, file_name="habit_data.json"):
        self.entries = {}
        self.previous_successes = []
        self.REWARD_MESSAGES = {
            7: "Congrats! You've tracked your habits for one week! Keep the momentum going! 🎉",
            14: "Amazing! Two weeks of consistent tracking! You're building a great habit! 🌟",
            21: "Three weeks strong! Your determination is inspiring! 💪",
            30: "One month! You're unstoppable! Keep thriving! 🏆",
            60: "Two months! Your consistency is phenomenal! ✨",
            90: "Three months of success! You're mastering your habits! 🚀",
            180: "Six months! This is a lifestyle now. Incredible! 🌈",
            365: "One year of daily tracking! You're a self-care champion! 🎉🎊"
        }
        self.file_name = file_name  # File to store and load data

    def add_entry(self, food, sport, sleep, fun, rest):
        """Add daily habit entry, only one per day allowed."""
        today = datetime.date.today().isoformat()
        error_messages = []
        
        # Überprüfen, ob heute bereits ein Eintrag existiert
        if today in self.entries:
            error_messages.append("Entry for today already exists. Use update_entry to modify.")
            
        # Überprüfen, ob alle Werte im gültigen Bereich sind
        if not all(0 <= val <= 10 for val in [food, sport, sleep, fun, rest]):
            error_messages.append("All values must be in the range 0-10.")
            
        # Falls Fehler vorhanden, werfe eine ValueError mit den Fehlermeldungen
        if error_messages:
            raise ValueError(" | ".join(error_messages))
            
        # Ansonsten Eintrag hinzufügen
        self.entries[today] = {'food': food, 'sport': sport, 'sleep': sleep, 'fun': fun, 'rest': rest}
        self.check_rewards()

    def update_entry(self, food, sport, sleep, fun, rest):
        """Update today's entry."""
        today = datetime.date.today().isoformat()
        error_messages = []
    
        # Überprüfen, ob der Eintrag für heute existiert
        if today not in self.entries:
            error_messages.append("No entry for today exists. Use add_entry to create one.")
        
        # Überprüfen, ob alle Werte im gültigen Bereich sind
        if not all(0 <= val <= 10 for val in [food, sport, sleep, fun, rest]):
            error_messages.append("All values must be in the range 0-10.")
        
        # Falls Fehler vorhanden, werfe eine ValueError mit den Fehlermeldungen
        if error_messages:
            raise ValueError(" | ".join(error_messages))
        
        # Ansonsten den Eintrag für heute aktualisieren
        self.entries[today] = {'food': food, 'sport': sport, 'sleep': sleep, 'fun': fun, 'rest': rest}


    def calculate_streak(self):
        """Calculate the current streak of consecutive days with entries."""
        sorted_dates = sorted(self.entries.keys(), reverse=True)
        streak = 0
        today = datetime.date.today()
        for i, date_str in enumerate(sorted_dates):
            expected_date = (today - datetime.timedelta(days=i)).isoformat()
            if date_str == expected_date:
                streak += 1
            else:
                break
        return streak

    def calculate_selfcare(self, date):
        """Calculate the selfcare score for a given date."""
        if date not in self.entries:
            return None
        habit_values = self.entries[date].values()
        return sum(habit_values) / len(habit_values)

    def calculate_weekly_selfcare(self):
        """Calculate average self-care value for each week."""
        weekly_selfcare = {}
        for date, habits in self.entries.items():
            year, week, _ = datetime.date.fromisoformat(date).isocalendar()
            week_key = f"{year}-W{week}"
        
            if week_key not in weekly_selfcare:
                weekly_selfcare[week_key] = []
            weekly_selfcare[week_key].append(self.calculate_selfcare(date))
    
        # calculate weekly averages
        weekly_averages = {week: sum(values) / len(values) for week, values in weekly_selfcare.items()}

        # change dictionnaries to Pandas DataFrame
        df = pd.DataFrame(list(weekly_averages.items()), columns=['week', 'selfcare scoring'])
        # sorting through week
        
        df['week'] = pd.to_datetime(df['week'] + '-1', format='%Y-W%U-%w')
        df = df.sort_values(by='week', ascending=False)

        return df
    
    def check_rewards(self):
        """Check for streak milestones and award rewards."""
        streak = self.calculate_streak()
        milestones = [milestone for milestone in self.REWARD_MESSAGES if streak >= milestone]
        for milestone in milestones:
            if milestone not in [success['streak'] for success in self.previous_successes]:
                message = self.REWARD_MESSAGES[milestone]
                self.previous_successes.append({
                    'streak': milestone,
                    'message': message,
                    'date': datetime.date.today().isoformat()
                })
                print(message)

    def show_previous_successes(self):
        """Display all previously achieved rewards."""
        if not self.previous_successes:
            print("No rewards achieved yet.")
        else:
            print("\n--- Previous Successes ---")
            for success in sorted(self.previous_successes, key=lambda x: x['streak']):
                print(f"Streak: {success['streak']} days - {success['message']} (Achieved on: {success['date']})")

    def show_all_data(self):
        """Display all recorded data with selfcare scores."""
        for date, habits in sorted(self.entries.items()):
            selfcare = self.calculate_selfcare(date)
            print(f"{date} - Habits: {habits}, Selfcare: {selfcare:.2f}")

    def add_demo_data(self):
        """Add sample data for the last four weeks with random values."""
        base_date = datetime.date.today()
        for i in range(28):  # 4 weeks of data
            day = base_date - datetime.timedelta(days=i)
            self.entries[day.isoformat()] = {
                'food': random.randint(0, 10),
                'sport': random.randint(0, 10),
                'sleep': random.randint(0, 10),
                'fun': random.randint(0, 10),
                'rest': random.randint(0, 10)
            }
        
    def calculate_statistics(self):
        """Calculate average, best, and worst values for each habit and selfcare."""
        try:
            if not self.entries:
                raise ValueError("No data available to calculate statistics.")
            
            # Collect all values for each habit
            all_values = {habit: [] for habit in ['food', 'sport', 'sleep', 'fun', 'rest']}
            all_selfcare = []
            
            for date, habits in self.entries.items():
                for habit, value in habits.items():
                    all_values[habit].append(value)
                all_selfcare.append(self.calculate_selfcare(date))
            
            # Calculate statistics
            statistics = {
                habit: {
                    'average': sum(values) / len(values),
                    'best': max(values),
                    'worst': min(values)
                }
                for habit, values in all_values.items()
            }
            
            statistics['selfcare'] = {
                'average': sum(all_selfcare) / len(all_selfcare),
                'best': max(all_selfcare),
                'worst': min(all_selfcare)
            }
            
            return statistics
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def plot_selfcare(self):
        """Generate a line plot of the Selfcare values over time."""
        try:
            if not self.entries:
                raise ValueError("No data available to plot selfcare.")
            
            # Extract dates and selfcare values
            dates = sorted(self.entries.keys())
            selfcare_values = [self.calculate_selfcare(date) for date in dates]
            
            # Plot the data
            plt.figure(figsize=(10, 6))
            plt.plot(dates, selfcare_values, marker='o', linestyle='-', color='blue')
            plt.title("Selfcare Values Over Time")
            plt.xlabel("Date")
            plt.ylabel("Selfcare Value")
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        except ValueError as e:
            print(f"Error: {e}")
    def save_to_file(self):
        data = {
            'entries': self.entries,
            'previous_successes': self.previous_successes
        }
        with open(self.file_name, 'w') as file:
            json.dump(data, file)
        print(f"Data saved to {self.file_name}.")

    def load_from_file(self):
        if not os.path.exists(self.file_name) or os.stat(self.file_name).st_size == 0:
            print(f"Die Datei {self.file_name} existiert nicht oder ist leer. Standardwerte werden verwendet.")
            self.entries = {}
            self.previous_successes = []
            return
    
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)  # Versuche, die Datei zu laden
            self.entries = data.get('entries', {})
            self.previous_successes = data.get('previous_successes', [])
        except (json.JSONDecodeError, IOError) as e:
            print(f"Fehler beim Laden der Datei: {e}")
            self.entries = {}
            self.previous_successes = []
            
    # Example test function for duplicate entry
    def test_add_entry_duplicate(self):
        tracker = HabitTrackerDaily()
        
        # Füge einen ersten Eintrag hinzu
        tracker.add_entry(8, 9, 7, 6, 10)
        
        # Versuche, denselben Eintrag erneut hinzuzufügen und prüfe, ob der Fehler geworfen wird
        with self.assertRaises(ValueError):
            tracker.add_entry(9, 9, 9, 9, 9)


# In[348]:


print("Welcome to your Selfcare journey!")

habit_tracking_description = """The main goal of the Habit Tracking App is to assist users in self-reflection and goal tracking. 
Recording habits can make progress visible and increase motivation. \nThe project includes:
\n1. Daily Habit Tracking: Users rate daily activities such as nutrition, exercise, sleep, fun, and relaxation on a scale of 0 to 10.
2. Weekly Habit Tracking: Additionally, weekly habits can be defined and monitored to track long-term personal goals.
3. Reward System: Achieving certain streaks is rewarded with motivational messages to reinforce positive behavior patterns.
4. Visualization and Analysis: Charts and statistics provide a better overview of progress and self-care.
"""
print(habit_tracking_description)


# # ADDING DEMO DATA

# In[366]:


# Instantiate the HabitTracker (daily habits)
tracker = HabitTrackerDaily()

# Add demo data with random values
tracker.add_demo_data()

# Show all data including selfcare scores
tracker.show_all_data()


# # ADDING / UPDATING ENTRIES

# In[350]:


# Add a new entry (intentionally wrong)
tracker.add_entry(8, 9, 97, 6, 10)


# In[352]:


# Add a new entry (if clicked twice, error is triggered)
tracker.add_entry(8, 9, 7, 6, 10)


# In[355]:


# Update a new entry (intentionally wrong)
tracker.update_entry(8, 9, 27, 6, 10)


# In[354]:


# Update a new entry
tracker.update_entry(8, 9, 7, 6, 10)


# # REWARDS TEST / PREVIOUS SUCCESS (demo data)

# In[356]:


# Instantiate the HabitTracker (daily habits)
tracker = HabitTrackerDaily()

# Add demo data with random values (also checks rewards)
tracker.add_demo_data()

# Display previous successes
tracker.check_rewards()
tracker.show_previous_successes()


# # STORING DATA

# In[364]:


# Instantiate the HabitTracker
tracker = HabitTrackerDaily()

# Load data from file if available
tracker.load_from_file()

# Save updated data
tracker.save_to_file()


# # SAVE THE FILE (export)

# In[365]:


get_ipython().system('jupyter nbconvert --to script habit_tracker.ipynb')


# # debugging (storing data)

# In[359]:


print("json module loaded:", json) # for debugging, shows the path from which the json module is loaded

