#Coffee shop.
#We're making a robot barista.

#Note, learn how to use google tts so you can use it for the coffee barista.

print("Hello, welcome to Happyface Hackers \n" "Coffee!!!!!!!!!")


name = input("What's your name? \n")

print("Hello " + name + ", use this coffee on your \n" "journey from zero to hero. \n \n")

menu = "Black, Espresso, Cappuccino."

print("Hi " + name + ", what would you like today? \n" "This is what we're serving: \n" + menu)

order = input()

price = 8 

quantity = input("\n\n" "How much coffees would you like? \n")

total = price * int(quantity)

print("Your total is: $" + str(total) + ".")

print("\n\n" "Sounds good " + name + " we'll have your \n" + quantity + " " + order + "\n" "in a moment.")