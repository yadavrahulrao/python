# checking the interger is palindrome or not 


def reverseNumber(number):
    if number == 0:
        return 0
    else:
        return (number % 10) * 10 ** (len(str(number)) - 1) + reverseNumber(number // 10)
number = int(input("enter number : "))
reversedNumber = reverseNumber(number)
def palindrome(number):
    if number == reversedNumber :
        print("number is palindrome")

    else :
        print("not palindrome .")
palindrome(number)