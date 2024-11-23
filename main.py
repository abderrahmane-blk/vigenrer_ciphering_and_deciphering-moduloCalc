from expo_mod_part import expo_mod_start
from vigenere_decipher import vig_decipher_start
from viginere_cipher import vig_cipher_start



if __name__ =="__main__" :

    stop = False
    while(not stop):
        print('---------------------------------------')

        print('enter    1       for    modular exponentiation')
        print('enter    2       for    vigenere ciphering')
        print('enter    3       for    vigenere deciphering')
        print('enter    exit    for    exiting')

        print('---------------------------------------')

        the_input = input(' >>>   ')
        if(the_input == 'exit'):
            stop =True
        else:
            if(the_input == '1'):
                
                expo_mod_start()
            
            elif(the_input == '2'):
                vig_cipher_start()


            elif(the_input == '3'):
                vig_decipher_start()


            else:
                print('irrelevant')





