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
elif answer == "venus":
    print("wait ",answer,"is very hot and toxic for you to live in",human)
elif answer == "mars":
    print("makes sense for humans to live in",answer," as i heard yall were building bases there ",human)
elif answer == "saturn":
    print("i dont know what ",answer," is ? is it ring god",human)
elif answer == "uranus":
    print("ohHOHHohh",answer,"wery cild and vindy place",human)

else:
    print("oh love that place",human)
    