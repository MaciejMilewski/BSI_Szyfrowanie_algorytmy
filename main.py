from utils.console_utility import menu
import src.aes as aes
import src.des as des
import src.three_des as three_des

print(menu())
while True:
    operacja = input("Co wybierzesz? ")
    if operacja == "1":
        print(":::Wybrałeś szyfrowanie AES:::\n"), aes.main()
    elif operacja == "2":
        print(":::Wybrałeś szyfrowanie DES:::\n"), des.main()
    elif operacja == "3":
        print(":::Wybrałeś szyfrowanie 3DES:::\n"), three_des.main()
    elif operacja == "0":
        print(menu())
    else:
        break
