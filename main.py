def encrypt(txt, shift):
    encd_text = ''
    for i in txt:
        pos = alphabet.index(i)
        n_pos = pos + shift
        encd_text += alphabet[n_pos]
    return encd_text

def decrypt(txt, shift):
    decd_text = ''
    for i in txt:
        pos = alphabet.index(i)
        n_pos = pos - shift
        decd_text += alphabet[n_pos]
    return decd_text


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction == 'encode':
    x=encrypt(text,shift)
    print("Encoded Text is "+x)
elif direction == 'decode':
    y=decrypt(text,shift)
    print("Decoded Text is " +y)
