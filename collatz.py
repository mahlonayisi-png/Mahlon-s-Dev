def collatz(number):
    if number % 2 == 0:
       result = number // 2

    else:
        result = 3 * number + 2
        print(number)
    return result
print("enter a  number")
n = int(input())
while n != 1:
    n =collatz(n)