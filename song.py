"""
Select a Song: Choose a song that is well-known and suitable for a classroom setting. Avoid any song with inappropriate or offensive content.
Identify Variables: Determine at least 8 different variables that the user will provide to customize the song. These could include names, adjectives, nouns, places, etc.
Write the Function:
Define a function named custom_song that takes at least 8 parameters corresponding to the variables you've identified.
Use f-strings to incorporate these parameters into the song's lyrics.
Ensure the function prints the customized song lyrics.
Collect User Input:
Write code to collect user input for each of the 8 variables.
Use clear and descriptive prompts to guide the user.
Call the Function:
Call the custom_song function with the user inputs as named arguments.
Ensure the order of arguments matches the parameters in your function definition.
"""
def song():
    
    adjective = input("enter an adjective: ")
    adjective2 = input("enter another adjective: ")
    adjective3 = input("enter another adjective: ")
    weekday = input("enter a weekday: ")
    adjective4 = input("enter another adjective: ")
    adjective5 = input("enter another adjective: ")
    weekday2 = input("enter another weekday: ")
    pronoun = input("enter a pronoun: ")

    print(f"We're {adjective} away")
    print(f"I don't know what {pronoun}'s to {adjective2}")
    print(f"I'll {adjective2} it anyway")
    print(f"{weekday} another {weekday2} to find you")
    print(f" {adjective3} away")
    print(f"I'll be {adjective5} for your love, okay?")
    print(f"Take {adjective4} me")
    print(f"Take {adjective4} me")

song()