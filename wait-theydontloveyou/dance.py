import tkinter as tk
import threading
import pygame  # For audio playback

def play_audio_in_background():
    """Play the audio file in a loop."""
    pygame.mixer.init()
    pygame.mixer.music.load("audio.mp3")  # Replace with your audio file path
    pygame.mixer.music.play(loops=-1)  # Loop indefinitely

def start_flipbook():
    """Control the image display sequence."""
    # Timings in milliseconds
    image1_duration = 1848  # 1.75 seconds for image1
    video_duration = 2080   # 2.15 seconds for alternating image2 and image3
    frame_interval = 100    # Interval for alternation between image2 and image3 (in ms)

    def display_image1():
        """Show image1 for a fixed duration."""
        img = tk.PhotoImage(file="photo1.png")  # Replace with your image file path
        label.config(image=img)
        label.image = img
        # After showing image1, start the video loop
        root.after(image1_duration, start_video_loop)

    def start_video_loop():
        """Alternate between image2 and image3 for a fixed duration."""
        start_time = root.winfo_toplevel().after_idle(lambda: None)
        
        def alternate_frames(frame_time=0):
            if (frame_time // frame_interval) % 2 == 0:
                img = tk.PhotoImage(file="photo2.png")  # Show image2
            else:
                img = tk.PhotoImage(file="photo3.png")  # Show image3
            
            label.config(image=img)
            label.image = img

            # If within video duration, continue alternating frames
            if frame_time < video_duration:
                root.after(frame_interval, alternate_frames, frame_time + frame_interval)
            else:
                display_image1()  # After video loop, go back to image1

        alternate_frames()  # Start the alternation

    display_image1()  # Start with image1

# Create the main Tkinter window
root = tk.Tk()
root.title("Wait they don't love you like I love you")

# Create a label to display images
label = tk.Label(root)
label.pack()

# Start audio in a separate thread
threading.Thread(target=play_audio_in_background, daemon=True).start()

# Start the flipbook
start_flipbook()

# Run the application
root.mainloop()
