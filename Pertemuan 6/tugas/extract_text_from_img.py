import tkinter as tk
from PIL import Image, ImageTk
from pytesseract import pytesseract

class TextExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Extractor App")

        # Define path to tesseract.exe
        self.path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Define path to image
        self.path_to_image = 'python.png'  # Ganti dengan path gambar yang sesuai

        # Point tessaract_cmd to tessaract.exe
        pytesseract.tesseract_cmd = self.path_to_tesseract

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Display the author information
        author_label = tk.Label(self.root, text="AHMAD MAULANA 220511138")
        author_label.grid(row=0, column=0, padx=10, pady=10)

        try:
            # Open image with PIL
            img = Image.open(self.path_to_image)

            # Extract text from image
            text = pytesseract.image_to_string(img)

            # Display the image in the Tkinter window
            img.thumbnail((300, 300))  # Resize image for display
            img_tk = ImageTk.PhotoImage(img)
            image_label = tk.Label(self.root, image=img_tk)
            image_label.image = img_tk
            image_label.grid(row=1, column=0, padx=10, pady=10)

            # Display extracted text
            text_label = tk.Label(self.root, text=f"Extracted Text:\n{text}")
            text_label.grid(row=2, column=0, padx=10, pady=10)

        except FileNotFoundError:
            error_label = tk.Label(self.root, text=f"File not found: {self.path_to_image}")
            error_label.grid(row=1, column=0, padx=10, pady=10)
        except Exception as e:
            error_label = tk.Label(self.root, text=f"Error: {str(e)}")
            error_label.grid(row=1, column=0, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextExtractorApp(root)
    root.mainloop()
