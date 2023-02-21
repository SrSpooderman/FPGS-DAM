try:
    f = open("def2.py", "r")
except:
    print("err")

for num_line in range(0, len(f)):
    line = f.readline()
    print(num_line, line, end="")
    
f.close()