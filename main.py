#from myFunctions import *
from colorama import Fore, Style
import os
os.system('clear')


### from myFunctions.py ###

# Counts the total number of space missions.
def count_num_missions(missions_list):
    num = 0
    for i in missions_list:
        num += 1
    return num



# Counts the number of successful missions.
def count_num_success(missions_list):
    num = 0
    for i in missions_list:
        if i == True:
            num +=1
    return num


# Calculates the success rate of the missions.
def calc_success_rate(missions, successes):
    rate = (successes / missions) * 100
    rate = round(rate, 2)
    return rate




# Identifys list of missions launched before year 2000.
def identify_pre2000(years, names):
    pre2000_names = []
    for year, name in zip(years, names):    # To go through both list together
        if year < 2000:
            pre2000_names.append(name)

    return pre2000_names




def print_bulletList(list):
    for name in list:
        print(f"- {name}")

### end myFunctions.py ###

mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

total_missions = 0
successful_missions = 0
success_rate = 0
pre_2000_missions = []

# Count the total number of space missions.
total_missions = count_num_missions(mission_success)      # could have use any one of the lists

# Count the number of successful missions.
successful_missions = count_num_success(mission_success)

# Calculate the success rate of the missions.
success_rate = calc_success_rate(total_missions, successful_missions)

# Identify list of missions launched before year 2000.
pre_2000_missions = identify_pre2000(mission_years, mission_names)



print("Total number of missions: ", end="")                     # print the total number of missions.
print(Fore.BLUE + str(total_missions) + Style.RESET_ALL) 

print("Number of successful missions: ", end="")                # print the number of successful missions.
print(Fore.BLUE + str(successful_missions) + Style.RESET_ALL)

print("Success rate: ", end="")                                 # print the success rate as a percentage.
print(Fore.BLUE + str(success_rate) + "%" + Style.RESET_ALL)

print("Missions launched before the year 2000:")                # print the names of the missions launched before the year 2000.
print_bulletList(pre_2000_missions)
