"""This is a function written by Emmanuel Oluwatobi that accpets two parameters,
one is a text that has been encrypted and the second is a negative or positive integer
 key to decrypt the text. The function returns the decrypted text."""
def decryptor(text, key):
    alpha_list = ['A','B','C','D','E','F','G','H',
                  'I','J','K','L','M','N','O','P',
                  'Q','R','S','T','U','V','W','X',
                  'Y','Z']
    decrypted_text = ''
    try:
        for char in text:
            if char.upper() in alpha_list:
                n_key = str(key)
                if n_key[0]=='-':
                    real_char_key = (alpha_list.index(char.upper())+int(key)+26)%26
                    if char == char.upper():
                        decrypted_text += alpha_list[real_char_key]
                    else:
                        decrypted_text += alpha_list[real_char_key].lower()
                else:
                    real_char_key = (alpha_list.index(char.upper())+int(key))%26
                    if char == char.upper():
                        decrypted_text += alpha_list[real_char_key]
                    else:
                        decrypted_text += alpha_list[real_char_key].lower()
            else:
                decrypted_text += char

        return decrypted_text
    except:
        return "Decryptor function accepts a string(text) as first parameter and a positive or negative integer as second parameter. e.g print(decryptor('shade', -3)"

#Function Test
print(decryptor("sdwp zkaoj'p gehh ukq, iwgao ukq",-22))
print(decryptor("Nby vis cm aiix.",6))
print(decryptor("Rovvy pbyw dro ydrob csno...", -10))
print(decryptor("Ukq'ra kjhu fqop xacqj.", 4))
print(decryptor("sdwp zkaoj'p gehh ukq, iwgao ukq opnwjcan.",-22))
print(decryptor("Rc'b mjh 9 xo cqn 30 mjhb xo lxmn.",17))