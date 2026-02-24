# continue
while True:
    print(" hey there who are you ")
    name = input()
    if name != 'Appiah':
        continue
    print("hey  Appiah what is the password ( it's a fish).")
    password = input()
    if password == "madfish":
        break
    print("access granted")


