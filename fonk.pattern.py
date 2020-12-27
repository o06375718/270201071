x=10
for i in range(1,x+1):
    for j in range(1,i+1):
      print("* ",end="")
    print("\r")
for i in range(x+1,0,-1):
     for j in range(0,i):
      print("* ",end="")
     print("\r")
def pattern(x):
  x=10
  for i in range(1,x+1):
      for j in range(1,i+1):
        print("* ",end="")
      print("\r")
  for i in range(x+1,0,-1):
      for j in range(0,i):
        print("* ",end="")
      print("\r")
pattern(10)