from utils.console_utility import menu

print(menu())
while True:
    operacja = input("Co wybierzesz? ")
    if operacja == "1":
        print(":::Wybrałeś szyfrowanie AES:::\n")
    elif operacja == "2":
        print(":::Wybrałeś szyfrowanie DES:::\n")
    elif operacja == "3":
        print(":::Wybrałeś szyfrowanie Twofish:::\n")
    elif operacja == "0":
        print(menu())
    else:
        break
