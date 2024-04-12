"""Python program to record and 
analyse temperatures for a weather station"""

import numpy as np

def record_temperatures(user_input,choice):
    temperature_list = list(user_input.split(','))
    temperature_list = [ float(x) for x in temperature_list ]
    analyse_temperatures(temperature_list,choice)
    

def analyse_temperatures(temperature_list,choice):
    analysis = {'max_temperature': np.max(temperature_list),
                'min_temperature': np.min(temperature_list),
                'average_temperature': round(np.mean(temperature_list),3)}
    
    display(temperature_list,analysis,choice)

def display(temperature_list,analysis,choice):
    analysis_short = f"Maximum temperature is: {analysis['max_temperature']}\nMinimum temperature is: {analysis['min_temperature']}\nAverage temperature is: {analysis['average_temperature']}\n"
    print( f"Preferred Unit: {choice}\n temperatures recorded: {temperature_list}\n {analysis_short}")
    
    

choice = input('Choice of unit: Kelvin, Celsius, Farenheit\n\n')
user_input = input("Enter temperatures separated by comma:\n")
record_temperatures(user_input,choice)


