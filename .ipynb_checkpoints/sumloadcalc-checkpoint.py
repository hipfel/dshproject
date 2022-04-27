# 
"""
Function for handling the widget on Loads_Summer.ipynb
"""
import numpy as np
import psychro as psy

# A * x = b ==> x = inv(A) * b
# constants
c = 1e3                     # air specific heat J/kg K
l = 2496e3                  # latent heat J/kg

# Function for just creating widget to define parameters and later on saving them in variables
def summerloadcalc(θ0=30, φ0=0.8, θi=23, φi=0.6):

    print(f'θ0 = {θ0:5.1f} °C, φ0 = {φ0*100:5.0f} %')
    print(f'θi = {θi:5.1f} °C, φi = {φi*100:5.0f} %')
    print('')
    print('Change the values with the sliders. Then klick on the next Jupyter Notebook row and run it to save the parameters.')
    return θ0, φ0, θi, φi

