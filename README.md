# Storm v2 - AI Voice Assistant with Productivity Enhancement

Storm v2 is an advanced evolution of the AI-powered personal assistant system, featuring enhanced contextual awareness, focus enforcement capabilities, and an immersive desktop interface. The system builds upon v1's foundation with significant improvements in user productivity, contextual intelligence, and behavioral guidance.

## Features

- 🎤 **Voice Activation**: Enhanced wake word detection for hands-free operation
- 🗣️ **Speech Recognition**: Real-time speech-to-text conversion
- 💬 **Natural Language Processing**: Understands and processes natural language commands
- 📢 **Text-to-Speech**: Clear, synthesized voice responses
- 🖥️ **Application Control**: Open and close applications on demand
- 📝 **Memory System**: Remember and recall information
- ⏰ **Reminders**: Schedule and receive time-based notifications
- 🎯 **Command Routing**: Intelligent command execution system
- 🛡️ **Security**: Validation and safety checks for all commands
- 🧠 **Context Awareness**: Real-time monitoring of active applications
- 🎯 **Focus Enforcement**: Automatic termination of distracting applications during focus mode
- 😊 **Personality Engine**: Personalized user engagement with behavioral interventions
- 👨‍🏫 **Guidance System**: Productivity coaching and advice
- 🎨 **Immersive UI**: Animated desktop wallpaper with expressive eyes
- 🔍 **Task Profiling**: Adaptive application allowances based on detected activities
- 📊 **Behavioral Analytics**: Insights into user productivity patterns

## Architecture

Storm v2 maintains the modular architecture of v1 while introducing several new subsystems:

- **Enhanced Voice Module**: Improved speech processing pipeline
- **Context Tracker**: Monitors active applications and user behavior
- **Focus Control System**: Enforces productivity through application management
- **Personality Engine**: Drives personalized user interactions
- **Guidance System**: Provides productivity coaching and interventions
- **Desktop UI Server**: Web-based interface with animated elements
- **Task Profiling System**: Detects and adapts to user activities
- **All v1 components**: Retained and enhanced functionality

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt` (or use uv if configured)
3. **Set up the models directory**:
   - Create a `models/` folder in the project root if it doesn't exist
   - Add the Vosk speech recognition model: `models/vosk/vosk-model-en-in-0.5/`
   - You can download the model from [Vosk Models](https://alphacephei.com/vosk/models) (English India model recommended)
4. Install additional dependencies for Windows-specific features
5. Run the application: `python main.py`

## Dependencies

### Core Dependencies (from v1)
- `vosk` - Offline speech recognition
- `pyttsx3` - Text-to-speech synthesis
- `pyaudio` - Audio processing
- `langchain` and related packages - LLM integration
- `chromadb` - Vector storage for RAG
- `appopener` - Application control
- `keyboard` and `pyautogui` - System interaction
- `psutil` - System monitoring

### New Dependencies (v2 specific)
- `flask` - Web server for UI
- `flask-cors` - Cross-origin resource sharing
- `pywin32` - Windows-specific GUI operations (win32gui, win32process)

## Usage

1. Start the application with `python main.py`
2. Wait for the "Storm Online." message
3. Say "Hey Storm" to activate the wake word detection
4. Issue your command after hearing "How may I help you?"
5. Receive voice response from the assistant
6. The system will now monitor your active applications and provide productivity guidance

## Lively Wallpaper Integration

Storm v2 includes an animated desktop interface located in the `desktop_ui/walpaper/` folder. To use this as a Lively Wallpaper:

1. Download and install [Lively Wallpaper](https://rocksdanister.github.io/lively/) from the official website
2. Copy the contents of the `desktop_ui/walpaper/` folder to a convenient location
3. In Lively Wallpaper settings, add a new "Website" wallpaper
4. Point it to the `index.html` file in the walpaper folder
5. The animated eyes will now appear as your desktop wallpaper, synchronized with Storm's status

The animated interface will reflect the system state:
- **Idle**: Calm blinking animation
- **Speaking**: Alert/active animation
- **Focus Enforcement**: Narrow stare animation
- **Sleep/Off**: Closed eyes animation

## Commands Supported

### Traditional Commands (from v1)
- **Application Control**: "Open Chrome", "Close Notepad"
- **Memory Operations**: "Remember my name is John", "Recall my phone number"
- **Reminders**: "Remind me to call mom at 5 PM"
- **Web Browsing**: "Open YouTube", "Search for Python tutorials"
- **Text Input**: "Type 'Hello World' in the current window"
- **System Tasks**: "Take a screenshot"

### Enhanced Productivity Commands (v2)
- **Focus Mode**: Activate focus mode to block distractions
- **Task Detection**: System automatically detects your activity type
- **Behavioral Coaching**: Receive productivity tips and encouragement

## New Modules (v2 specific)

### Context Module
- **tracker.py**: Monitors active windows and applications
- **state.py**: Maintains context state
- **categories.py**: Classifies applications as productive/distractions

### Control Module
- **watchdog.py**: Monitors focus enforcement
- **enforcer.py**: Terminates unauthorized applications during focus
- **focus_state.py**: Tracks focus mode state
- **actions.py**: Manages focus mode activation/deactivation
- **task_detector.py**: Detects user activity type
- **task_profiles.py**: Defines application allowances per task
- **rules.py**: Configures default allowed applications

### Personality Module
- **engine.py**: Implements personality-driven interventions
- **state.py**: Tracks personality metrics
- **traits.py**: Configures personality characteristics

### Guidance Module
- **engine.py**: Implements productivity guidance
- **rules.py**: Defines guidance rules and triggers

### Desktop UI Module
- **server.py**: Flask-based UI state server
- **state.py**: Thread-safe UI state management
- **walpaper/**: Animated desktop interface assets

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - See LICENSE file for details.

## Note on Privacy

Storm v2 includes enhanced monitoring capabilities that continuously track your active applications. This enables the context awareness and focus enforcement features. All processing happens locally on your machine, and no data is transmitted externally. However, please be aware of the increased system access required for these advanced features.