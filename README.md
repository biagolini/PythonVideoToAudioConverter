# Video to Audio Converter

This project provides a modular and extensible foundation for **converting video files to audio formats** using Python. It is designed to support various video and audio formats, making it suitable for tasks such as transcription, audio extraction, speech analysis, or standalone audio playback.

---

## Project Overview

The project is structured to include individual scripts for specific types of conversions. For example:

- **Audio Conversion** — The script `mp4_wav.py` handles the conversion of `.mp4` files to `.wav` format. It scans a defined `input/` directory for video files and saves the resulting audio in the `output/` directory with matching filenames.

Future scripts may support other input and output formats such as `.mov`, `.avi`, `.mp3`, `.flac`, etc.

---

## Features

- Scans the `input/` directory for supported video formats (e.g., `.mp4`)
- Converts video to audio formats (e.g., `.wav`)
- Saves output in a structured `output/` directory
- Lightweight implementation with minimal dependencies
- Easily extendable to support additional formats and workflows

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- [FFmpeg](https://ffmpeg.org/download.html) must be installed and available in your system's PATH

### Installation

1. **Clone the Repository**
```bash
git clone https://github.com/biagolini/PythonVideoToAudioConverter.git
cd VideoToAudioConverter
```

2. **(Recommended) Set Up a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## Usage

1. Place supported video files (e.g., `.mp4`) into the `input/` directory.
2. Run the appropriate script depending on the conversion type. For example:
```bash
python mp4_wav.py
```
3. Output audio files (e.g., `.wav`) will appear in the `output/` directory.

### Example
If your `input/` directory contains:
```
input/
├── lecture.mp4
├── interview.mp4
```
After running the script:
```
output/
├── lecture.wav
├── interview.wav
```

---

## Project Structure
```
VideoToAudioConverter/
├── mp4_wav.py
├── requirements.txt
├── README.md
├── input/
└── output/
```

---

## Notes
- Ensure `ffmpeg` is properly installed and accessible via the system PATH.
- The project is designed to grow with additional scripts and modules for handling diverse video and audio formats.
- Only files placed in the `input/` directory will be processed.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to add new conversion scripts, features, or documentation improvements.

---

## License

This project is licensed under the MIT License.