def exchange_letters(lst, char, key):
    for l in lst:
        if l == char:
            key_index = ((lst.index(char) + int(key)) % len(lst))  # get index of letter to exchange with
    return lst[key_index]


def encrypt_caesar(lst_cap, lst_low, message, key):
    enc_user_input = ""
    for c in message:
        if c.isalpha():
            if c.isupper():
                enc_user_input += str(exchange_letters(lst_cap, c, key))
            elif c.lower():
                enc_user_input += str(exchange_letters(lst_low, c, key))
        elif c.isdigit():
            enc_user_input += str((int(c) + int(key)) % 10)
        else:
            enc_user_input += c
    print(enc_user_input)
    return enc_user_input

