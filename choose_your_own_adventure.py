name = input("Type your name: ")
print("welcome ", name,"to this adventure 👋")

answer = input(
"You are on a dirt road 🛤️, it has come to an end and you can go left ⬅️  or right ➡️ . Which way would you like to go? "
).lower()

if answer == "left" :
    answer = input(
        "You come to a river 🏞️, you can walk around it 🚶 or swim accross 🏊‍♂️ ? Type walk to walk around and swim to swim accross: "
        ).lower()

    if answer == "swim":
        print("You swam accross 🏊‍♂️ and were eaten by an alligator 🐊.")
    elif answer == "walk":
        print("You walked 🚶 for many miles, ran out of water and lost the game ❌")
    else:
        print("Not a valid option. You lose ❌")
elif answer == "right":
    answer = input("You come to a bridge 🌉  ,it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()
    if answer == "cross":
        answer = input("You cross the bridge 🌉  and meet a stranger 🧍  .Do you want to talk to them 🗣️ (yes/no)? ").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you precious stone 💎. You WIN 🏆")
            print("CONGRATULATIONS",name," 🎊 🎊 🎊")
            
        elif answer == "no":
            print("You ignore the stranger and they are offended. You lose ❌")
        else:
            print("Not a valid option. You lose ❌")
    elif answer == "back":
        print("You go back 🚶 and lose ❌")
    else:
        print("Not a valid option. You lose ❌")
else:
    print("Not a valid option. You lose ❌")

print("Thank you for trynig",name," see you next time!")
