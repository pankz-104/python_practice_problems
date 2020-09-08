print("Enter the numbers of item in list\n")
size = int(input("Enter size of list\n"))
# initialize a blank list
mylist = []
for i in range(size):
    mylist.append(int(input("Enter list items \n ")))

reverse1 = mylist[:]
reverse1.reverse()
print(f"My first reversed list is {reverse1}")

# second method
reverse2 = mylist[::-1]
print(f"second list is {reverse2}")

# swapping elements

# a,b = b,a
reverse3 = mylist[:]
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(mylist)-i-1] = reverse3[len(mylist)-i-1], reverse3[i]
print(f"Third list is {reverse3}")

if reverse1 == reverse2 and reverse2 == reverse3:
    print("same result")
