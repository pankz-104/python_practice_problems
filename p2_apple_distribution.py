# harry has got n number of apples. Harry has some student among whom, he wants to distribute the
# apples. These n numbers of apples are provided to harry by his friends and he can request for few more or few
# less apples.
#
# You need to print whether a number in range mn to mx is a divisor or not.
#
# Input :: Take input n, mn and mx from the user
#
# output :: print whether the number between mn and mx are divisor of n or not
#
# Example :
# If n is 20 and mn = 2 and mx = 5
# 2 is a divisor of 20
# 3 is not a divisor of 20
# 4 is a divisor of 20
# 5 is a divisor of 20

n = int(input("Enter the number of apples: "))
mn = int(input("Enter the min range value: "))
mx = int(input("Enter the max range value: "))

if mx < mn:
    print("Unspecific range value given: ")
else:
    for i in range(mn, mx+1):
        if(n % i) == 0:
            print(f"{i} is divisor of {n}")
        else:
            print(f"{i} is not a divisor of {n}")
