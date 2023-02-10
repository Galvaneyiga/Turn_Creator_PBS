"""

    "turn_creator.py"

    Use the following functions when interacting with the turn creator:

    * print_turns(collection, mode)
        > prints the provided collection of turns to the screen
        > mode can be changed to view turns horizontally (0, default) or vertically (any other value)

    * create(player_dictionary, lobby_size, lobby_creator_preference)
        > creates a new collection of turns from the provided arguments
        > won't do anything if the player dictionary is empty or the lobby size is 0
        > the default value of lobby creator preference is "0", meaning it won't compute preference if the argument is not provided
    
    * output_turns(collection, mode)
        > returns the list of strings instead of printing to the console, which can be passed around
        > it contains redundant code but I'm too lazy to change that at the moment :P

    - FX
    09/02/2023

"""


import itertools

test_players = {
    "Player A"      : "Master",
    "Player B"      : "1st",
    "Player C"      : "1st",
    "Player D"      : "2nd",
    "Player E"      : "2nd",
    "Player F"      : "3nd",
    "Player G"      : "4th"

}

# ____________________________________________________

# private functions

def _print_turn_horizontal(collection_filtered, index):
    print("Turn " + str(index+1) + ": ", end=" ")
    for i in range(len(collection_filtered[index])):
        if(i == len(collection_filtered[index])-1):
            print(collection_filtered[index][i])
        else:
            print(collection_filtered[index][i], end=", ")

def _print_turn_vertical(collection_filtered, index):
    print("Turn " + str(index+1))
    for i in range(len(collection_filtered[index])):
        print(str(i+1) + ". " + collection_filtered[index][i])
    print()

def _gen_unfiltered_turns(player_dict):
    print("Found " + str(len(player_dict)) + " players. Collecting permutations...")
    collection = list(itertools.permutations(list(player_dict.keys())))

    return collection

def _filter_turns(collection, lobby_size):
    collection_filtered = []
    blacklist = []
    elem = []
    print("Shrinking and sorting results...")
    i = 0
    while(i < len(collection)):
        elem = list(collection[i])[0:lobby_size]
        elem.sort()
        if elem not in blacklist:
            collection_filtered.append(elem)
            blacklist.append(elem)
        i += 1
    
    collection_filtered.sort()
    
    return collection_filtered

def _apply_preference(players, collection_filtered, lobby_creator_preference):
    # don't do anything to the collection if pref is 0
    if(str(lobby_creator_preference) == "0"):
        return collection_filtered

    print("Adding lobby creator preference... " + "(" + lobby_creator_preference + ")")
    for i in range(len(collection_filtered)):
        for j in range(len(collection_filtered[i])):
            if(players[collection_filtered[i][j]] == lobby_creator_preference):
                collection_filtered[i][j] += "*"
    
    return collection_filtered


# public functions

# print turns to the console
def print_turns(collection_filtered, mode=0):
    # do nothing if the collection is empty
    if(not bool(collection_filtered)):
        return

    # print based on mode
    print()
    if(mode == 0):
        for i in range(len(collection_filtered)):
            _print_turn_horizontal(collection_filtered, i)
    else:
        for i in range(len(collection_filtered)):
            _print_turn_vertical(collection_filtered, i)

# output turns as a list of strings
def output_turns(collection_filtered, mode=0):
    # do nothing if the collection is empty
    if(not bool(collection_filtered)):
        return
    
    output = []
    
    if(mode == 0):
        # horizontal mode output
        for h in range(len(collection_filtered)):
            output.append("Turn " + str(h+1) + ": ")
            for i in range(len(collection_filtered[h])):
                if(i == len(collection_filtered[h])-1):
                    output.append(collection_filtered[h][i] + "\n")
                else:
                    output.append(collection_filtered[h][i] + ", ")
    else:
        # vertical mode output
        for h in range(len(collection_filtered)):
            output.append("Turn " + str(h+1) + "\n")
            for i in range(len(collection_filtered[h])):
                output.append(str(i+1) + ". " + collection_filtered[h][i] + "\n")
            output.append("\n")
        
    return output

def create(player_dict, lobby_size, lobby_creator_pref = "0"):
    if(not bool(player_dict)):
        print("The player dictionary is empty.")
        return dict()
    
    if(lobby_size <= 0):
        print("Invalid lobby size.")
        return dict()

    # compute permutations of players, filter results, then apply lobby creator preference
    final_collection = _apply_preference(player_dict,
    _filter_turns(
    _gen_unfiltered_turns(player_dict), lobby_size), lobby_creator_pref)
    
    return final_collection
    
# ____________________________________________________


# >> tests (debug use only) <<
#print_turns(create(dict(), 4))
#print()
#print_turns(create(test_players, 0))
#print()
#print_turns(create(test_players, 6, "1st"))
