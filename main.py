from file_input_output import open_file, write_file

def encrypt_letter(letter,key):
  if ord(letter) >= ord('a') and ord(letter) <= ord("z"):
    P = ord(letter) - ord('a') #change to number
    C = (key[0]*P + key[1]) % 26
    encrypted_letter = chr(C + ord('a'))
  elif ord(letter) >= ord('A') and ord(letter) <= ord("Z"):
  return letter

def encrypt_word(P,K):
  encrypted_word =""
  for letter in P:
    encrypted_word +=encrypt_letter(letter,K)
  return encrypted_word

def encrypt_message(P,K):
  encrypted_message=[]
  for w in P:
    encrypted_message.append(encrypt_word(w,K))
  return encrypted_message

def decrypt_letter(letter,key): #key should be a list key 
  if ord(letter) >= ord('a') and ord(letter) <= ord("z"):

  return decrypted_letter

def decrypt_word(C,K):
  decrypted_word =""
  for letter in C:
    decrypted_word += decrypt_letter(letter,K)
  return decrypted_word

def decrypt_message(C,K):
  decrypted_message=[]
  for w in C:
    decrypted_message.append(decrypt_word(w,K))
  return decrypted_message
  
def find_inverse(a):
  inverse = 2
  while ((inverse*a) % 26 != 1):
    inverse += 1
  return inverse

#NOTES FOR ENCRYPTING USING AN AFFINE CIPHER

key = [17, 21] #first number should be prime, the second number between 0 and 25
letter_to_encrypt = 'c'
P = ord(letter_to_encrypt) - ord('a') #change to number
C = (key[0]*P + key[1]) % 26
encrypted_letter = chr(C + ord('a'))
print(encrypted_letter)


#print the alphabet key YOU DONT NEED THIS
for P in range(26):
  C = (key[0]*P + key[1]) % 26
  enc_letter = chr(C + ord('a'))
  print(chr(P + ord('a')) , enc_letter)

#NOTES FOR DECRYPTING USING AN AFFINE CIPHER
a_inverse = find_inverse(key[0]) #find the inverse of a
C = ord(encrypted_letter) - ord('a')
P = (a_inverse*(C - key[1])) % 26
decrypted_letter = chr(P + ord('a'))
print(decrypted_letter)


