from utils.console_utility import menu
import src.aes as aes
import src.des as des
import src.three_des as three_des
import src.RSA as rsa
import src.elgamal as elgamal
import src.ecc as ecc
import src.my_salting as salting

print(menu())
while True:
    operacja = input("Co wybierzesz? ")
    if operacja == "1":
        print(":::Wybrałeś szyfrowanie AES:::\n"), aes.main()
    elif operacja == "2":
        print(":::Wybrałeś szyfrowanie DES:::\n"), des.main()
    elif operacja == "3":
        print(":::Wybrałeś szyfrowanie 3DES:::\n"), three_des.main()
    elif operacja == "4":
        print(":::Wybrałeś szyfrowanie RSA:::\n"), rsa.main()
    elif operacja == "5":
        print(":::Wybrałeś szyfrowanie ElGamal:::\n"), elgamal.main()
    elif operacja == "6":
        print(":::Wybrałeś szyfrowanie ECC:::\n"), ecc.main()
    elif operacja == "7":
        print(":::Wybrałeś salting:::\n"), salting.main()
    elif operacja == "0":
        print(menu())
    else:
        break
