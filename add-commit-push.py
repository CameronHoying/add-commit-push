import os
import sys

print("testing")
numOfArgs = len(sys.argv)
print("Total Arguments Passed: ", numOfArgs)
message = "Update files"
if numOfArgs == 3:
    if sys.argv[1] == "-m":
        print("Number of args = 3 and p2 = -m")
        message = sys.argv[2]

print (message) 



print ("add-commit-push")
print("\ngit status")
os.system("git status")

#w3c schools code
if numOfArgs != 2:
    print("Do you want to continue with add commit push? (y):")
    confirm = input()
    if confirm != "y":
        print("canceling", confirm)
        quit()

print("\ngit add -A")
os.system("git add -A")

commitStatement = '\ngit commit -m "' + message + '"'
print(commitStatement)
os.system(commitStatement)

print("\ngit push")
os.system ("git push")
