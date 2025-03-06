

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