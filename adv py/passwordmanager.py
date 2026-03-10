passwords = {}
def encrypt(p):
    return "".join(chr(ord(c)+1) for c in p)
def decrypt(p):
    return "".join(chr(ord(c)-1) for c in p)
while True:
    print("\n1.Add 2.Get 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        site = input("Site: ")
        pwd = input("Password: ")
        passwords[site] = encrypt(pwd)
        print("Saved")
    elif ch == "2":
        site = input("Site: ")
        if site in passwords:
            print("Password:", decrypt(passwords[site]))
        else:
            print("Not found")
    elif ch == "3":
        break
