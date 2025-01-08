import os
import yt_dlp


def download_and_convert_to_wav(youtube_url, output_path=None):
    try:
        # If no output path specified, use current directory
        if output_path is None:
            output_path = os.getcwd()

        # Configure yt-dlp options
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
            }],
            'prefer_ffmpeg': True,
            'keepvideo': False
        }

        # Download and convert
        print("Downloading and converting to WAV...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=True)
            wav_filename = os.path.join(output_path, f"{info['title']}.wav")

        print(f"Successfully converted to WAV: {wav_filename}")
        return wav_filename

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def main():
    # Get YouTube URL from user
    url = input("Enter YouTube video URL: ")

    # Get output path (optional)
    output_path = input("Enter output path (press Enter for current directory): ").strip()
    if output_path == "":
        output_path = None

    # Download and convert
    result = download_and_convert_to_wav(url, output_path)

    if result:
        print("\nConversion completed successfully!")
    else:
        print("\nConversion failed!")


if __name__ == "__main__":
    main()
