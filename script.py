# names of hurricanes
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

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def updated_damages(list1):
  newdamages = []
  for i in list1:
    if 'M' in i:
      new = float(i[0:i.index('M')]) * 1000000
      newdamages.append(new)
    elif 'B' in i:
      new = float(i[0:i.index('B')]) * 1000000000
      newdamages.append(new)
    else:
      newdamages.append(i)
  return newdamages

# test function by updating damages
newdamages = updated_damages(damages)


# 2 
# Create a Table
def combine_dict(names, month, year, max_sustained_wind, areas_affected, damages, death):
  newdict = {}
  for i in range(len(names)):
    newdict[names[i]] = {"Name": names[i],
                          "Month": month[i],
                          "Year": year[i],
                          "Max Sustained Wind": max_sustained_wind[i],
                          "Areas Affected": areas_affected[i],
                          "Damage": damages[i],
                          "Death": death[i]}
  return newdict

# Create and view the hurricanes dictionary
hurricanesdict = combine_dict(names, months, years, max_sustained_winds, areas_affected, newdamages, deaths)


# 3
# Organizing by Year
def canes_by_year(canes):
  hurricanes_by_year= dict()
  for cane in canes:
      current_year = canes[cane]['Year']
      current_cane = canes[cane]
      if current_year not in hurricanes_by_year:
          hurricanes_by_year[current_year] = [current_cane]
      else:
          hurricanes_by_year[current_year].append(current_cane)
  return hurricanes_by_year

# create a new dictionary of hurricanes with year and key
canes_by_year = canes_by_year(hurricanesdict)


# 4
# Counting Damaged Areas
def affected_areas(hurricanes):
  areas_count = dict()
  for cane in hurricanes:
    for area in hurricanes[cane]['Areas Affected']:
      if area not in areas_count:
        areas_count[area] = 1
      else:
        areas_count[area] += 1
  return areas_count

# create dictionary of areas to store the number of hurricanes involved in
areas_count = affected_areas(hurricanesdict)

# 5 
# Calculating Maximum Hurricane Count
def max_hit(areas_count):
  max_area = 'Central America'
  max_count = 0
  for cane in areas_count:
    if areas_count[cane] > max_count:
      max_area = cane
      max_count = areas_count[cane]
    else:
      max_area = max_area
      max_count = max_count
  return(max_area, max_count)

# find most frequently affected area and the number of hurricanes involved in
most = max_hit(areas_count)


# 6
# Calculating the Deadliest Hurricane
def cane_deaths(hurricanes):
   max_death = 'Central America'
   max_count = 0
   for cane in hurricanes:
      if hurricanes[cane]['Death'] > max_count:
        max_death = hurricanes[cane]['Name']
        max_count = hurricanes[cane]['Death']
      else:
        max_death = max_death
        max_count = max_count
   return (max_death,max_count)
# find highest mortality hurricane and the number of deaths
highest_death = cane_deaths(hurricanesdict)


# 7
# Rating Hurricanes by Mortality
def mortality(hurricanes):
  mortality_scale = {0: 0,
                1: 100,
                2: 500,
                3: 1000,
                4: 10000}
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for cane in hurricanes:
    num_deaths = hurricanes[cane]['Death']
    if num_deaths == mortality_scale[0]:
      hurricanes_by_mortality[0].append(hurricanes[cane])
    elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
      hurricanes_by_mortality[1].append(hurricanes[cane])
    elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
      hurricanes_by_mortality[2].append(hurricanes[cane])
    elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
      hurricanes_by_mortality[3].append(hurricanes[cane])
    elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
      hurricanes_by_mortality[4].append(hurricanes[cane])
    elif num_deaths > mortality_scale[4]:
      hurricanes_by_mortality[5].append(hurricanes[cane])
  return hurricanes_by_mortality

# categorize hurricanes in new dictionary with mortality severity as key
by_mortality = mortality(hurricanesdict)


# 8 Calculating Hurricane Maximum Damage
def max_damage(hurricanes):
  damage_cane = 'Cuba I'
  max_damage = 0
  for cane in hurricanes:
    if hurricanes[cane]['Damage'] == 'Damages not recorded':
      continue
    if hurricanes[cane]['Damage'] > max_damage:
      damage_cane = hurricanes[cane]['Name']
      max_damage = hurricanes[cane]['Damage']
    else:
      damage_cane = damage_cane
      max_damage = max_damage
  return(damage_cane, max_damage)
      
# find highest damage inducing hurricane and its total cost
highest_damage = max_damage(hurricanesdict)


# 9
# Rating Hurricanes by Damage
def by_damage(hurricanes):
  damage_scale = {0: 0,
                  1: 100000000,
                  2: 1000000000,
                  3: 10000000000,
                  4: 50000000000}
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for cane in hurricanes:
    num_damage = hurricanes[cane]['Damage']
    if hurricanes[cane]['Damage'] == 'Damages not recorded':
      continue
    if num_damage == damage_scale[0]:
      hurricanes_by_damage[0].append(hurricanes[cane])
    elif num_damage > damage_scale[0] and num_damage <= damage_scale[1]:
      hurricanes_by_damage[1].append(hurricanes[cane])
    elif num_damage > damage_scale[1] and num_damage <= damage_scale[2]:
      hurricanes_by_damage[2].append(hurricanes[cane])
    elif num_damage > damage_scale[2] and num_damage <= damage_scale[3]:
      hurricanes_by_damage[3].append(hurricanes[cane])
    elif num_damage > damage_scale[3] and num_damage <= damage_scale[4]:
      hurricanes_by_damage[4].append(hurricanes[cane])
    elif num_damage > damage_scale[4]:
      hurricanes_by_damage[5].append(hurricanes[cane])
  return hurricanes_by_damage

  
# categorize hurricanes in new dictionary with damage severity as key

canes_by_damage = by_damage(hurricanesdict)
print(canes_by_damage)
