#Write a program to print out all Armstrong numbers between 1 and 500. 
# If sum of cubes of each digit of the number is equal to the number itself, 
# then the number is called an Armstrong number. For example, 153 = (1*1*1)+(5*5 *5)+(3*3*3)


for n in range(1,501):

#n=int(input("Enter the number :-"))
    original=n
    sum=0

    digits=len(str(n))

    while n > 0:
        digit = n % 10  # Get the last digit
        power = digit ** digits
        sum = sum + power
        n = n // 10
    if sum == original:
        print(original)