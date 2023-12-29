from huffman import huffman_main_func
from shannon_fano import shannon_fano_main_func
import os, time

isContinue = True

while isContinue:
    print("##################################################")
    print("Select Encryption Algorithms:")
    print("1. Huffman\n2. Shannon-Fano\n3. Exit")
    print("##################################################")
    user_select = int(input("Your selection: "))
    print("\n")

    if user_select == 1:
        huffman_main_func()
        time.sleep(5)
    elif user_select == 2:
        shannon_fano_main_func()
        time.sleep(5)
    elif user_select == 3:
        break
    else:    
        print("Invalid input!")
        time.sleep(2)
        os.system('cls')