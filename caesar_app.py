import string
from tkinter import *

# create the main window
root = Tk()
# rename the main window
root.title("Caesar Cipher")
# resize the window
root.geometry("450x350")

# creating the message
enter_msg = Label(root, text="Please enter a string to be encrypted: \n ")
# placing the message in the window
enter_msg.grid(row=0, column=0)
# creates the method for the command "done" to be used when pressing the done-button
# maybe this should be removed!!!!!
'''def done():
    to_encipher = Label(root, text=str_entry.get())
    to_encipher.grid(row=3, column=0)
'''


# creating the entry-field
str_entry = Entry(root, width=20)
str_entry.grid(row=1, column=0)
# creating the button and what it does when pressed
'''done_btn = Button(root, text="Done", command=done)
done_btn.grid(row=2, column=0)
'''


# key_msg
# this needs to go further down as well todo
key_msg = Label(root, text="Select a key to encrypt the message with")
key_msg.grid(row=3, column=0)

# the option-menu-widget
# can probably make it prettier todo
key_list = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
]
# shows what key was chosen
default_key = StringVar(root)
default_key.set("1")
# make something happen when the option is entered todo
key_option = OptionMenu(root, default_key, *key_list)
key_option.grid(row=4, column=0)


# encrypts the entered message
def encrypt_msg():
    user_input = str_entry.get()
    key = default_key.get()
    # print(user_input + " " + key)
    encrypt_caesar(alpha_capital, alpha_lower, user_input, key)


alpha_capital = (list(string.ascii_uppercase))
alpha_lower = (list(string.ascii_lowercase))

#TODO break out method for exchanging the letters
def encrypt_caesar(lst_cap, lst_low, message, key):
    enc_user_input = ""
    for c in message:
        if c.isupper():
            for l in lst_cap:
                if l == c:
                    key_index = ((lst_cap.index(c)+int(key)) % len(lst_cap)) # get index of letter to exchange with
                    enc_user_input += str(lst_cap[key_index]) # letters are added to the encrypted message.
        elif c.lower():
            for l in lst_low:
                if l == c:
                    key_index = ((lst_low.index(c)+int(key)) % len(lst_low)) # get index of letter to exchange with
                    enc_user_input += str(lst_low[key_index]) # letters are added to the encrypted message.
        elif c.isdigit():
            enc_user_input += str((int(c) + int(key)) % 10)
        else:
            enc_user_input += c

    show_enc_msg = Label(root, text="The encrypted message is: " + enc_user_input)
    show_enc_msg.grid(row=7, column=0)
    print(enc_user_input)

    ''' FOR DEBUGGING/SEPARATE FUNCTION
    dec_user_input = ""
    print("Deciphering . . . ")
    for c in enc_user_input:
        if c.isalpha():
            dec_user_input += str(chr(ord(c) - int(key)))
        elif c.isdigit():
            d_key = int(c)
            dec_user_input += str(d_key - key)
        else:
            dec_user_input += c

    print(dec_user_input)
    print("Input matches output: ", dec_user_input == user_input)
'''


enc_btn = Button(root, text="Encrypt", command=encrypt_msg)
enc_btn.grid(row=5, column=0)

# clears the text-field
def cancel():
    pass
# clears the textfield and resets the widget to 1 TODO


# needs to be put closer to done_btn todo
cancel_btn = Button(root, text="Cancel", command=cancel)
cancel_btn.grid(row=5, column=1)

def exit_app():
    root.quit()


exit_btn = Button(root, text="Exit", command=exit_app)
exit_btn.grid(row=6, column=0)

# runs the program
root.mainloop()



# root.restart-button