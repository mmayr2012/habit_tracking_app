#!/usr/bin/env python
# coding: utf-8

# # statistics and diagrams 

# In[6]:


import datetime # import for timestamps
import random  # import for random values for default data (4 weeks)
import matplotlib.pyplot as plt # import for diagram / visualization
import json # import for storing the data
import os # import for storing the data
import pandas as pd

from habit_tracker import HabitTrackerDaily

# instantiate the HabitTracker (daily habits)
tracker = HabitTrackerDaily()

# add demo data with random values
tracker.add_demo_data()


# In[7]:


# calculate statistics such as average, best and worst values for the habits

statistics = tracker.calculate_statistics()
if statistics:
    print("\n--- Statistics ---")
    for habit, stats in statistics.items():
        print(f"{habit.capitalize()}: Average = {stats['average']:.2f}, Best = {stats['best']}, Worst = {stats['worst']}")

def calculate_statistics(self):
    """Calculate statistics including the longest streak."""
    statistics = super().calculate_statistics()  # Falls du eine gemeinsame Funktion hast
    statistics['longest_streak'] = self.calculate_longest_streak()
    return statistics


# In[8]:


# plot the selfcare values to give an overview of the progress over time

tracker.plot_selfcare()


# In[9]:


# self-care score determined by averaging each week, shown in a table

tracker.calculate_weekly_selfcare()

