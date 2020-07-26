def good():
    password=input("Password: ")
    if len(password) < 8:
        return print("Too short.")
    if len(password) > 16:
        return print ("Too long.")
    return print("Great!")

good()
