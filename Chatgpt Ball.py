# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 17:48:40 2023

@author: rfranco11
"""

initial_velocity = 50  # Initial velocity in feet per second
acceleration_due_to_gravity = 32.17  # Acceleration due to gravity in feet per second squared
initial_height = 0  # Initial height in feet

max_height = (initial_velocity ** 2) / (2 * acceleration_due_to_gravity) + initial_height

print("The maximum height reached by the ball is:", max_height, "feet")
