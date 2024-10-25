import string

alphabet = list(string.printable)
print(len(alphabet))


def encode(message, key):

    encoded_list = []
    
    key = key % len(alphabet)
    keyed_alphabet = alphabet[key:] + alphabet[:key]

    for letter in message:

        encoded_list.append(str(keyed_alphabet.index(letter)) if letter != " " else "/")

    encoded_string = " ".join(encoded_list)

    return encoded_string
    


def decode(message, key):

    decoded_list = []

    key = key % len(alphabet)
    keyed_alphabet = alphabet[key:] + alphabet[:key]

    for number in message.split(" "):

        if number != "/" and number != " ":

            decoded_list.append(keyed_alphabet[int(number)])

        else:

            decoded_list.append(" ")

    decoded_string = "".join(decoded_list)

    return decoded_string


ans = input("Encode (E) or Decode (D)?: ")

if ans.lower() == "d":

    key = input("Key: ")
    message = input("Message: ")

    if set(message).issubset(set(alphabet)):
        print(decode(message, int(key)))
    else:
        print("Invalid Input")
elif ans.lower() == "e":

    key = input("Key: ")
    message = input("Message: ")

    if set(message).issubset(set(alphabet)):
        print(encode(message, int(key)))
    else:
        print("Invalid Message")

else:
    print("Invalid Option")
