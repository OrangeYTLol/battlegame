import sys

#Constants
COLUMNS = 12
ROWS = 8

#Function to clean numeric user input
def validate(string, cap):
    try:
        if not int(string)-1 in cap:
            raise IndexError
    except:
        return validate(input("Invalid option, try again:\n"), cap)
    else:
        return int(string)

#Main editing function
def editMap():
    global name, map
    print("Editing " + map + ".map...")
    name = map
    while True:
        map = open("./assets/maps/"+name+".map").read().split("\n")
        print(f"\n{name}.map:")
        if map[0] == '':
            print(None)
            del map[0]
        for i in range(len(map)):
            print(f"{i+1}: {eval(map[i])}")
        print("")
        match validate(input("Select an action:\n1) Append tile\n2) Remove tile\n3) Duplicate tile\n4) Edit tile\n5) Exit\n"), range(5)):
            case 1:
                appendTile()
            case 2:
                removeTile()
            case 3:
                dupeTile()
            case 4:
                editTile()
            case _:
                print("Closing map...")
                return
                
#Function for appending a tile to the end of the map
def appendTile():
    tile = {}
    if len(map):
        if input("Is this tile sequential to the previous tile?(y/n): ") == "y": 
            if eval(map[-1])["col"] == COLUMNS:
                if eval(map[-1])["row"] == ROWS:
                    print("This tile cannot be sequential.")
                    tile["col"] = validate(input("Enter the tile's column: "), range(12))
                    tile["row"] = validate(input("Enter the tile's row: "), range(8))
                else:
                    tile["col"] = 1
                    tile["row"] = eval(map[-1])["row"] + 1
            else:
                tile["col"] = eval(map[-1])["col"] + 1
                tile["row"] = eval(map[-1])["row"]
        else:
            tile["col"] = validate(input("Enter the tile's column: "), range(12))
            tile["row"] = validate(input("Enter the tile's row: "), range(8))
    else:
        tile["col"] = validate(input("Enter the tile's column: "), range(12))
        tile["row"] = validate(input("Enter the tile's row: "), range(8))
    tile["tileID"] = input("Enter the tile's ID: ")
    tile["tileIndex"] = validate(input("Enter the tile's index: "), range(9))
    tile["collision"] = True if input("Does this tile have collision?(y/n): ") == "y" else False
    tile["flags"] = []
    for i in range(validate(input("Enter the amount of flags you want to add: "), range(-1, 9))):
        tile["flags"].append(validate(input(f"Enter flag {i+1}: "), range(-1, 999)))
    map.append(str(tile))
    open("./assets/maps/"+name+".map", "w").write("\n".join(map))
    print("Appended", str(tile))

#Function for removing a tile from the map
def removeTile():
    if len(map):
        try:
            del map[int(input("Which tile do you want to remove: "))-1]
        except:
            print("Invalid tile")
        open("./assets/maps/"+name+".map", "w").write("\n".join(map))
    else:
        print("There are no tiles to remove!")

#Function for duplicating a tile on the map
def dupeTile():
    if len(map):
        try:
            tile = eval(map[int(input("Which tile do you want to duplicate: "))-1])
        except:
            print("Invalid tile")
        else:
            if eval(map[-1])["col"] == COLUMNS:
                if eval(map[-1])["row"] == ROWS:
                    tile["col"] = validate(input("Enter the new tile's column: "), range(12))
                    tile["row"] = validate(input("Enter the new tile's row: "), range(8))
                else:
                    tile["col"] = 1
                    tile["row"] = eval(map[-1])["row"] + 1
            else:
                tile["col"] = eval(map[-1])["col"] + 1
                tile["row"] = eval(map[-1])["row"]
            map.append(str(tile))
            open("./assets/maps/"+name+".map", "w").write("\n".join(map))
    else:
        print("There are no tiles to duplicate!")

#Function for editing a tile
def editTile():
    try:
        tileI = int(input("Which tile do you want to edit: "))-1
    except:
        print("Invalid tile")
    else:
        print(f"Editing tile {tileI+1}...")
        tile = eval(map[tileI])
        while True:
            print(tile)
            print("")
            match validate(input("Select an action:\n1) Change column/row\n2) Change tile ID\n3) Change tile index\n4) Edit collision\n5) Change flags\n6) Finish\n"), range(6)):
                case 1:
                    tile["col"] = validate(input("Enter the tile's new column: "), range(12))
                    tile["row"] = validate(input("Enter the tile's new row: "), range(8))
                case 2:
                    tile["tileID"] = input("Enter the tile's new ID: ")
                case 3:
                    tile["tileIndex"] = validate(input("Enter the tile's new index: "), range(9))
                case 4:
                    tile["collision"] = True if input("Does this tile have collision?(y/n): ") == "y" else False
                case 5:
                    match validate(input("Select an action:\n1) Append flag\n2) Edit flag\n3) Remove flag\n4) Back\n"), range(4)):
                        case 1:
                            tile["flags"].append(validate(input(f"Enter the new flag: "), range(-1, 999)))
                        case 2:
                            tile["flags"][validate(input("Which flag will you edit?: "), range(len(tile["flags"])))-1] = validate(input(f"Enter the new flag: "), range(-1, 999))
                        case 3:
                            del tile["flags"][validate(input("Which flag will you remove?: "), range(len(tile["flags"])))-1]
                        case _:
                            pass
                case _:
                    break
        print("Applying changes...")
        map[tileI] = str(tile)
        open("./assets/maps/"+name+".map", "w").write("\n".join(map))
            

#Main loop
while True:
    match validate(input("Select an action:\n1) Edit Map\n2) Create map\n3) Exit\n"), range(3)):
        case 1:
            try:
                map = input("Enter the name of the map you want to edit:\n(Should be in ./assets/maps)\n")
                editMap()
            except:
                print("Editing failed, map file is likely corrupted")
        case 2:
            map = input("Enter a name for the file: ")
            try:
                open(f"./assets/maps/{map}.map", "x")
            except:
                print("That name is invalid or a map with that name already exists!")
            else:
                try:
                    editMap()
                except:
                    print("Editing failed, map file is likely corrupted")
        case _:
            print("Exiting...")
            sys.exit()