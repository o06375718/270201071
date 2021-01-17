def password_checker(n):
 def get_password_level(n):
  level = 0
  letters = 0
  numbers = 0
  specials = 0


  if  " " in n or len(n) < 8 :
    return(level)

   for char in n:
      if char.isalpha():
        letters += 1
      elif char.isnumeric():
         numbers += 1
      else:
         specials += 1

    if letters > 0:
       level += 1
    if numbers > 0:
      level += 1
    if specials > 0:
       level += 1
    return(level)

def main():
  pw = input("Enter password: ")
  print("Security level:", get_password_level(pw))

main()

