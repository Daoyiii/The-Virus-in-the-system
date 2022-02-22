# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("System")
define b = Character("Virus")
define c = Character("You")
define d = Character("Narrator")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    a "The system was restarted due to an unknown error - error code (26387412)"
    scene restarting
    a "Restarting system please don't close your pc"
    scene pause
    scene 1
    a "Unexpected error has occured unable to restart the system"
    #the screen turns from default blue to red/black
    scene hacked
    b "The system was succesfully blocked"
    b "Hahah the system was successfully eliminated"
    # This ends the game.

    return
