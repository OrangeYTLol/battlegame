import sys

COLUMNS = 12
ROWS = 8
LAYERS = 3

def validate(string, cap):
    try:
        if not int(string)-1 in cap:
            raise IndexError
    except:
        return validate(input("Invalid option, try again:\n"), cap)
    else:
        return int(string)
def editMap(map):
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
                tile["layer"] = validate(input("Enter the tile's layer: "), range(LAYERS))
                tile["flags"] = []
                for i in range(validate(input("Enter the amount of flags you want to add: "), range(-1, 9))):
                    tile["flags"].append(validate(input(f"Enter flag {i+1}: "), range(-1, 999)))
                map.append(str(tile))
                open("./assets/maps/"+name+".map", "w").write("\n".join(map))
                print("Appended", str(tile))
            case 2:
                if len(map):
                    try:
                        del map[int(input("Which tile do you want to remove: "))-1]
                    except:
                        print("Invalid tile")
                    open("./assets/maps/"+name+".map", "w").write("\n".join(map))
                else:
                    print("There are no tiles to remove!")
            case 3:
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
            case 4:
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
                        match validate(input("Select an action:\n1) Change column/row\n2) Change tile ID\n3) Change tile index\n4) Change layer\n5) Change flags\n6) Finish\n"), range(6)):
                            case 1:
                                tile["col"] = validate(input("Enter the tile's new column: "), range(12))
                                tile["row"] = validate(input("Enter the tile's new row: "), range(8))
                            case 2:
                                tile["tileID"] = input("Enter the tile's new ID: ")
                            case 3:
                                tile["tileIndex"] = validate(input("Enter the tile's new index: "), range(9))
                            case 4:
                                tile["layer"] = validate(input("Enter the tile's new layer: "), range(LAYERS))
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
            case _:
                print("Closing map...")
                return

while True:
    match validate(input("Select an action:\n1) Edit Map\n2) Create map\n3) Exit\n"), range(3)):
        case 1:
            try:
                editMap(input("Enter the name of the map you want to edit:\n(Should be in ./assets/maps)\n"))
            except:
                print("Editing failed, map file is likely corrupted")
        case 2:
            new = input("Enter a name for the file: ")
            try:
                open(f"./assets/maps/{new}.map", "x")
            except:
                print("That name is invalid or a map with that name already exists!")
            else:
                try:
                    editMap(new)
                except:
                    print("Editing failed, map file is likely corrupted")
        case _:
            print("Exiting...")
            sys.exit()