"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Ryleigh Butler
Date: 10/27/25

AI Usage: Used ChatGPT to help understand def load_character part. I asked for it to explain because I couldn't figure out how to make it work. 
Example: AI helped with file I/O error handling logic in save_character function
"""
import os

# Function 1: Character Creation
def create_character(name, character_class):
    """
    Creates a character dictionary with default stats based on the class.
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    """
    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    character = {
        "name": name,
        "class": character_class,  
        "level": 1,
        "strength": strength, 
        "magic": magic,     
        "health": health,   
        "gold": 100
    }
    return character

    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    pass

# Function 2: Stat Calculation
def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    """   
    if character_class == "Warrior":
        # Has high strength, low magic, high health
        base_strength = 15
        base_magic = 5
        base_health = 100 
    elif character_class == "Mage":
        # Has low strength, high magic, medium health
        base_strength = 4
        base_magic = 20
        base_health = 85
    elif character_class == "Rogue":
        # Has medium strength, medium magic, low health
        base_strength = 7
        base_magic = 10
        base_health = 70
    elif character_class == "Cleric":
        # Has medium strength, high magic, high health
        base_strength = 8
        base_magic = 17
        base_health = 95
    else:
        # Default stats for unknown class
        base_strength = 5
        base_magic = 5
        base_health = 50

    # Scale stats by level
    # Used the built in AI to help understand a little more as to why this works
    strength = base_strength + (level - 1) * 2
    magic = base_magic + (level - 1) * 3
    health = base_health + (level - 1) * 10

    return (strength, magic, health)

    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)

    pass

# Function 3: Save Character
def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # Used AI to help understand the file error handling part
    if filename == "":
        return False
    
    # Open file, write character data, then close
    with open(filename, 'w') as file:
        file.write("Character Name: " + str(character['name']) + "\n")
        file.write("Class: " + str(character['class']) + "\n")
        file.write("Level: " + str(character['level']) + "\n")
        file.write("Strength: " + str(character['strength']) + "\n")
        file.write("Magic: " + str(character['magic']) + "\n")
        file.write("Health: " + str(character['health']) + "\n")
        file.write("Gold: " + str(character['gold']) + "\n")
    
    
    # Return True to indicate successful save
    return True

 
# Function 4: Load Character
def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # Check if file exists
    if not os.path.exists(filename):
        return None

    with open(filename, 'r') as file:
        lines = file.readlines()
        
    character = {}
    for line in lines:
        if ": " in line:
            key, value = line.strip().split(": ")
            
            # Convert key format (e.g., "Character Name" -> "name")
            if key == "Character Name":
                key = "name"
            else:
                key = key.lower()
            
            # Convert numeric values to integers
            if key in ["level", "strength", "magic", "health", "gold"]:
                value = int(value)
                
            # Store in character dictionary
            character[key] = value
    
    return character

# Function 5: Display Character
def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # Print formatted character sheet
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    # TODO: Implement this function

# Function 6: Leveling Up
def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # Increase level by 1 and update stats
    character['level'] += 1
    strength, magic, health = calculate_stats(character['class'], character['level'])
    
    character['strength'] = strength
    character['magic'] = magic
    character['health'] = health

    print(f"{character['name']} has leveled up to level {character['level']}!")
    # TODO: Implement this function
    # Remember to recalculate stats for the new level


# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    a = input("Enter character name: ")
    b = input("Enter character class (Warrior, Mage, Rogue, Cleric): ")
    char  = create_character(a, b)

    display_character(char)
    save_character(char, "my_character.txt")
    loaded = load_character("my_character.txt")
    print("Loaded character from file:")
    print(loaded)
   
