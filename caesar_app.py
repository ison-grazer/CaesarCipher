import string
from tkinter import *
import caesar

# TODO do a menubar with help, encrypt, decrypt
# TODO do the decrypt-logic and an option to use it
# TODO make it less visually displeasing
# TODO fix how to display the encrypted message


def main():
    root = Tk()
    root.title("Caesar Cipher")
    root.geometry("450x350")

    enter_msg = Label(root, text="Please enter a string to be encrypted: \n ")
    enter_msg.grid(row=0, column=0)

    # creating the entry-field
    str_entry = Entry(root, width=20)
    str_entry.grid(row=1, column=0, pady=10)

    # the key which is used to encrypt the message
    key_msg = Label(root, text="Select a key to encrypt the message with")
    key_msg.grid(row=3, column=0)

    # the option-menu-widget for the key
    key_list = [str(x) for x in range(10)]  # list(map(str,range(10))) extract this

    # shows what key was chosen
    default_key = StringVar(root)
    default_key.set("1")

    key_option = OptionMenu(root, default_key, *key_list)
    key_option.grid(row=4, column=0)

    # make the frame here
    result_msg = Label(root, text="Your encrypted message is: ")
    result_msg.grid(row=6, column=0)

    textbox = Label(root, text="..", bg='white')
    textbox.grid(row=7, column=0)

    # encrypts the entered message

    def send_encrypt():
        encrypt_msg(str_entry, default_key, textbox)


    enc_btn = Button(root, text="Encrypt", command=send_encrypt)
    enc_btn.grid(row=5, column=0)

    exit_btn = Button(root, text="Exit", command=root.quit)
    exit_btn.grid(row=8, column=0)

    root.mainloop()
# root.restart-button


def encrypt_msg(str_entry, default_key, textbox):
    user_input = str_entry.get()
    key = default_key.get()
    alpha_capital = (list(string.ascii_uppercase))
    alpha_lower = (list(string.ascii_lowercase))

    # puts the message in a label or textbox
    msg = caesar.encrypt_caesar(alpha_capital, alpha_lower, user_input, key)
    textbox.config(text=msg)

main()

