def get_shares():
    while True:
        sharess = input("Enter number of shares: ")
        try:
            sharess = int(sharess)
            break
        except:
            print("Invalid number!")
    return sharess



answer = "y"

while answer in ['y', 'Y']:
    shares = get_shares()


    while True:
        price = input("Enter price (dollars, numerator, denominator): ")
        try:
            num = price.split()
            num1 = int(num[0])
            num2 = int(num[1])
            num3 = int(num[2])
            break
        except:
            print("Invalid price!")

    value = num1 + (num2/num3)
    print("{0} shares with market price {1} {2}/{3} have value ${4:.2f}".format(shares, num1, num2, num3, value * shares))

    answer = input("Continue: ")