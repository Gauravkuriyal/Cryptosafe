def find_id(key):
    user_id = ''
    for i in key:
        if i.isnumeric():
            user_id = user_id + i
        else :
            break
    return user_id

def decrypt_mail_id(cipher_mail_id, user_id):
    shift = int(str(user_id)[-1] + str(user_id)[-2])
    shift = shift%25
    
    decrypted_mail_id = caesar_cipher_decrypt(cipher_mail_id, shift)
    
    return decrypted_mail_id

def decrypt_cipher_text(cipher_text,key,user_id):
    plain_text = cipher_text
    i = len(user_id)

    while i<len(key):
        if key[i] == 'A':
            
            shift = int(key[i+1])
            try:
                if key[i+2].isnumeric():
                    shift = shift*10 + int(key[i+2])
            except:
                pass
            
            plain_text = caesar_cipher_decrypt(plain_text, shift)

            # Checking if data is valid or not
            if plain_text == "Data not found":
                return plain_text

            i+=1

        elif key[i] == 'C':
            plain_text = vigenere_cipher_decrypt(plain_text, user_id)

            if plain_text == "Data not found":
                return plain_text
            
        elif key[i] == 'E':
            rails = int(key[i+1])
            try :
                if key[i+2].isnumeric():
                    rails = rails*10 + int(key[i+2])
            except:
                pass
            plain_text = rail_fence_cipher_decrypt(plain_text, rails)

            # Checking if data is valid or not
            if plain_text == "Data not found":
                return plain_text

            i+=1
            
        i+=1
    # Checking if data is valid or not
    if plain_text[0:6] == "GAuraV" :
        plain_text = plain_text[6:]
    else:
        plain_text = "Data not found"
    
    return plain_text



#Algorithm A
def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift

            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26

            decrypted_text += chr(shifted)
        else:
            decrypted_text += char

    
    if decrypted_text[0:5] == "APllE" :
        decrypted_text = decrypted_text[5:]
    else:
        decrypted_text = "Data not found"

    return decrypted_text

#Algorithm C
def vigenere_cipher_decrypt(text, key):
    decrypted_text = ""
    key_index = 0
    
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            if char.islower():
                shifted = ord(char) - shift - ord('a')
                decrypted_text += chr((shifted % 26) + ord('a'))
            elif char.isupper():
                shifted = ord(char) - shift - ord('A')
                decrypted_text += chr((shifted % 26) + ord('A'))
            key_index += 1
        else:
            decrypted_text += char

    if decrypted_text[0:4] == "CrOw" :
        decrypted_text = decrypted_text[4:]
    else:
        decrypted_text = "Data not found"

    return decrypted_text

#Algorithm E
def rail_fence_cipher_decrypt(cipher, key):
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]
    dir_down = None
    row, col = 0, 0
    
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key -1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index< len(cipher) :
                rail[i][j] = cipher[index]
                index+=1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False

        if rail[row][col] != '*':
            result.append(rail[row][col])
            col+=1
        
        if dir_down:
            row+=1
        else :
            row-=1
    
    decrypted_text = ("".join(result))

    if decrypted_text[0:5] == "ENemY" :
        decrypted_text = decrypted_text[5:]
    else:
        decrypted_text = "Data not found"
    
    return decrypted_text