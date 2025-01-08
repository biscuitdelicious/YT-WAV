## SIMPLE YOUTUBE TO HIGH QUALITY WAV

#### Commands to run for MAC OS:

1. `pip install yt_dlp`
2. `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
3. `brew --version` -> should print the version
4. `brew update` -> update
5. `brew install ffmpeg`
6. `ffmpeg` -> to confirm it's installed(it should have the window name `FFMPEG`

Then get the code from .py file(or clone the repo if you know).

Run the code in an IDE(PyCharm) or run it via terminal `python youtube_to_wav.py`(or get the directory of the file and replace it with `youtube_to_wav.py`; e.g: `python user/documents/pythonfiles/youtube_to_wav.py`).

Why is this the highest quality?
1. **FFmpeg**: A powerful tool that extracts and converts audio without losing quality. It preserves the original bitrate and uses advanced codecs for the best results.

2. **yt-dlp**: Downloads the original audio directly from YouTube without unnecessary re-encoding. It's an improved version of youtube-dl that supports more formats and ensures higher performance.

3. **Direct WAV Conversion**: The audio is downloaded in its original format (like .m4a or .webm) and converted directly to WAV (a lossless format), ensuring no quality is lost during conversion.




