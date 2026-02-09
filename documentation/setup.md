# Storm Setup Guide

This guide provides detailed instructions for setting up Storm on your system.

## Prerequisites

- **Python 3.8+** installed on your system
- **Windows 10/11** (for desktop UI and win32 features)
- **pip** or **uv** package manager
- **Audio Input/Output devices** (microphone and speakers)
- **Internet connection** (for initial setup and downloads)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/storm.git
cd storm
```

### 2. Set Up Models Directory

The models directory is **required** for speech recognition to work.

#### Directory Structure

```
Storm/
├── models/
│   └── vosk/
│       └── vosk-model-en-in-0.5/
│           ├── am/
│           ├── conf/
│           ├── graph/
│           ├── ivector/
│           ├── rescore/
│           └── README
└── ... (other folders)
```

#### Getting the Vosk Model

1. Download the English (India) Vosk model from [Vosk Models](https://alphacephei.com/vosk/models):
   - **Recommended**: `vosk-model-en-in-0.5.zip` (approximately 47MB)
   - Alternative: `vosk-model-en-us-0.22.zip` for US English

2. Extract the downloaded ZIP file to `models/vosk/`:
   ```bash
   # On Windows PowerShell
   Expand-Archive -Path vosk-model-en-in-0.5.zip -DestinationPath models/vosk/
   ```

3. Verify the installation:
   ```
   models/vosk/vosk-model-en-in-0.5/README
   ```
   Should exist and contain model information.

### 3. Install Python Dependencies

Using pip (standard):
```bash
pip install -r requirements.txt
```

Or using uv (faster):
```bash
uv pip install -r requirements.txt
```

### 4. Install Windows-Specific Dependencies

The system requires some Windows-specific packages:

```bash
pip install pywin32
python -m pip install pyaudio  # For audio processing
```

If you encounter issues with PyAudio on Windows:
- Install [Visual C++ redistributables](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads)
- Or use pre-built wheels from [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/)

### 5. Verify Installation

Test that all components are properly installed:

```bash
# Test Vosk model loading
python -c "from vosk import Model, KaldiRecognizer; print('Vosk OK')"

# Test PyAudio
python -c "import pyaudio; print('PyAudio OK')"

# Test other dependencies
python -c "import pyttsx3; import keyboard; import psutil; print('Dependencies OK')"
```

## Configuration

### Audio Device Selection

If you have multiple audio input/output devices, you may need to configure which ones Storm uses.

1. List available audio devices:
   ```bash
   python -c "import pyaudio; p = pyaudio.PyAudio(); [print(f'{i}: {p.get_device_info_by_index(i)[\"name\"]}') for i in range(p.get_device_count())]"
   ```

2. Update the device IDs in `voice/live_stt.py` and `voice/live_tts.py` if needed.

### Desktop UI (Lively Wallpaper)

To use Storm's animated desktop interface:

1. Install [Lively Wallpaper](https://rocksdanister.github.io/lively/)
2. Copy the contents of `desktop_ui/walpaper/` to a folder on your system
3. In Lively Wallpaper, add a new "Website" wallpaper
4. Point to the `index.html` file from the walpaper folder

## Running Storm

### Start the Application

```bash
python main.py
```

You should see:
```
Loading Vosk model...
Model loaded successfully
Storm Online.
Waiting for wake word activation...
```

### Basic Usage

1. **Wake Word**: Say "Hey Storm" to activate
2. **Command**: After the "How may I help you?" prompt, issue your command
3. **Response**: The system will respond with voice feedback
4. **Desktop UI**: The animated wallpaper (if configured) will reflect the system state

### Supported Commands

- **Application Control**: "Open Chrome", "Close Notepad"
- **Memory**: "Remember my name is John", "Recall my name"
- **Reminders**: "Remind me to call mom at 5 PM"
- **Search**: "Search for Python tutorials"
- **Focus Mode**: "Enable focus mode"
- **Status**: "What's my context"

## Troubleshooting

### Vosk Model Not Found

**Error**: `Exception: Could not open model`

**Solution**:
```bash
# Verify the model path
ls models/vosk/vosk-model-en-in-0.5/README

# If missing, re-download and extract the model
```

### PyAudio Installation Issues

**Error**: `error: Microsoft Visual C++ 14.0 or greater is required`

**Solutions**:
1. Install Visual C++ Build Tools from Microsoft
2. Use pre-built PyAudio wheels
3. Use conda instead: `conda install pyaudio`

### Microphone Not Detected

**Error**: `No input devices found` or no audio input

**Solutions**:
1. Check System Settings → Sound → Input devices
2. Set a default microphone in Windows
3. Run as Administrator: `python main.py`
4. Check device ID and update `voice/live_stt.py`

### Wake Word Not Detecting

**Possible causes**:
1. Microphone sensitivity too low
2. Background noise too high
3. Speaking too quietly
4. Model language mismatch

**Solutions**:
- Speak clearly at normal volume
- Use in a quiet environment
- Check microphone levels in System Settings

### Focus Mode Not Working

**Possible causes**:
1. Need to run with Administrator privileges
2. Application names not correctly configured

**Solutions**:
```bash
# Run as Administrator
python -m pip install pywin32
python -m pip install pywin32-ctypes

# Run with admin privileges
python main.py  # (run as Administrator in PowerShell)
```

## System Requirements

### Minimum

- **CPU**: Intel i5 or equivalent
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 500MB free (including model)
- **Microphone**: Built-in or USB
- **Speakers**: Built-in or external

### Recommended

- **CPU**: Intel i7 or AMD Ryzen 5+
- **RAM**: 8GB+
- **Storage**: 1GB+ free
- **Microphone**: Dedicated USB microphone for better quality
- **Display**: Dual monitors or high resolution for optimal desktop UI experience

## Performance Notes

- Vosk model requires ~100-200MB RAM during operation
- Context tracking adds ~1-2% CPU overhead
- Focus enforcement monitoring uses minimal resources (~0.5% CPU)
- Web UI server uses negligible resources

## Security Considerations

- All voice processing happens locally on your machine
- No data is sent to external servers by default
- Database files (`memory.json`, `reminders.json`, `chroma.sqlite3`) are stored locally
- Administrator privileges are required for focus enforcement features

## Next Steps

- Read [Architecture Documentation](architecture.md) for system design details
- Review [Modules Documentation](modules.md) for component information
- Check [Overview](overview.md) for feature summary
- Explore the codebase in `main.py` for entry point and threading model

## Getting Help

If you encounter issues:

1. Check the troubleshooting section above
2. Review console output for specific error messages
3. Verify all models are properly downloaded and extracted
4. Ensure you're running on Windows 10/11
5. Run with Administrator privileges if you get permission errors
