import sys

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
        map = open("./assets/maps/"+name+".map").read()
        print(f"{name}.map:\n{map}")
        match validate(input("Select an action:\n1) Append tile\n2) Remove last tile\n3) Duplicate last tile\n4) Exit\n"), range(4)):
            case 1:
                id = input("Enter the tile's id: ")
                index = str(validate(input("Enter the tile's index: "), range(9)))
                layer = input("Enter the tile's layer: ")
                tileid = f"{id};{index};{layer} "
                if map != "" and map[-1] != " ":
                    tileid = " " + tileid
                open("./assets/maps/"+name+".map", "a").write(tileid)
                print("Appended", tileid)
            case 2:
                try:
                    while map[-1] != ";": map = map[:-1]
                    while map[-1] != " ": map = map[:-1]
                except:
                    pass
                open("./assets/maps/"+name+".map", "w").write(map)
                print("Removed last tile")
            case 3:
                foundID = False
                for i in range(1, len(map)+1):
                    print(i)
                    print(map[-i])
                    if not foundID and map[-i] != " ":
                        foundID = True
                    elif foundID and map[-i].isalpha():
                        open("./assets/maps/"+name+".map", "a").write(map[-i:])
                        break
            case _:
                return

while True:
    match validate(input("Select an action:\n1) Edit Map\n2) Create map\n3) Exit\n"), range(3)):
        case 1:
            editMap(input("Enter the name of the map you want to edit:\n(Should be in ./assets/maps)\n"))
        case 2:
            new = input("Enter a name for the file: ")
            try:
                open(f"./assets/maps/{new}.map", "x")
                editMap(new)
            except:
                print("That name is invalid or a map with that name already exists!")
        case _:
            print("Exiting...")
            sys.exit()