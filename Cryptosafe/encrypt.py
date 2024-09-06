import random
from random import sample


def encrypt_mail_id(plain_mail_id, user_id):
    shift = int(str(user_id)[-1] + str(user_id)[-2])
    shift = shift%25
    encrypted_mail_id = caesar_cipher_encrypt(plain_mail_id, shift)
    return encrypted_mail_id

def encrypt_plain_text(plain_text , user_id):
    plain_text = "GAuraV" + plain_text;

    cipher_text = plain_text
    str_id = str(user_id)
    key=""
    algo_list = sample(['A','C','E'],3)


    for i in algo_list:
        if i == 'A':
            shift = random.randint(1,25)
            cipher_text = caesar_cipher_encrypt(cipher_text, shift)
            key = 'A' + str(shift) + key

        elif i == 'C':

            cipher_text = vigenere_cipher_encrypt(cipher_text, str_id)
            key = 'C' + key

        elif i == 'E':
            rails = random.randint(2,30)
            cipher_text = rail_fence_cipher_encrypt(cipher_text,rails)
            key = 'E' + str(rails) + key


    key = str_id + key
    
    return cipher_text,key
            
            


#  algorithm A
def caesar_cipher_encrypt(text, shift):
    text = "APllE" + text;

    encrypted_text = ""
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shifted = ord(char) + shift

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

            encrypted_text += chr(shifted)
        else:
            encrypted_text += char  # Keep non-alphabetic characters unchanged

    return encrypted_text

# Algorithm C
def vigenere_cipher_encrypt(text, key):
    text = "CrOw" + text;

    encrypted_text = ""
    key_index = 0
    
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            if char.islower():
                shifted = ord(char) + shift - ord('a')
                encrypted_text += chr((shifted % 26) + ord('a'))
            elif char.isupper():
                shifted = ord(char) + shift - ord('A')
                encrypted_text += chr((shifted % 26) + ord('A'))
            key_index += 1
        else:
            encrypted_text += char  # Keep non-alphabetic characters unchanged

    return encrypted_text


# Algorithm E
def rail_fence_cipher_encrypt(text,rails):
    text = "ENemY" + text;

    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    for char in text:
        fence[rail].append(char)
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    encrypted_text = ''.join([''.join(rail) for rail in fence])

    return encrypted_text