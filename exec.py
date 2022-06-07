import os

# os.system("xdotool key Alt+F10") REMOVE COMMENT BEFORE PUSHING
os.system("clear")

cmd = input("command: ")
spl = cmd.split(" ")
# print(spl[1])
spl2 = spl[1].split(".")
# print(spl2)
fileName = spl2[0]
ext = spl2[1]

print(fileName)
print(ext)


def Xqtr(fileName, ext):
    if ext == 'c':
        print("This is c")
        os.system(f"gcc {fileName}.c")
        os.system("./a.out")
    elif ext == 'py':
        print("This is Python")
        os.system(f"python3 {fileName}.py")
    elif ext == 'java':
        print("this is java")
    elif ext == 'cpp':
        print("This is C++")
        os.system(f"g++ {fileName}.cpp")
        os.system("./a.out")
    else:
        print("ProDriverX does not support that Language currently")


Xqtr(fileName, ext)
