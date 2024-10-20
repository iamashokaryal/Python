import yt_dlp

# Function to download videos from a playlist with a chosen resolution
def download_playlist(playlist_url, download_path='.', resolution='best'):
    # Set yt-dlp options, including user-defined resolution
    ydl_opts = {
        'format': f'{resolution}',  # User-selected resolution
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
    }

    # Download the playlist
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

# Display resolution options
def get_resolution_choice():
    print("Choose the resolution to download:")
    print("1. Best quality available")
    print("2. 1080p")
    print("3. 720p")
    print("4. 480p")
    print("5. 360p")

    choice = input("Enter the number of your choice (default is best): ")
    
    resolution_map = {
        "1": "best",
        "2": "bestvideo[height<=1080]+bestaudio/best",
        "3": "bestvideo[height<=720]+bestaudio/best",
        "4": "bestvideo[height<=480]+bestaudio/best",
        "5": "bestvideo[height<=360]+bestaudio/best",
    }

    return resolution_map.get(choice, "best")  # Default to best if invalid input

# Replace with your playlist link
playlist_link = input("Enter the YouTube playlist link: ")

# Replace with your desired download path
download_folder = './downloads'

# Get the resolution choice from the user
chosen_resolution = get_resolution_choice()

# Call the function to start downloading with the chosen resolution
download_playlist(playlist_link, download_folder, chosen_resolution)
