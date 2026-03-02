import sys, os, yaml

#Constants
COLUMNS = 12
ROWS = 8

#Function to clean numeric user input
def validate(question: str, stop: int, start: int = 0):
    num = input(question)
    try:
        if not int(num)-1 in range(start, stop):
            raise IndexError
        return int(num)
    except:
        return validate("Invalid option, try again:\n", stop, start)

#Main editing function
def editMap():
    global name, map
    name = map
    print("Editing ./assets/maps/" + name + "/...")
    while True:
        match validate("Select an action:\n1) Edit map properties\n2) Edit tiles\n3) Exit\n", 3):
            case 1:
                while True:
                    map = "./assets/maps/"+name+"/mapproperties.yaml"
                    properties = yaml.safe_load(open(map, "r"))
                    attributes = {"columns": int, "rows": int, "xOffset": int, "yOffset": int, "tileKeys": bool, "tileSize": int, "entities": list}
                    print(f"\n{name}/mapproperties.yaml: \n{properties}")
                    match validate("Select an action:\n1) Edit/Add attribute\n2) Remove attribute\n3) Exit\n", 3):
                        case 1:
                            attribute = input("Which attribute do you want to edit?: ")
                            if attribute in attributes.keys():
                                value = eval(input("What do you want to set this attribute to?: "))
                                try:
                                    if type(value) == attributes[attribute]:
                                        properties[attribute] = value
                                        yaml.dump(properties, open(map, "w"), sort_keys=False)
                                    else:
                                        raise TypeError
                                except:
                                    print("Invalid attribute type.")
                            else:
                                print("That attribute does not exist!")
                        case 2:
                            attribute = input("Which attribute would you like to remove?: ")
                            if attribute in properties.keys() and not attribute in ["columns", "rows"]:
                                del properties[attribute]
                                yaml.dump(properties, open(map, "w"), sort_keys=False)
                            else:
                                print("Attribute does not exist or could not be removed.")
                        case _:
                            break
            case 2:
                while True:
                    map = open("./assets/maps/"+name+"/tiles.txt").read().split("\n")
                    print(f"\nassets/maps/{name}/tiles.txt:")
                    if map[0] == '':
                        print(None)
                        del map[0]
                    for i in range(len(map)):
                        print(f"{i+1}: {eval(map[i])}")
                    print("")
                    match validate("Select an action:\n1) Append tile\n2) Remove tile\n3) Duplicate tile\n4) Edit tile\n5) Exit\n", 5):
                        case 1:
                            appendTile()
                        case 2:
                            removeTile()
                        case 3:
                            dupeTile()
                        case 4:
                            editTile()
                        case _:
                            break
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
                    tile["col"] = validate("Enter the tile's column: ", 12)
                    tile["row"] = validate("Enter the tile's row: ", 8)
                else:
                    tile["col"] = 1
                    tile["row"] = eval(map[-1])["row"] + 1
            else:
                tile["col"] = eval(map[-1])["col"] + 1
                tile["row"] = eval(map[-1])["row"]
        else:
            tile["col"] = validate("Enter the tile's column: ", 12)
            tile["row"] = validate("Enter the tile's row: ", 8)
    else:
        tile["col"] = validate("Enter the tile's column: ", 12)
        tile["row"] = validate("Enter the tile's row: ", 8)
    tile["tileID"] = input("Enter the tile's ID: ")
    tile["tileIndex"] = validate("Enter the tile's index: ", 9)
    tile["collision"] = input("Does this tile have collision?(y/n): ") == "y"
    tile["flags"] = []
    for i in range(validate("Enter the amount of flags you want to add: ", 9, -1)):
        tile["flags"].append(validate(f"Enter flag {i+1}: ", 999, -1))
    map.append(str(tile))
    open("./assets/maps/"+name+"/tiles.txt", "w").write("\n".join(map))
    print("Appended", str(tile))

#Function for removing a tile from the map
def removeTile():
    if len(map):
        try:
            del map[int(input("Which tile do you want to remove: "))-1]
        except:
            print("Invalid tile")
        open("./assets/maps/"+name+"/tiles.txt", "w").write("\n".join(map))
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
                    tile["col"] = validate("Enter the new tile's column: ", 12)
                    tile["row"] = validate("Enter the new tile's row: ", 8)
                else:
                    tile["col"] = 1
                    tile["row"] = eval(map[-1])["row"] + 1
            else:
                tile["col"] = eval(map[-1])["col"] + 1
                tile["row"] = eval(map[-1])["row"]
            map.append(str(tile))
            open("./assets/maps/"+name+"/tiles.txt", "w").write("\n".join(map))
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
            match validate("Select an action:\n1) Change column/row\n2) Change tile ID\n3) Change tile index\n4) Edit collision\n5) Change flags\n6) Finish\n", 6):
                case 1:
                    tile["col"] = validate("Enter the tile's new column: ", 12)
                    tile["row"] = validate("Enter the tile's new row: ", 8)
                case 2:
                    tile["tileID"] = input("Enter the tile's new ID: ")
                case 3:
                    tile["tileIndex"] = validate("Enter the tile's new index: ", 9)
                case 4:
                    tile["collision"] = True if input("Does this tile have collision?(y/n): ") == "y" else False
                case 5:
                    match validate("Select an action:\n1) Append flag\n2) Edit flag\n3) Remove flag\n4) Back\n", 4):
                        case 1:
                            tile["flags"].append(validate(f"Enter the new flag: ", 999, -1))
                        case 2:
                            tile["flags"][validate("Which flag will you edit?: ", len(tile["flags"]))-1] = validate(f"Enter the new flag: ", 999, -1)
                        case 3:
                            del tile["flags"][validate("Which flag will you remove?: ", len(tile["flags"]))-1]
                        case _:
                            pass
                case _:
                    break
        print("Applying changes...")
        map[tileI] = str(tile)
        open("./assets/maps/"+name+"/tiles.txt", "w").write("\n".join(map))
            
#Main loop
while True:
    match validate("Select an action:\n1) Edit Map\n2) Create map\n3) Exit\n", 3):
        case 1:
            try:
                map = input("Enter the name of the map you want to edit:\n(Should be in ./assets/maps)\n")
                editMap()
            except:
                print("Editing failed, map file is likely corrupted")
        case 2:
            map = input("Enter a name for the map: ")
            try:
                os.makedirs(f"./assets/maps/{map}", exist_ok=False)
                open(f"./assets/maps/{map}/mapproperties.yaml", "x")
                open(f"./assets/maps/{map}/tiles.txt", "x")
                properties = {}
                properties["columns"] = validate("How many columns will the map have?: ", 999)
                properties["rows"] = validate("How many rows will the map have?: ", 999)
                properties["xOffset"] = 0
                properties["yOffset"] = 0
                properties["tileKeys"] = True
                properties["tileSize"] = 16
                properties["entities"] = []
                with open(f"./assets/maps/{map}/mapproperties.yaml", "w") as file:
                    yaml.dump(properties, file, sort_keys=False)
            except:
                print("An error occurred while creating map!")
            else:
                try:
                    editMap()
                except:
                    print("Editing failed, map file is likely corrupted")
        case _:
            print("Exiting...")
            sys.exit()