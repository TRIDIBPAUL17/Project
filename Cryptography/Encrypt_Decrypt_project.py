from tkinter import *
from tkinter import messagebox
import base64

def encrypt():
    key = code.get()

    if key:
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="cyan2")

        message = text1.get(1.0, END)
        encode_message = message.encode("utf-8")
        base64_bytes = base64.b64encode(encode_message)
        encrypt_message = base64_bytes.decode("utf-8")

        Label(screen1, text="ENCRYPTED TEXT", font="arial", fg="black", bg="cyan2").place(x=10, y=0)
        text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encrypt_message)
    else:
        messagebox.showerror("Encryption", "Enter a valid encryption key")


def decrypt():
    key = code.get()

    if key:
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        decode_message = message.encode("utf-8")
        base64_bytes = base64.b64decode(decode_message)
        decrypt_message = base64_bytes.decode("utf-8")

        Label(screen2, text="DECRYPTED TEXT", font="arial", fg="black", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, decrypt_message)
    else:
        messagebox.showerror("Decryption", "Enter a valid decryption key")


def reset():
    code.set("")
    text1.delete(1.0, END)


def exit_screen():
    screen.destroy()


def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    screen.title("Encrypt_Decrypt_Project")

    Label(text="Enter text for encryption and decryption", fg="black", font=("calibri", 13, "bold")).place(x=10, y=10)
    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13, "bold")).place(x=10,
                                                                                                                y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Button(text="Encrypt", height="2", width=24, bg="cyan2", fg="black", font=("Arial", 9, "bold"), bd=0,
           command=encrypt).place(x=10, y=250)
    Button(text="Decrypt", height="2", width=24, bg="#00bd56", fg="black", font=("Arial", 9, "bold"), bd=0,
           command=decrypt).place(x=191, y=250)
    Button(text="Reset", height="2", width=50, bg="#1089ff", fg="white", font=("Arial", 9, "bold"), bd=0,
           command=reset).place(x=10, y=300)
    Button(text="Exit", height="2", width=50, bg="#ed3833", fg="white", font=("Arial", 9, "bold"), bd=0,
           command=exit_screen).place(x=10, y=350)

    screen.mainloop()


if __name__ == "__main__":
    main_screen()
