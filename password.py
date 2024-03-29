import tkinter
import string
import random

class PasswordGeneratorApp():
    MAX_CHARS = 15
    MIN_CHARS = 3
    CHAR_OPTIONS = ["Alphanumeric", "Numeric", "Alpha"]
    DIFFICULTY_OPTIONS = ["Easy", "Medium", "Hard"]
    GRID_PADY = (18, 18)
    
    def __init__(self):
        self.initUI()
        
    def initUI(self):
        # Construction of the root element
        self.master = tkinter.Tk()
        self.master.title("Password Generator")
        self.master.geometry("580x300")
        self.master.configure(bg="#f0f0f0")  # Setting background color
        
        self.password_type = tkinter.StringVar(self.master, value=PasswordGeneratorApp.CHAR_OPTIONS[0])
        self.num_chars = tkinter.IntVar(self.master, value=PasswordGeneratorApp.MIN_CHARS)
        self.difficulty_level = tkinter.StringVar(self.master, value=PasswordGeneratorApp.DIFFICULTY_OPTIONS[0])
        
        self.label_chars = tkinter.Label(self.master, text="Characters that will compose the Password:", bg="#f0f0f0")
        self.option_menu_chars = tkinter.OptionMenu(self.master, self.password_type, *PasswordGeneratorApp.CHAR_OPTIONS)
        
        self.frame_num_chars = tkinter.Frame(self.master) 
        self.label_num_chars = tkinter.Label(self.master, text="Password Length:", bg="#f0f0f0")
        self.option_menu_num_chars = tkinter.OptionMenu(self.master, self.num_chars, *range(PasswordGeneratorApp.MIN_CHARS, PasswordGeneratorApp.MAX_CHARS+1))
        
        self.frame_difficulty = tkinter.Frame(self.master) 
        self.label_difficulty = tkinter.Label(self.master, text="Difficulty Level:", bg="#f0f0f0")
        self.option_menu_difficulty = tkinter.OptionMenu(self.master, self.difficulty_level, *PasswordGeneratorApp.DIFFICULTY_OPTIONS)
        
        self.text_password_output = tkinter.Text(self.master, border=2, height=2, width=30)
        
        self.frame_buttons = tkinter.Frame(bg="#f0f0f0")
        self.button_generate = tkinter.Button(self.frame_buttons, text="Generate", width=8, command=lambda: self.generate_password())
        self.button_close = tkinter.Button(self.frame_buttons, text="Close", command=self.master.quit, width=8)
        
        self.label_chars.grid(row=0, column=0, pady=PasswordGeneratorApp.GRID_PADY, padx=10, sticky='w')
        self.option_menu_chars.grid(row=0, column=1, pady=PasswordGeneratorApp.GRID_PADY, sticky='w')
        
        self.label_num_chars.grid(row=1, column=0, pady=PasswordGeneratorApp.GRID_PADY, padx=10, sticky='w')
        self.option_menu_num_chars.grid(row=1, column=1, pady=PasswordGeneratorApp.GRID_PADY, sticky='w')
        
        self.label_difficulty.grid(row=2, column=0, pady=PasswordGeneratorApp.GRID_PADY, padx=10, sticky='w')
        self.option_menu_difficulty.grid(row=2, column=1, pady=PasswordGeneratorApp.GRID_PADY, sticky='w')
        
        self.text_password_output.grid(row=3, column=0, pady=PasswordGeneratorApp.GRID_PADY, padx=10, columnspan=2)
        
        self.button_generate.pack(side=tkinter.LEFT, padx=10)
        self.button_close.pack(side=tkinter.LEFT, padx=10)
        self.frame_buttons.grid(row=4, column=1, columnspan=2, sticky='w')
               
        self.master.mainloop()

    def generate_password(self):
        chars = ""
        password_type = self.password_type.get().lower()
        if password_type == "numeric":
            chars = string.digits
        elif password_type == "alpha":
            chars = string.ascii_letters
        else:
            chars = string.digits + string.ascii_letters   

        password = "".join(random.choices(chars, k=self.num_chars.get()))
        
        self.text_password_output.delete("1.0", tkinter.END)
        self.text_password_output.insert("1.0", password)

if __name__=="__main__":
    PasswordGeneratorApp()
