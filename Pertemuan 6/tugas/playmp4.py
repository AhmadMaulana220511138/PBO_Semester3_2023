import tkinter as tk
from PIL import Image, ImageTk
import cv2

class VideoPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")

        # Replace 'tugas/drakor.mp4' with the path to your video file
        self.video_path = 'tugas/kelas.mp4'

        # Create a VideoCapture object
        self.cap = cv2.VideoCapture(self.video_path)

        # Check if the video opened successfully
        if not self.cap.isOpened():
            print("Error opening video file")
            self.root.destroy()
            return

        # Get the video width and height
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Calculate the canvas size while maintaining the aspect ratio
        self.max_width = 800  # You can adjust this value
        self.max_height = int(self.max_width * (self.height / self.width))

        # Display the author information
        author_label = tk.Label(self.root, text="AHMAD MAULANA 220511138")
        author_label.pack(pady=10)

        # Create a canvas to display the video frames
        self.canvas = tk.Canvas(root, width=self.max_width, height=self.max_height)
        self.canvas.pack()

        # Bind the 'q' key to close the application
        self.root.bind('q', self.close_app)

        # Start the video playback
        self.play_video()

    def play_video(self):
        try:
            # Read the video frames and display them on the canvas
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(frame)
                self.photo = ImageTk.PhotoImage(image=image)
                self.canvas.create_image((self.max_width - image.width) // 2, (self.max_height - image.height) // 2, anchor=tk.NW, image=self.photo)
                self.root.after(25, self.play_video)  # Update every 25 milliseconds
            else:
                self.close_app()
        except Exception as e:
            print(f"Error: {str(e)}")
            self.close_app()

    def close_app(self, event=None):
        # Release the video capture object and destroy the Tkinter window
        if hasattr(self, 'cap'):
            self.cap.release()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()
