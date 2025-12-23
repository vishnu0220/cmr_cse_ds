def reverseNumber(num):
    reverse = 0
    temp = num
    while temp > 0:
        rem = temp % 10
        reverse = reverse*10 + rem
        temp //= 10
    return reverse
    
num = int(input())
print("Reverse of ", num , " : " , reverseNumber(num))