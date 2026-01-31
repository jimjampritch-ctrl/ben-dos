import time

# boot 
print("booting bios")
time.sleep(1)
print("loading firmware")
time.sleep(1)
print("loading os")
time.sleep(1)
print("loading files")
time.sleep(1)
print("ben dos open beta")
print("=================")
print("type help for commands:")

# functions
def helpc():
    print("commands: help, exit, calc, ver, sysinfo, game")

def calcc():
    val1 = input("val1")
    val2 = input("val2")
    finval = val1+val2
    print("""
    """)
    print (finval)

def verc():
    print(" ")
    print("version open beta")
 
def sysc():
    print("ram:16mb")
    print("hdd:32gb")
    print("os version open beta")

def gamec():
    hp = 100
    while loop == 1:
        print("\n=== ben quest ===")
        print("hp:", hp)
        action = input("What do you do? 1.walk 2.chop a tree 3.quit: ")
        
        if action == "1":
            hp -= 10
            print("You walked and lost 10 HP!")
        elif action == "2":
            print("You built a house!")
        elif action == "3":
            print("Exiting game...")
            break
        else:
            print("Invalid action. Choose 1, 2, or 3.")
        if hp == 0:
            print("game over")
            break

# loop
loop = 1
while loop == 1:
    cmd = input("c:>")
    if cmd == "help":
        helpc() 
    elif cmd == "ver":
          verc() 
    elif cmd == "calc":
          calcc()
    elif cmd == "sysinfo":
          sysc()
    elif cmd == "game":
        gamec()
    elif cmd == "exit":
          print("ben dos is shutting down")
          time.sleep(1)
          print("stoping proseses")
          time.sleep(1)
          print("quiting session")
          time.sleep(1)
          break
    else:
        print("uknown command")
