import json, time
from packages.dprint import dprint


def space():
    print("\n" * 5)
    return

print("Welcome to the Python Story Player!\nThis is a script designed to be able to load game files in the .json format.\nSorry for the fact that text does not disappear after you have chosen a response, this is sadly not fixable with the current IDLE build installed on these computers.\nThe text wrapping is also extremely annoying, the IDLE window does not wrap by word but by character.  This is also unfixable.")

# keeps asking for a valid .json file until one is provided
while True:
    file = input("Specify the game file you want to open (include any file extensions): ")
    print("Loading and parsing game file...")

    try:
        # attempts to load the provided file
        data = json.load(open("games/" + file))
    except FileNotFoundError:
        print("Cannot find specified file.  Make sure you have the name correct.")
    else:
        break
    # NOTE: i did not include an exception for any errors with the JSON file
    # because if a gamefile doesn't work, it probably means it is in development
    # and therefore it is nice to have the extra information provided with
    # regular error messages.
while True:
    print(file + " successfully loaded!\nEnjoy the game!")
    space()
    time.sleep(1)

    dictionary = data
    move = False

    while True:
        # if they are available, assign dictionary options to list 'options'
        try:
            options = dictionary['opts']
        except:
            # if not, check if it contains any redirections
            try:
                goto = dictionary['goto']
            except:
                # if there are no options or redirections
                dprint(dictionary["text"] + "\n\n")
                dprint("The end!")
                break
            else:
                # if there is a redirection, print the text and enable moving
                dprint(dictionary["text"] + "\n")
                move = True
        if move:
            # reset the dictionary to the root, and then increase the level, using
            # the goto list supplied by the loaded json
            moveLength = len(goto)
            dictionary = data
            for i in range(moveLength):
                dictionary = dictionary[goto[i]]
            # set move to false to prevent infinite moving, also redefine options to
            # match new dictionary
            move = False
            options = dictionary['opts']

        # print the text
        dprint(dictionary['text'] + '\n')
        # keep checking for a response until a valid one is provided
        while True:
            response = input()
            if response.lower() in options:
                print("\n")
                break
            else:
                dprint("Invalid response, please choose either " + options[0] + " or " + options[1] + ".\n")
        # elevate dictionary level to the response
        dictionary = dictionary[response.lower()]
    # asks to play again until valid answer given
    while True:
        playAgain = input("\n\nPlay again (y/n)? ")
        if playAgain.lower() == "y":
            print("Reloading " + file + "...")
            data = json.load(open("games/" + file))
            break
        elif playAgain == "n":
            exit()
        else:
            print("That is not a valid option.  Please type either 'y' or 'n'")
        
