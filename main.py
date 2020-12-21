print("Welcome to the rollercoaster!")
name = input("What is your name?\n")
height = int(input("What is your height in cm?\n"))

if height >= 120:
  print("Hooray " + name + " ,you can ride the rollercoaster!")
  duration = int(input("How long of a ride do you want? Enter the duration in minutes.\n"))
else:
  print("Oops " + name + " ,you're too short to ride the rollercoaster!")
  exit()

ticket_cost = duration * 20
print(f"Your ticket should cost ${ticket_cost}. Thanks, enjoy!")



