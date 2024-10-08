alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

print(ord(alphabet[0]))
character = 0

shift_no = int(input("how much do you want to shift it by?"))

input_answer = input("What do you want encoded (plaintext)")


for i in input_answer:
    charcter = ord(i)
    character + shift_no
    print(chr(character),end='')
    
   