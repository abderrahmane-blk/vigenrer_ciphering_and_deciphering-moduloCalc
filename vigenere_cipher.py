characters = [
    # Letters 0-25 26-51
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',

    # Digits 52-61
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',

    # Punctuation 62 - 93
    '.', ',', '?', '!', ':', ';','-',
      '\"', "\'", 
      #'–','—','#','...'
      '(', ')', '[', ']', '{', '}', '<', '>', '@', '$', '%', '&', '*', '+', '=', '_', '/', '\\', '|', '~', '^', '`',

    # Whitespace 94-97
    ' ','\n', 
    #   '\t',  '\r'
]
# characters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
# ]



def vig_cipher(text,key):
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
            changed= (idx+new_idx) %len(characters)
            # print('ciphered to :',changed)
            res+=characters[changed]
            # print(res ,'\n')

        print("\n---------------------------\nciphered text :     ")
        print( res)

    except:
        print('something went wrong')







def vig_cipher_start():
    print('---------------------------------------')
    print('vigenere cipher')
    print('---------------------------------------')
    text = input('enter the text you want to cipher :\n')
    key = input('\nenter the key :\n')

    print('\n')
    # print(text ,key)

    vig_cipher(text,key)


    print('\n\n')






