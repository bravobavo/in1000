input("Far, far, far...\nIn the woods of a farmer...\n"+
      "A sly fox lurks from underneath the many trees.....")
input("Ready to kill!")
print("Your goal is to stop the fox from killing all your precious chickens...")
help = input("Are you ready? (y/help)\n")
if help == "h" or help =="help":
    with open("help.txt","r") as helpTxt:
        lines = helpTxt.readlines()
        i = 0
        while i < len(lines):
            print(lines[i].rstrip("\n"))
            i += 1
