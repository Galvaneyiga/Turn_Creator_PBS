Turn creator v1.0
===============

_____
ABOUT

A small program originally written for use in Senran Kagura: Peach Beach Splash to help manage player rotation during events.

The program takes a total list of players, separates them into unique turns, and saves the output to a file (_out.txt by default).


__________
HOW TO USE

At the moment the can program only be run in Python.

To run the program from command prompt, access the folder containing the program, run main.py and specify the player file as the argument as follows:

	>> main.py [your_player_file] [optional_output_filename]

The behavior of the program can be modified by changing the values of parameters in config.txt:

	LOBBY_CREATOR_PREFERENCE    - a string that is checked when creating turns to mark players responsible for making lobbies in PBS. It can be anything as long as it's consistent between players. If you don't care about creator preference, you can set it as 0

    LOBBY_SIZE                  - any positive integer higher than zero

    OUTPUT_MODE                 - the format in which turns are output. 0 means turns will be output horizontally, which is the default output option; anything else will render turns vertically

See the comments in the code of main.py and turn_creator.py for more information.


_______
CREDITS

Written by FX in Python 3.11.1

Inspired by prettytail's ranked event player management
