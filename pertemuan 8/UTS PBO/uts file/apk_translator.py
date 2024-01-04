from tkinter import Frame, Label, Entry, Button, OptionMenu, StringVar, YES, BOTH, END, Tk, W
from googletrans import Translator

class Translate:
    def __init__(self, parent, title, nama, nim):
        self.parent = parent
        self.parent.geometry("600x300")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.parent.configure(bg="#5F9EA0")  # Set the main background color
        self.aturKomponen(nama, nim)

    def aturKomponen(self, nama, nim):
        # Add Labels for name and student ID at the top
        Label(self.parent, text=nama, font=("Helvetica", 16, "bold"), bg="#5F9EA0").pack(pady=5)
        Label(self.parent, text=nim, font=("Helvetica", 16), bg="#5F9EA0").pack(pady=5)

        mainFrame = Frame(self.parent, bd=10, bg="#5F9EA0")  # Change the background color here
        mainFrame.pack(fill=BOTH, expand=YES)

        # Install Labels
        Label(mainFrame, text='Masukan  Text:', bg="#5F9EA0").grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Mulai Translate:', bg="#5F9EA0").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)

        # Install textboxes
        self.source_text = Entry(mainFrame, width=50)
        self.source_text.grid(row=0, column=1, columnspan=3, padx=5, pady=5)

        self.result_text = Entry(mainFrame, width=50)
        self.result_text.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

        # List of language codes and language names
        self.language_mapping = {
            "en": "English",
            "mn": "Mongolian",  
            "no": "Norwegian"   
        }

        # Install OptionMenu to select the language
        self.selected_language = StringVar()
        self.selected_language.set("en")  # Default language
        languages = list(self.language_mapping.values())
        self.option_menu = OptionMenu(mainFrame, self.selected_language, *languages)
        self.option_menu.grid(row=1, column=0, padx=5, pady=5)

        # Install Button to translate
        self.btn_translate = Button(mainFrame, text='Translate', command=self.onTranslate)
        self.btn_translate.grid(row=1, column=1, padx=5, pady=5)

    def onTranslate(self):
        dest_lang = [key for key, value in self.language_mapping.items() if value == self.selected_language.get()][0]

        # Create an instance object
        translator = Translator()

        # Translate
        result = translator.translate(self.source_text.get(), dest=dest_lang)

        # Clear the previous result textbox content
        self.result_text.delete(0, END)

        # Display the translation result
        self.result_text.insert(END, result.text)

    def onKeluar(self, event=None):
        # Command to close the application
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    app = Translate(root, "Aplikasi Translator", "AHMAD MAULANA", "220511138")
    root.mainloop()
