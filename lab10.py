####### Basic Multiplication ########
#f(n) =3*n
#f(0)=0
#f(n-1)=3n-3
#f(n)=f(n-1)+3
def multiple(n):
  if n==0:
    return 0
  else :
    return multiple(n-1)+3
print(multiple(6))

####### Hailstone ################
def hailstone(n):
  if n==1:
     print(1)
  else:
    print(n)
    if n%2==0:
      hailstone(n//2)
    else:
      hailstone((3*n)+1)
print(hailstone(5))

########### Hailstone ###########
def function(a_list):
    b=0
    for i in range(len(a_list)):
        if isinstance(a_list[i],list):
            for j in range(len(a_list[i])):
                b+=a_list[i][j]
        else:
            b+=a_list[i]
    return b
print(function([3,12,76,[4,56,43],[2,8],81,75]))

def sum_of_nested_list(x):
    if len(x)==0:
        return 0
    else:
        if isinstance(x,list):
            return sum_of_nested_list(x[0]) + sum_of_nested_list(x[1:])
        else :
            return sum_of_nested_list(x)[0]+sum_of_nested_list(x)[1:]

###### Pascal Triangle ########
def pascal_triangle_line(n):
 if n == 1:
    return [1]
 else:
    line = [1]
    previous_line = pascal_triangle_line(n-1)
    for i in range(len(previous_line)-1):
        line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line

print(pascal_triangle_line(6))