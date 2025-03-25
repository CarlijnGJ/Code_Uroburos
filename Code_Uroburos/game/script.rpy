# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Felicity")


# The game starts here.

label start:

    scene bg room

    # Use the default character speaking
    "Hello, I will talk in typewriter style now."

    # Show text with a typewriter effect
    window hide

    show screen computer("Can")
    $ renpy.pause(0.5)
    show screen computer("Can you")
    $ renpy.pause(0.5)
    show screen computer("Can you read")
    $ renpy.pause(0.5)
    show screen computer("Can you read this?")
    $ renpy.pause()

    show screen computer("Are")
    $ renpy.pause(0.5)
    show screen computer("Are we")
    $ renpy.pause(0.5)
    show screen computer("Are we connected?")
    $ renpy.pause()

    return

screen computer(message):
    text _(message) xalign 0.5 yalign 0.5
