def encrypt_letter(P,K):
  if ord(P)>=ord("a") and ord(P)<=ord("z"):
    P = ord(P) - ord("a")
    C = (P + K) % 26
    encrypted_letter = chr(C + ord("a"))
    return encrypted_letter
  elif ord(P)>=ord("A") and ord(P)<=ord("Z"):
    P = ord(P) - ord("A")
    C = (P + K) % 26
    encrypted_letter = chr(C + ord("A"))
    return encrypted_letter
  else:
    return P

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

def decrypt_letter(C,K):
  if ord(C)>=ord("a") and ord(C)<=ord("z"):
    C = ord(C) - ord("a")
    P = (C - K) % 26
    decrypted_letter = chr(P + ord("a"))
    return decrypted_letter
  elif ord(C)>=ord("A") and ord(C)<=ord("Z"):
    C = ord(C) - ord("A")
    P = (C - K) % 26
    decrypted_letter = chr(P + ord("A"))
    return decrypted_letter
  else:
    return C

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

word = "BEAR"
e_word = encrypt_word(word, 10)
print(e_word)
d_word = decrypt_word(e_word,10)
print(d_word)