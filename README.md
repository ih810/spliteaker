# Split Speaker (Spliteaker)

This project extracts audio from a video, performs speaker diarization, and splits the audio into separate files for each speaker.

## Prerequisites

- Python 3.7 or higher
- `ffmpeg` installed on your system

## Setup

Follow these steps to set up the project in a virtual environment:

### 1. Clone the Repository

```
git clone git@github.com:ih810/spliteaker.git

cd spliteaker
```
### 2. Create and Activate a Virtual Environment

On Windows
```
python -m venv venv
venv\Scripts\activate
```

On macOS and Linux
```
python3 -m venv venv
source venv/bin/activate
```
### 3. Upgrade pip
```
pip install --upgrade pip
```
### 4. Install the Required Packages
```
pip install -r requirements.txt
```
### 5. Place Your Video File   
Place your video file in the data directory and name it input_video.mp4. You can change the file name, but make sure to update the script accordingly.

### 6. Run the Script
```
python src/main.py
```
This will extract audio from the video, perform speaker diarization, and save each speaker's audio to separate files in the data directory.

Project Structure
```
spliteaker/  
├── venv/  
├── src/  
│   ├── __init__.py  
│   ├── main.py  
├── data/  
│   ├── input_video.mp4  
│   ├── output_audio.wav  
├── requirements.txt  
└── README.md  
```
venv/: The virtual environment directory.  
src/: The source code directory.  
main.py: The main script to run the project.  
data/: Directory to store input video and output audio files.  
requirements.txt: File listing the required Python packages.  
README.md: This file.  
### 7. Troubleshooting  
Common Issues    
  
ModuleNotFoundError: Make sure you have activated your virtual environment.  
File Not Found: Ensure that your input_video.mp4 is in the data directory.  
Verifying ffmpeg Installation  
To verify ffmpeg is installed and accessible, run:  
```
ffmpeg -version
```
You should see the version information for ffmpeg.