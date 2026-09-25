scents = ("Amber orb 150ml", "Mande allure 150ml", "Cred musa 150ml", "Cotron dor 150ml", "Velvet empress 100ml", "Lave silk 100ml")
prices = (10000, 10000, 10000, 10000, 8000, 8000)

def show_scents():
    print("Hello Renn have:")
    for s in scents:
        print(f"{s}")

def get_price(name):
    for i in range(len(scents)):
        if scents[ i ] == name:
            return prices[ i ]
    return 0

show_scents()

buy = input(f"What do you want to buy?")
price = get_price(buy)

if price == 0:
    print("product not avalable")
else:
    print(f"{buy} is N{price}")
    cash = int (input("Whats your budget?"))
    if cash >= price:
        print(f"purchase succesful {buy} is N{price} your change is {cash - price}")
    else:
        print(f"insufficent you need {price - cash} more Thanks")