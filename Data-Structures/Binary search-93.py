## 4. Implementing binary search -- Part 1 ##

# A function to extract a player's last name
def format_name(name):
    return name.split(" ")[1] + ", " + name.split(" ")[0]

# The length of the dataset
length = len(nba)

# Implement the player_age function. For now, simply return what is specified in the instructions
def player_age(name):
    name = format_name(name)
    first_guess_index = math.floor(length/2)
    first_guess = format_name(nba[first_guess_index][0])
    if name < first_guess:
        return "earlier"
    elif name > first_guess:
        return "later"
    else:
        return "found"
    
johnson_odom_age = player_age("Darius Johnson-Odom")
young_age = player_age("Nick Young")
adrien_age = player_age("Jeff Adrien")

## 5. Implementing binary search -- Part 2 ##

# A function to extract a player's last name
def format_name(name):
    return name.split(" ")[1] + ", " + name.split(" ")[0]

# The length of the dataset
length = len(nba)

# Implement the player_age function. For now, simply return what is specified in the instructions
def player_age(name):
    # We need to appropriately format our name for successful comparison
    name = format_name(name)
    upper_bound = length - 1
    lower_bound = 0
    first_guess_index = math.floor(length/2)
    first_guess = format_name(nba[first_guess_index][0])
    if name < first_guess:
        upper_bound = first_guess_index - 1
    elif name > first_guess:
        lower_bound = first_guess_index + 1
    else:
        return first_guess
    second_guess_index = math.floor((lower_bound + upper_bound) / 2)
    second_guess = format_name(nba[second_guess_index][0])
    return second_guess
    
gasol_age = player_age("Pau Gasol")
pierce_age = player_age("Paul Pierce")

## 7. Implementing binary search -- Part 3 ##

# A function to extract a player's last name
def format_name(name):
    return name.split(" ")[1] + ", " + name.split(" ")[0]

# The length of the dataset
length = len(nba)

# Implement the player_age function. For now, simply return what is specified in the instructions
def player_age(name):
    # We need to appropriately format our name for successful comparison
    name = format_name(name)
    # Bounds of the search
    upper_bound = length - 1
    lower_bound = 0
    # Index of first split
    index = math.floor((lower_bound + lower_bound) / 2)
    # First guess halfways through the list
    guess = format_name(nba[index][0])
    # Search until the name is found
    while name != guess:
        if name < guess:
            upper_bound = index - 1
        else:
            lower_bound = index + 1
        index = math.floor((lower_bound + lower_bound) / 2)
        guess = format_name(nba[index][0])
    return "found"
    
carmelo_age = player_age("Carmelo Anthony")

## 8. Implementing binary search -- Part 4 ##

# A function to extract a player's last name
def format_name(name):
    return name.split(" ")[1] + ", " + name.split(" ")[0]

# The length of the dataset
length = len(nba)

# Implement the player_age function. For now, simply return what is specified in the instructions
def player_age(name):
    name = format_name(name)
    upper_bound = length - 1
    lower_bound = 0
    index = math.floor((upper_bound + lower_bound) / 2)
    guess = format_name(nba[index][0])
    while name != guess and upper_bound >= lower_bound:
        if name < guess:
            upper_bound = index - 1
        else:
            lower_bound = index + 1
        index = math.floor((lower_bound + lower_bound) / 2)
        guess = format_name(nba[index][0])
    if name == guess:
        return nba[index][2]
    else:
        return -1
    
curry_age = player_age("Stephen Curry")
griffin_age = player_age("Blake Griffin")
jordan_age = player_age("Michael Jordan")