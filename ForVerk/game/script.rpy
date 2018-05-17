# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Analog Music Snob")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "(I see someone approaching)"

    "(As he comes closer I see it's this hipster I go to class with)"

    "(After practically sprinting towards me, he seem's out of breath)"

    "(I see him start to open his mouth)"

    m "Hey you, yeah you! I'm talking to you!"

    "Huh?"

    m "Do you know how much better analog is than digital?"

    "N-"

    m "Pfft -Don't get me started on these garbage streaming platforms."

    "(I don't recall asking)"

    "I-"

    m "Do you like Kate Bush?"

    "(What?)"

    menu:
        "Yeah, love her":
            jump choice1_yes

        "Vinyl is overrated":
            jump choice1_no

    label choice1_yes:
        $ menu_flag = True

        m "Cool, but have you heard her music on vinyl??"

        "(This guy just doesn't shut up, does he?)"

        menu:
            "Vinyl is overrated":
                jump choice1_no

    label choice1_no:
        $ menu_flag = False

        "(The Music Snob squirms in pain, not sure how to respond, fumbling over his own words)"

        "(It's super effective)"

        jump choice1_cont

    label choice1_done:

    # This ends the game.

    label choice1_cont:

        "(Where was I going again?)"

        "(That hipster really threw off my train of thought)

        

    return
