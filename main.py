def rot13(message):
    turn = 0
    message = input("Enter word or sentence to encrypt in Rot13: ")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted = []
    for letter in message:
        if letter in alphabet_upper:
            new_index = (alphabet_upper.index(letter) + 13) % 26
            new_letter = alphabet_upper[new_index]
            encrypted.append(new_letter)
        elif letter in alphabet:
            new_index = (alphabet.index(letter) + 13) % 26
            new_letter = alphabet[new_index]
            encrypted.append(new_letter)
        else:
            encrypted.append(letter)
    turn +=1
    result = "".join(encrypted)

    return result
