input_string = input("Write a string: ")
alphabet = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
for symbol in input_string:
    if symbol in alphabet:
        alphabet[symbol] = alphabet[symbol] + 1
i = 0
alphabet = list(alphabet.items())
print(alphabet)
while i < len(alphabet)-1:
    j = i + 1
    while j < len(alphabet):
        if alphabet[i][1]<alphabet[j][1]:
            temp = alphabet[i]
            alphabet[i] = alphabet[j]
            alphabet[j] = temp
        j = j + 1
    i = i + 1
for res in alphabet:
    print(res)