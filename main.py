def encrypt_letter(P,K):
  if ord(P)>=ord("a") and ord(P)<=ord("z"):
    #WRITE THIS
    encrypted_letter = "?"
    return encrypted_letter
  elif ord(P)>=ord("A") and ord(P)<=ord("Z"):
    #WRITE THIS
    encrypted_letter = "?"
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
  #WRITE THIS FUNCTION
  return C

def decrypt_word(C,K):
  #WRITE THIS FUNCTION
  decrypted_word = ""
  return decrypted_word

def decrypt_message(C,K):
  #WRITE THIS FUNCTION
  decrypted_message =[]
  return decrypted_message