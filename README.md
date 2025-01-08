## SIMPLE YOUTUBE TO HIGH-QUALITY WAV

#### Steps to Follow (Mac OS):

1. **Install the YouTube Audio Downloader (yt-dlp)**:  
   Open Terminal and type:  
   `pip install yt_dlp`

2. **Install Homebrew (if you don’t already have it)**:  
   Open Terminal and type:  
   `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

3. **Check if Homebrew is Installed**:  
   Type:  
   `brew --version`  
   *(You should see a version number if it’s installed correctly)*  

4. **Update Homebrew**:  
   Type:  
   `brew update`

5. **Install FFmpeg (an audio tool)**:  
   Type:  
   `brew install ffmpeg`

6. **Check if FFmpeg is Installed**:  
   Type:  
   `ffmpeg`  
   *(You should see FFmpeg details in the Terminal window)*

---

#### Run the Code

1. **Get the Code**:  
   - Copy the Python script into a file named `youtube_to_wav.py`, or  
   - Download/clone the repository if you know how.

2. **Run the Code**:  
   Open Terminal and type:  
   `python youtube_to_wav.py`  

   If your file is in a specific folder, provide the full path. Example:  
   `python /Users/YourName/Documents/youtube_to_wav.py`

3. **Paste the YouTube Link**:  
   The script will ask for the **YouTube video URL**. Paste the link and hit **Enter**.

---

### Why This Method Provides the Best Audio Quality

1. **FFmpeg (Audio Tool)**:  
   - Converts audio without losing any quality.  
   - Keeps the original sound clarity by preserving the bitrate.

2. **yt-dlp (Downloader)**:  
   - Downloads the exact **original audio** directly from YouTube.  
   - Avoids unnecessary conversions that can lower the quality(what we don't want).

3. **Direct WAV Format**:  
   - The audio is saved as **WAV**, a format that preserves all audio details without compression.  
   - Other formats (like `.mp3`) reduce quality by shrinking the file size—WAV keeps it crystal clear.

---

### What You’ll Get:
A **high-quality WAV audio file** named `output.wav` in the same folder as the script.

