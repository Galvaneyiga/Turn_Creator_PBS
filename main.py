"""

    "main.py"

    The main executable program.
    To run it from a terminal (or command line), you want to pass an input file to it containing players and their respective tier. Please take example from sample_input.txt when creating your own player files.

    Here are examples of running the program from the terminal:

        main.py sample_input.txt        <- launches your program and loads sample_input.txt

        main.py pbs.txt myoutput.txt    <- launches your program and loads pbs.txt, and saves the output of the turns to myoutput.txt

        main.py                         <- without arguments, this doesn't work

    This program also loads config.txt, whose arguments you can also modify:

        LOBBY_CREATOR_PREFERENCE    <- a string that is checked when creating turns to mark players responsible for making lobbies in PBS. It can be anything as long as it's consistent between players. If you don't care about creator preference, you can set it as 0

        LOBBY_SIZE                  <- any positive integer higher than zero

        OUTPUT_MODE                 <- the format in which turns are output. 0 means turns will be output horizontally, which is the default output option; anything else will render turns vertically

    Please note that when modifying player file and config file that there must not be blank lines in between entries. If there are, the program will think that it reached the end of file and stops reading them completely.

    - FX
    09/02/2023

"""

import sys
import os
import turn_creator

# stuff
players = {}
player_turns = []
lobby_size = 4                  # default for 3v3 ranked
lobby_creator_preference = "0"  # default for no preference
output_mode = 0                 # output is horizontal by default
output_filename = "_out.txt"    # default name for the output file

# ____________________________________________________

def load_players(player_file_path):
    if(not os.path.exists(player_file_path)):
        print("Couldn't find the player file")
    else:
        player_file = open(player_file_path, "r")
        while(player_file):
            # separate player name and tier using ":"
            x = (player_file.readline()).rsplit(":")

            # break out of loop if line is empty
            if(len(x) <= 1):
                player_file.close()
                break
            elif(len(x) < 2 or len(x) > 2):
                continue
            x[0] = x[0].strip()
            x[1] = x[1].strip("\n\t ")

            # add player
            players[x[0]] = x[1]
    
        player_file.close()
        print("Successfully loaded players.")

def load_config():
    global lobby_size, lobby_creator_preference, output_mode

    config_file = open("config.txt")
    if(not config_file):
        print("Couldn't find the config file; sticking to default values")
    else:
        while(config_file):
            x = (config_file.readline()).rsplit(" ")
            if(len(x) <= 1):
                config_file.close()
                break

            if(x[0] == "LOBBY_SIZE"):
                lobby_size = int(x[1])
            if(x[0] == "LOBBY_CREATOR_PREFERENCE"):
                lobby_creator_preference = x[1].strip("\n\t ")
            if(x[0] == "OUTPUT_MODE"):
                output_mode = int(x[1].strip("\n\t "))

    config_file.close()
    print("Successfully loaded configuration.")

def write_to_file(turns):
    out = open(output_filename, "w")
    for i in range(len(turns)):
        out.write(turns[i])
    out.close()


# ____________________________________________________

# check if arguments are provided to the program
if(len(sys.argv) > 1):
    # rename the output file if specified
    if(len(sys.argv) > 2):
        output_filename = sys.argv[2]
    
    # load the player file
    load_players(sys.argv[1])
    
    # if player file processed successfully, load everything else
    if(bool(players)):
        load_config()
        
        # create player turns
        player_turns = turn_creator.create(players, lobby_size, lobby_creator_preference, output_mode)
        
        # write player turns to console
        #turn_creator.print_turns(player_turns, output_mode)
        
        # write player turns to file
        write_to_file(turn_creator.output_turns(players, player_turns, lobby_creator_preference, output_mode))

else:
    print("Player file missing. Please provide one.")
