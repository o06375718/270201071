def anagram(s1,s2):
    s_l=[]
    s_l_2=[]
    for word in s1:
        s_l.append(word)
    for words in s2:
        s_l_2.append(words)
    s_l.sort()
    s_l_2.sort()
    if s_l ==s_l_2:
          print("They are anagram")
    else :
        print("They are not anagram")

s1=input("Enter a string")
s2=input("Enter a string")
print(anagram(s1,s2))