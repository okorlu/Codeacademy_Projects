#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# In[ ]:


# Update Recorded Damages
def damages_converter(damages):
    lst = []
    conversion = {"M": 1000000,
              "B": 1000000000}
    for damage in damages:
        if damage == "Damages not recorded":
            lst.append(damage)
        elif damage[-1] == "M":
            lst.append(float(damage[0:-1])*conversion["M"])
        elif damage[-1] == "B":
            lst.append(float(damage[0:-1])*conversion["B"])
    return lst


# In[ ]:


# test function by updating damages
damage_updated = damages_converter(damages)
print(damage_updated)


# In[ ]:


# Create a Hurricane Dictionary
def hurricanes_dic(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    dic = {}
    for i in range(len(names)):
        dic[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], 
                         "Max Sustained Wind": max_sustained_winds[i], "Area Affected": areas_affected[i], 
                         "Damage": damages[i], "Death": deaths[i]}
    return dic


# In[ ]:


# Create and view the hurricanes dictionary
hurricanes = hurricanes_dic(names, months, years, max_sustained_winds, areas_affected, damage_updated, deaths)
print(hurricanes)


# In[ ]:


# Organizing by Year
def hurricane_sorter(hurricanes):
    dic = {}
    for canes in hurricanes:
        current_year = hurricanes[canes]["Year"]
        current_item = hurricanes[canes]
        if current_year not in dic:
            dic[current_year]= [current_item]
        else:
            dic[current_year].append([current_item])
    return dic


# In[ ]:


# create a new dictionary of hurricanes with year and key
hurricane_by_year = hurricane_sorter(hurricanes)
print(hurricane_by_year)


# In[ ]:


# Counting Damaged Areas
def areas_count(hurricanes):
    count = 0
    dic = {}
    area = " "
    for canes in hurricanes:
        for i in range(len(hurricanes[canes]["Area Affected"])):
            area = hurricanes[canes]["Area Affected"][i]
        if area == hurricanes[canes]["Area Affected"][i]:
            count += 1
            dic[area] = count
    return dic


# In[ ]:


# create dictionary of areas to store the number of hurricanes involved in
number_of_hurricane_hits = areas_count(hurricanes)
print(number_of_hurricane_hits)


# In[ ]:


# Calculating Maximum Hurricane Count
def most_affected(number_of_hurricane_hits):
    most_affected = " "
    most_affected_num = 0
    for places in number_of_hurricane_hits:
        if number_of_hurricane_hits[places] > most_affected_num:
            most_affected = places
            most_affected_num = number_of_hurricane_hits[places]
    return most_affected, most_affected_num


# In[ ]:


# find most frequently affected area and the number of hurricanes involved in
most_affected = most_affected(number_of_hurricane_hits)
print(most_affected)


# In[ ]:


# Calculating the Deadliest Hurricane
def casulties_dic(hurricanes):
    name = " "
    number_of_deaths = 0
    for names in hurricanes:
        if hurricanes[names]["Death"] > number_of_deaths:
            name = names
            number_of_deaths = hurricanes[names]["Death"]
    return name, number_of_deaths


# In[ ]:


# find highest mortality hurricane and the number of deaths
highest_casulties = casulties_dic(hurricanes)
print(highest_casulties)


# In[ ]:


# Rating Hurricanes by Mortality
def category_by_mortality_scale(hurricanes):
    mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
    dic = {1:[], 2: [], 3: [], 4: [], 5:[]}
    for canes in hurricanes:
        if hurricanes[canes]["Death"] == mortality_scale[0]:
            dic[0].append(hurricanes[canes])
        elif hurricanes[canes]["Death"] <= mortality_scale[1]:
            dic[1].append(hurricanes[canes])
        elif hurricanes[canes]["Death"] <= mortality_scale[2]:
            dic[2].append(hurricanes[canes])
        elif hurricanes[canes]["Death"] <= mortality_scale[3]:
            dic[3].append(hurricanes[canes])
        elif hurricanes[canes]["Death"] <= mortality_scale[4]:
            dic[4].append(hurricanes[canes])
        else:
            dic[5].append(hurricanes[canes])
    return dic


# In[ ]:


# categorize hurricanes in new dictionary with mortality severity as key
mortality_scales = category_by_mortality_scale(hurricanes)
print(mortality_scales)


# In[ ]:


# Calculating Hurricane Maximum Damage
def cost_calculator(hurricanes):
    cost = 0
    area = " "
    for canes in hurricanes:
        if hurricanes[canes]["Damage"] != "Damages not recorded":
            if hurricanes[canes]["Damage"] > cost:
                cost = hurricanes[canes]["Damage"]
                area = canes
    return area, cost


# In[ ]:


# find highest damage inducing hurricane and its total cost
max_cost = cost_calculator(hurricanes)
print(max_cost)


# In[ ]:


# Rating Hurricanes by Damage
def damage_rating(hurricanes):
    damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
    dic = {0:[], 1: [], 2: [], 3:[], 4:[], 5:[]}
    for canes in hurricanes:
        if hurricanes[canes]["Damage"] == "Damages not recorded":
            dic[0].append(hurricanes[canes])
        elif int(hurricanes[canes]["Damage"]) <= damage_scale[1]:
            dic[1].append(hurricanes[canes])
        elif int(hurricanes[canes]["Damage"]) <= damage_scale[2]:
            dic[2].append(hurricanes[canes])
        elif int(hurricanes[canes]["Damage"]) <= damage_scale[3]:
            dic[3].append(hurricanes[canes])
        elif int(hurricanes[canes]["Damage"]) <= damage_scale[4]:
            dic[4].append(hurricanes[canes])
        else:
            dic[4].append(hurricanes[canes])
    return dic


# In[ ]:


# categorize hurricanes in new dictionary with damage severity as key
damage_rating = damage_rating(hurricanes)
print(damage_rating)


# In[ ]:




