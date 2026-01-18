# Storm v2 Modules Documentation

## Voice Module

### assistant_loop.py
Enhanced main orchestration module with context integration:
- Maintains backward compatibility with v1 functionality
- Integrates with new context state system
- Updates desktop UI state through set_ui_state()
- Removed overlay dependency, now uses web-based UI
- Prints context state for debugging purposes
- Coordinates with focus actions for productivity features

### wake_word.py
Implements wake word detection using Vosk speech recognition:
- Continuously listens for activation keywords ('hey storm')
- Uses offline speech recognition for privacy
- Provides callback when wake word is detected
- Handles audio stream processing

### live_stt.py
Real-time speech-to-text conversion:
- Records audio from microphone
- Processes audio chunks in real-time
- Converts speech to text using Vosk
- Implements silence detection to end recording
- Handles audio quality and noise filtering

### live_tts.py
Text-to-speech synthesis using Piper (neural text-to-speech system):
- Converts text responses to audible speech
- Uses Piper for high-quality voice synthesis
- Manages voice properties (rate, volume, pitch)
- Handles speech interruption capabilities
- Uses temporary WAV files and sounddevice for audio playback

### interrupt.py
Provides interruption mechanism:
- Allows user to interrupt ongoing speech
- Uses threading Event for coordination
- Integrates with keyboard input for spacebar interrupt
- Enables responsive user interaction

## Context Module

### tracker.py
Real-time application monitoring system:
- Uses win32gui to get foreground window
- Uses win32process to get process IDs
- Uses psutil to get process names
- Continuously polls active applications every second
- Updates context state when application changes
- Tracks duration spent in each application
- Integrates with category classification system

### state.py
Context state management:
- Maintains active application information
- Tracks window title and category
- Records start time and duration
- Shared state dictionary accessed by all context-aware components

### categories.py
Application classification system:
- Defines productive applications (code editors, terminals, etc.)
- Defines distraction applications (browsers, media players, etc.)
- Implements categorize() function to classify applications
- Uses application name and window title for classification
- Returns category labels (productive, distraction, neutral, unknown)

## Control Module

### watchdog.py
Focus enforcement monitor:
- Runs enforcement checks every 2 seconds
- Calls enforce_focus() function continuously
- Runs as daemon thread for continuous monitoring
- Part of the seven-thread architecture

### enforcer.py
Application termination system:
- Uses win32gui to enumerate all windows
- Uses psutil to get process information
- Implements get_user_opened_apps() to identify running applications
- Implements enforce_focus() to terminate unauthorized applications
- Only operates when focus mode is enabled
- Compares running apps against allowed applications list

### focus_state.py
Focus mode state management:
- Tracks whether focus mode is enabled
- Maintains set of allowed applications
- Records reason for focus mode activation
- Stores start timestamp for focus session

### actions.py
Focus mode control functions:
- enable_focus() activates focus mode with configurable parameters
- disable_focus() deactivates focus mode
- Integrates with task detection to customize allowed applications
- Updates focus state with reason and timestamp

### task_detector.py
Activity identification system:
- Analyzes active application and window title
- Identifies coding, writing, studying, design, and other tasks
- Returns task category for profile selection
- Uses context state to access current application information

### task_profiles.py
Task-specific application allowances:
- Defines allowed applications for coding tasks
- Defines allowed applications for studying tasks
- Defines allowed applications for writing tasks
- Defines allowed applications for design tasks
- Used by focus system to customize permitted applications

### rules.py
Default allowed applications configuration:
- Defines applications always permitted during focus mode
- Includes development tools, file explorer, and browsers
- Serves as base set for focus enforcement

## Personality Module

### engine.py
Behavioral intervention system:
- Runs personality interventions every minute
- Analyzes context category and duration
- Implements distraction strike counting system
- Provides encouraging feedback for productive behavior
- Uses cooldown period to prevent over-intervention
- Integrates with TTS for personality-driven responses
- Tracks distraction strikes and focus successes

### state.py
Personality metrics tracking:
- Tracks time of last intervention
- Counts distraction strikes
- Records focus successes
- Maintains personality behavior metrics

### traits.py
Personality characteristic configuration:
- Defines patience level (0.7)
- Defines strictness level (0.6)
- Defines humor level (0.4)
- Defines support level (0.8)
- Influences personality engine behavior

## Guidance Module

### engine.py
Productivity coaching system:
- Runs guidance checks every 30 seconds
- Evaluates rules against current context
- Implements cooldown system to prevent repetitive interventions
- Triggers TTS messages based on rule conditions
- Tracks last triggered times for each rule

### rules.py
Guidance rule definitions:
- Defines distraction intervention after 15 minutes
- Defines idle state intervention after 10 minutes
- Specifies message content for each rule
- Configures cooldown periods between interventions
- Sets minimum duration thresholds for triggers

## Desktop UI Module

### server.py
Web-based UI server:
- Implements Flask web server
- Provides CORS support for cross-origin requests
- Exposes `/state` endpoint for UI state
- Returns JSON representation of UI state
- Runs on localhost:8765
- Uses threading to run alongside other system components

### state.py
Thread-safe UI state management:
- Maintains UI state dictionary with mode, focus, listening, speaking flags
- Uses threading.Lock for concurrent access safety
- Implements get_ui_state() for safe state retrieval
- Implements set_ui_state() for safe state updates

### walpaper/index.html
HTML structure for animated desktop interface:
- Contains animated eye elements
- Implements HUD containers for status indicators
- Provides focus overlay for enforcement visualization
- Links CSS and JavaScript assets
- Responsive design for desktop wallpaper use

### walpaper/style.css
Styling for animated interface:
- Defines eye appearance and glow effects
- Implements different states (calm, alert, narrow, sleep)
- Provides CSS animations for eye behaviors
- Creates focus overlay for enforcement visualization
- Uses CSS variables for theme customization
- Implements sonar and blink animations

### walpaper/eyes.js
Client-side UI state synchronization:
- Polls server for state updates every 300ms
- Implements loadState() to fetch UI state
- Updates visual appearance based on system state
- Maps system modes to visual states (idle, speaking, enforcement)
- Handles error cases gracefully

## System Modules (from v1, retained)

### command_router.py
Retained from v1 with same functionality for backward compatibility.

### validator.py
Retained from v1 with same functionality for backward compatibility.

### security.py
Retained from v1 with same functionality for backward compatibility.

## LLM Module (from v1, retained)

### model.py
Retained from v1 with same functionality for backward compatibility.

### parser_llm.py
Retained from v1 with same functionality for backward compatibility.

## RAG Module (from v1, retained)

### ingest.py
Retained from v1 with same functionality for backward compatibility.

### query.py
Retained from v1 with same functionality for backward compatibility.

## Memory Module (from v1, retained)

### controller.py
Retained from v1 with same functionality for backward compatibility.

### store.py
Retained from v1 with same functionality for backward compatibility.

### reminders.py
Retained from v1 with same functionality for backward compatibility.

## Main Module

### main.py
Enhanced entry point with additional subsystems:
- Maintains graceful shutdown handling
- Adds threads for new subsystems (context, guidance, watchdog, personality, UI server)
- Preserves all v1 threading model
- Adds seven new threads for enhanced functionality
- Maintains signal handling for proper cleanup

## Test Module

### test.py
Development testing file containing experimental code and AI prompting examples.