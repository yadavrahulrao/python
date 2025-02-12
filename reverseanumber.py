#program to reverse a number 


def reverseNumber(number):
    if number == 0:
        return 0
    else:
        return (number % 10) * (10 ** (len(str(number)) - 1)) + reverseNumber(number // 10)

number = int(input("enter number : "))
reversedNumber = reverseNumber(number)
print("Original Number:",number )
print("Reversed Number:",reversedNumber)