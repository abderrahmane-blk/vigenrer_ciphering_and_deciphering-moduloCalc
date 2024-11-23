from viginere_cipher import characters




def vig_decipher(text,key):
    # print('ciphering')
    res =''
    l_key =len(key)

    try:
        for i,char in enumerate(text,start=0):
            idx = characters.index(char)
            # print('the char :',char ,'    its index ' ,idx)

            keychar = key[(i % l_key)]
            new_idx =characters.index(keychar)
            # print('the key char: ',keychar ,'    its index',new_idx)

            # print(f'change {char} and key_char {keychar}  are modded to {((idx+new_idx) %len(characters))} which is :{characters[((idx+new_idx) %len(characters))]}')
            val =idx-new_idx
            while val < 0 :
                val += len(characters)
            # print('deciphered to :',val)

            res+=characters[(val) %len(characters)]
            # print(res,'\n')

        print("\n---------------------------\nplain text :     ")
        print( res)

    except:
        print('something went wrong')




def vig_decipher_start():
    print('---------------------------------------')
    print('vigenere decipher')
    print('---------------------------------------')
    
    text = input('enter the cipher-text you want to decipher :\n')
    key = input('enter the key :\n')

    # print(text ,key)

    vig_decipher(text,key)




    print('\n\n')