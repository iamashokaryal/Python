import tkinter as tk
from tkinter import messagebox
from yt_dlp import YoutubeDL

# Function to handle the download process
def download_playlist():
    playlist_link = playlist_entry.get()
    if not playlist_link:
        messagebox.showerror("Error", "Please enter a valid YouTube playlist link.")
        return

    # Set download options
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',  # Save videos with the title as the filename
        'noplaylist': False,             # Ensure the whole playlist is downloaded
    }

    # Update status label
    status_label.config(text="Downloading...")
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_link])
        status_label.config(text="Download complete!")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("YouTube Playlist Downloader")

# Create and place the widgets
tk.Label(root, text="Enter YouTube Playlist Link:").pack(pady=10)
playlist_entry = tk.Entry(root, width=50)
playlist_entry.pack(pady=5)

# Download button
download_button = tk.Button(root, text="Download Playlist", command=download_playlist)
download_button.pack(pady=10)

# Status label
status_label = tk.Label(root, text="", fg="green")
status_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
