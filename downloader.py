import yt_dlp

def download_video(url: str, output_path: str = "downloads/%(title)s.%(ext)s"):
    ydl_opts = {
        'outtmpl': output_path,
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading from: {url}")
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter video URL: ")
    download_video(video_url)
