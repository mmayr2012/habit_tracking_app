#!/usr/bin/env python
# coding: utf-8

# In[69]:


import unittest # import for testing the habit tracker
import datetime # import for timestamps
import random  # import for random values for default data (4 weeks)
import matplotlib.pyplot as plt # import for diagram / visualization
import json # import for storing the data
import os # import for storing the data
import pandas as pd # import for table

from habit_tracker import HabitTrackerDaily  # import of the habit tracker

class TestHabitTrackerDaily(unittest.TestCase):

    def setUp(self):
        """Setup a fresh instance of HabitTrackerDaily for each test."""
        self.tracker = HabitTrackerDaily()
        self.tracker.entries = {}  # Leere Einträge für Tests
        self.tracker.previous_successes = []  # Leere Erfolgsnachrichten für Tests

    def test_add_entry_valid(self):
        """Test adding a valid entry."""
        self.tracker.add_entry(8, 9, 7, 6, 10)
        self.assertIn(datetime.date.today().isoformat(), self.tracker.entries)
        self.assertEqual(self.tracker.entries[datetime.date.today().isoformat()]['food'], 8)

    def test_update_entry_valid(self):
        """Test updating an existing entry."""
        self.tracker.add_entry(8, 9, 7, 6, 10)
        self.tracker.update_entry(9, 8, 6, 5, 9)
        self.assertEqual(self.tracker.entries[datetime.date.today().isoformat()]['food'], 9)
        self.assertEqual(self.tracker.entries[datetime.date.today().isoformat()]['sport'], 8)

    def test_calculate_streak(self):
        """Test streak calculation."""
        self.tracker.add_entry(8, 9, 7, 6, 10)
        self.assertEqual(self.tracker.calculate_streak(), 1)
        
        # Simulate adding entries for previous days
        today = datetime.date.today()
        for i in range(1, 5):
            self.tracker.entries[(today - datetime.timedelta(days=i)).isoformat()] = {
                'food': 7, 'sport': 8, 'sleep': 6, 'fun': 5, 'rest': 9
            }
        self.assertEqual(self.tracker.calculate_streak(), 5)

    def test_calculate_selfcare(self):
        """Test self-care score calculation for a specific date."""
        self.tracker.add_entry(8, 9, 7, 6, 10)
        today = datetime.date.today().isoformat()
        self.assertAlmostEqual(self.tracker.calculate_selfcare(today), 8.0)

    def test_calculate_statistics(self):
        """Test overall statistics calculation."""
        # Add sample data
        for i in range(4):
            self.tracker.entries[(datetime.date.today() - datetime.timedelta(days=i)).isoformat()] = {
                'food': 8, 'sport': 7, 'sleep': 6, 'fun': 5, 'rest': 9
            }
        
        stats = self.tracker.calculate_statistics()
        self.assertIsNotNone(stats)
        self.assertIn('food', stats)
        self.assertIn('selfcare', stats)

    def test_save_to_file(self):
        """Test saving data to file."""
        self.tracker.add_entry(8, 9, 7, 6, 10)
        self.tracker.save_to_file()
        self.assertTrue(os.path.exists(self.tracker.file_name))

    def test_load_from_file(self):
        """Test loading data from file."""
        self.tracker.add_entry(8, 9, 7, 6, 10)
        self.tracker.save_to_file()

        # Create a new instance and load data
        new_tracker = HabitTrackerDaily()
        new_tracker.load_from_file()
        self.assertIn(datetime.date.today().isoformat(), new_tracker.entries)

    def test_plot_selfcare(self):
        """Test selfcare plot generation (requires matplotlib)."""
        self.tracker.add_entry(8, 9, 7, 6, 10)
        self.tracker.add_entry(7, 8, 6, 5, 9)
        
        # Ensure that the plot does not raise an error (not necessarily testing the visual output)
        try:
            self.tracker.plot_selfcare()
        except Exception as e:
            self.fail(f"Plotting raised an exception: {e}")

    def test_show_previous_successes(self):
        """Test displaying previous success rewards."""
        self.tracker.add_entry(8, 9, 7, 6, 10)
        self.tracker.check_rewards()
        
        # Simulate a streak of 7 days
        self.tracker.previous_successes.append({
            'streak': 7, 'message': "Congrats! You've tracked your habits for one week! Keep the momentum going! 🎉", 'date': datetime.date.today().isoformat()
        })
        
        # Ensure that the reward message is present
        self.assertGreater(len(self.tracker.previous_successes), 0)


# In[71]:


unittest.main(argv=[''], exit=False)


# In[72]:


get_ipython().system('jupyter nbconvert --to script unit_testing.ipynb')


# In[ ]:




