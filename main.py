def decryption(code, distanceValue):
  print("\nYour encrypted text is:", code)
  encryptedText = code
  distance = int(distanceValue)
  text = ""
  for ch in encryptedText:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < ord('!'):
      cipherValue = ord('~') - (distance - abs(ord('!') - ordvalue - 1))
    text += chr(cipherValue)
  print("The decrypted text is:", text)
  return text

code = input("Please input encrypted text: ")
distanceValue = input("Please input a distance value: ")
while True:
  decryption(code, distanceValue)
  option = input("\nIs this the desired result? (y/n) ")
  if option == "y":
    break
  elif option == "n":
    code = input("\nPlease re-input encrypted text: ")
    distanceValue = input("Please input a new distance value: ")
  else:
    print("\nInvalid response.  Reprinting results.")
print("\nYour plaintext is", text)