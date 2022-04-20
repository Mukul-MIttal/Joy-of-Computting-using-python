'''
str1=input("Enter the first string")
str2=input("Enter the second string")
count1=0
i=0
while(i<len(str1)):
    count1=count1+ord(str1[i])
    i=i+1
count2=0
i=0
while(i<len(str2)):
    count2=count2+ord(str2[i])
    i=i+1
if(count1==count2):
    print("These are Anagrams")
else:
    print("These are not Anagram")
'''
str1=input("Enter the first string")
str2=input("Enter the second string")
temp=sorted(str1)
temp2=sorted(str2)
if(temp==temp2):
    print("These are Anagrams")
else:
    print("These are not Anagram")