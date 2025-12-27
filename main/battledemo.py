import random
import time

player = {
    "name" : "Player",
    "hp" : 10,
    "maxhp" : 10,
    "def" : 0,
    "atk" : 1,
    "magic" : 4,
    "exp" : 0,
    "lv" : 0
}
DELAY = 0

def loadEnemies():
    global enemies
    virus = { 
        "name" : "Virus",
        "hp" : 10, 
        "maxhp" : 10,
        "def" : 0,
        "exp" : 5,
        "atks" : {
            "atk1" : {
                "name" : "Byte",
                "dmg" : 2
            },
            "atk2" : {
                "name" : "Bit Flip",
                "dmg" : 1
            }
        }
    }
    malware = { 
        "name" : "Malware",
        "hp" : 10, 
        "maxhp" : 10,
        "def" : 0,
        "exp" : 10,
        "atks" : {
            "atk1" : {
                "name" : "Data Steal",
                "dmg" : 2
            },
            "atk2" : {
                "name" : "Encryption",
                "dmg" : 3
            }
        }
    }
    trojan = { 
        "name" : "Trojan",
        "hp" : 20, 
        "maxhp" : 20,
        "def" : 0,
        "exp" : 20,
        "atks" : {
            "atk1" : {
                "name" : "Slowdown",
                "dmg" : 1
            },
            "atk2" : {
                "name" : "Data Steal",
                "dmg" : 2
            },
            "atk3" : {
                "name" : "Backdoor",
                "dmg" : 4
            }
        }
    }
    wannacry = { 
        "name" : "WANNACRY",
        "hp" : 200, 
        "maxhp" : 200,
        "def" : 0,
        "exp" : 100,
        "atks" : {
            "atk1" : {
                "name" : "Slowdown",
                "dmg" : 10
            },
            "atk2" : {
                "name" : "Encryption",
                "dmg" : 15
            },
            "atk3" : {
                "name" : "Backdoor",
                "dmg" : 20
            },
            "atk4" : {
                "name" : "Spread",
                "dmg" : 25
            }
        }
    }
    enemies = [virus, malware, trojan, wannacry]
    
def validate(string, cap):
    try:
        if not int(string)-1 in cap:
            raise IndexError
    except:
        return validate(input("Invalid option, try again:\n"), cap)
    else:
        return int(string)

def showStats(entity, stat):
    match stat:
        case "health":
            print(entity["name"], "HP:", entity["hp"], "/", entity["maxhp"])
        case "check":
            print(entity["name"], "HP:", entity["hp"], "/", entity["maxhp"])
            print(entity["name"], "ATK:", entity["atk"])
            print(entity["name"], "DEF:", entity["def"])
        case "all":
            print("HP:", entity["hp"], "/", entity["maxhp"])
            print("ATK:", entity["atk"])
            print("DEF:", entity["def"])
            print("Magic:", entity["magic"])
            print("EXP:", entity["exp"])

def addEXP(eexp):
    global health, defense, attack, magic, exp
    player["exp"] += eexp
    print("You gained", eexp, "EXP")
    player["maxhp"] += eexp // 2
    print("Your HP were increased by", eexp // 2)
    player["atk"] += eexp // 2
    print("Your ATK was increased by", eexp // 2)
    player["def"] += eexp // 5
    print("Your DEF was increased by", eexp // 5)
    player["magic"] += eexp // 4
    print("Your Magic was increased by", eexp // 4)

def battle(enemy):
    global player
    ename = enemy["name"]
    patk = player["atk"]
    pmagic = player["magic"]
    
    print("\n"+ename, "appeared!\n")
    time.sleep(DELAY)
    while True:
        action = validate(input("Select an action:\n1) Fight\n2) Heal\n3) Flee\n"), range(3))
        match action:
            case 1:
                print("\nDealt", patk, "damage to", ename+"!")
                enemy["hp"] -= patk
                if enemy["hp"] < 1:
                    print(ename, "has been defeated!\n")
                    addEXP(enemy["exp"])
                    print("")
                    break
                print("")
                time.sleep(DELAY)
            case 2:
                print(f"\nYou healed", pmagic, "HP.\n")
                player["hp"] += pmagic
                if player["hp"] > player["maxhp"]:
                    player["hp"] = player["maxhp"]
                time.sleep(DELAY)
            case 3:
                print("\nYou tried to flee...")
                if random.randint(0, 3) == 2:
                    print("and did!\n")
                    break
                else:
                    print("but couldn't!\n")
                    time.sleep(DELAY)
                
        atk = random.choice(list(enemy["atks"]))
        atkdmg = enemy["atks"][atk]["dmg"]
        
        print(ename, "used", enemy["atks"][atk]["name"]+"!")
        print("You took", atkdmg, "damage!")
        player["hp"] -= atkdmg
        if player["hp"] < 1:
            print("You were defeated!\n")
            break
        print("")
        
        time.sleep(DELAY)
        showStats(player, "health")
        showStats(enemy, "health")
        print("")
        time.sleep(DELAY)
        
while True:
    match validate(input("Select an action:\n1) Battle\n2) Check stats\n3) End\n"), range(3)):
        case 1:
            loadEnemies()
            enemy = validate(input("Pick an enemy(1 - 3): "), range(len(enemies)))
            battle(enemies[enemy - 1])
            if player["hp"] < player["maxhp"] // 2:
                player["hp"] = player["maxhp"] // 2
        case 2:
            print("")
            showStats(player, "all")
            print("")
            time.sleep(DELAY)
        case 3:
            if input("Are you sure? (y/n): ").lower().strip() == "y":
                time.sleep(DELAY)
                break