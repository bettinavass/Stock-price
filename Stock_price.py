shares = input("Enter number of shares: ")

price = input("Enter price (dollar, numerator,denominator): ")

num = price.split()

num1 = int(num[0])
num2 = int(num[1])
num3 = int(num[2])

value = num1 + (num2/num3)


print(shares, "shares with market price",num1, num2, num3, "have value", "$", value )
