global a
def greet():
    a=10
    print("What is your name")
    print("How are you doing today")
print(a)
# greet()
# greet()

# n=int((input("Enter the number times u have to greet")))
# for _ in range (n):
    # greet()

price=int(input("Enter the price"))
discount=int(input("Enter the discount"))


# discounted price calculate
def discountedPrice(price, discount):
    return price - (price * discount / 100)
print(discountedPrice(price, discount))