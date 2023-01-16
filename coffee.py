print("Hello, welcome to Express Espresso!\n")

name = input("What is your name?\n")

if name == "Jack" or name == "Rylie" or name == "Nozza" or name == "Louie":
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "Yes" and good_deeds < 4:
        print("Your're not welcome here " + name + ". Get out of here!")
        exit()
    else:
        print("Oh, so you're one of those good " + name + ". Come on in!\n")
else:
    print("Hello " + name + ", thank you so much for coming in today.\n")

menu = "Black Coffee, Espresso, Latte, Cappucino, Frappuccino, Tea, Snack Bar, Croissant, Cream Tea\n"

print("What would you like from our menu today? Here is what we are serivng.\n" + menu)

order = input()

if order == "Frappuccino":
    price = 7
elif order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 5
elif order == "Latte":
    price = 4
elif order == "Cappucino":
    price = 6
elif order == "Tea":
    price = 2
elif order == "Snack Bar":
    price = 1.50
elif order == "Croissant":
    price = 2
elif order == "Cream Tea":
    price = 18  
else:
  print("Sorry, we don't have that here.\n")
  print("What would you like from our menu today? Here is what we are serivng.\n" + menu)

  order = input()

  if order == "Frappuccino":
    price = 7
  elif order == "Black Coffee":
    price = 3
  elif order == "Espresso":
    price = 5
  elif order == "Latte":
    price = 4
  elif order == "Cappucino":
    price = 6
  elif order == "Tea":
    price = 2
  elif order == "Snack Bar":
     price = 1.50
  elif order == "Croissant":
    price = 2
  elif order == "Cream Tea":
    price = 18  
  else:
   print("Sorry, we don't have that here.\n")
   exit() 
  quantity = input("Quantity?\n")

  total = price * int(quantity)

  print("Thank you. Your total is: £" + str(total))

  print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for you in a moment.\n")

  print("Your drink/food is ready, have a good day!\n")  
  exit()  
  
quantity = input("Quantity?\n")

total = price * int(quantity)

print("Thank you. Your total is: £" + str(total))

print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for you in a moment.\n")

print("Your drink/food is ready, have a good day!\n")  
exit()