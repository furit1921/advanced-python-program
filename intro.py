def intro():
   name = input("what is the name of you human being? ")
   print("hello ", name)
   return name

human = intro()
print("nice to see a human in space!",human,"where do you come from?")

answer = input("where do you come from? ")

if answer == "earth":
    print("oh nice!",answer,"seems like e nice place to live in",human)
elif answer == "jupiter":
    print("my home planet is ", answer,"ĘĦ⨅⫒⨜⩙Đ")
else:
    print("oh love that place",human)