# Storm v2 Architecture

## System Architecture

Storm v2 introduces a significantly enhanced architecture compared to v1, with additional subsystems focused on contextual awareness and user productivity enhancement. The system maintains backward compatibility while adding advanced behavioral and productivity features.

### Enhanced Component Interaction Diagram
```
[User Behavior] → [Context Tracker] → [Task Detection] → [Focus Enforcement]
       ↑                ↓                  ↓                ↓
[Active Apps] ← [Window Monitoring] ← [Application Classification] ← [Behavior Analysis]

[User Voice Input] → [Wake Word Detection] → [STT Processing] → [Command Parsing]
         ↓                                               ↓              ↓
[Animated UI] ← [TTS Output] ← [Response Generation] ← [Command Execution]
         ↑                                    ↓
[Personality Engine] ← [Guidance System] ← [Intervention Logic]
```

## Enhanced Threading Model

Storm v2 utilizes a more complex multi-threading approach with seven concurrent threads:

1. **Reminder Thread**: Monitors and delivers scheduled reminders (reminders.py)
2. **Context Thread**: Tracks active applications and user behavior (tracker.py)
3. **Guidance Thread**: Provides productivity coaching and interventions (engine.py)
4. **Watchdog Thread**: Monitors and enforces focus mode (watchdog.py)
5. **Personality Thread**: Manages personality-driven interactions (engine.py)
6. **UI Server Thread**: Runs web server for animated desktop interface (server.py)
7. **Assistant Loop**: Main voice interaction loop (assistant_loop.py)

## New Subsystems Architecture

### Context Awareness System

The context system continuously monitors user activity:
```
[Active Window Detection] → [Application Classification] → [Category Assignment] → [Duration Tracking]
        ↓                        ↓                           ↓                      ↓
   win32gui & psutil      Productive/Distraction       Behavior Pattern      Time-Based Actions
```

- **Window Monitoring**: Uses win32gui and win32process to identify active applications
- **Classification**: Categorizes applications as productive, distraction, or neutral
- **Duration Tracking**: Measures time spent in each context
- **State Management**: Maintains context state for other subsystems

### Focus Enforcement System

The focus system actively manages user productivity:
```
[Focus State] → [Allowed Apps] → [Process Monitoring] → [Unauthorized Termination]
      ↑               ↑                  ↑                      ↑
[Enable/Disable] [Task Profile] [Active Applications] [Enforcement Action]
```

- **State Management**: Tracks focus mode activation and configuration
- **Task Profiling**: Adapts allowed applications based on detected task
- **Process Monitoring**: Enumerates all running processes
- **Enforcement**: Terminates unauthorized applications during focus mode

### Personality Engine

The personality system drives human-like interactions:
```
[Context Analysis] → [Behavior Assessment] → [Intervention Decision] → [Personality Expression]
        ↓                   ↓                      ↓                       ↓
   Current Activity    User Engagement      Appropriate Response      Verbal Feedback
```

- **Behavior Monitoring**: Analyzes user engagement patterns
- **Intervention Logic**: Decides when to provide encouragement or warnings
- **Personality Metrics**: Tracks distraction strikes and focus successes
- **Coordinated Responses**: Integrates with TTS for personality-driven feedback

### Guidance System

The guidance system provides productivity coaching:
```
[Rule Evaluation] → [Trigger Conditions] → [Message Delivery] → [Cooldown Management]
        ↑                  ↑                    ↑                    ↑
   Context State    Duration/Category    Personality Engine    Timing Control
```

- **Rule-Based Logic**: Defines productivity interventions based on behavior
- **Condition Checking**: Evaluates context and duration thresholds
- **Timed Interventions**: Manages cooldown periods to prevent over-intervention

## UI Architecture

### Web-Based Interface
```
[Flask Server] ↔ [JSON API] ↔ [JavaScript Client] → [CSS Animations]
      ↓              ↓              ↓                 ↓
[Python State] → [HTTP Requests] → [DOM Updates] → [Visual Feedback]
```

- **Server Component**: Flask API serving UI state
- **Client Component**: JavaScript polling for state updates
- **Visual Layer**: Animated CSS elements reflecting system state
- **State Synchronization**: Real-time updates between system and UI

## Integration Architecture

All subsystems integrate seamlessly with the existing v1 architecture:
- Voice processing maintains the same pipeline
- Memory and command routing preserved
- New context information feeds into existing components
- UI state management enhanced with new features

## Data Flow Architecture

Enhanced data flows in Storm v2:
1. **Context Flow**: Window → Classification → Context State → Subsystems
2. **Focus Flow**: Task Detection → Profile Selection → Enforcement → Process Control
3. **Guidance Flow**: Context + Duration → Rule Evaluation → Intervention → Feedback
4. **Personality Flow**: Behavior Analysis → Trait Application → Response Generation
5. **UI Flow**: System State → HTTP API → Client Updates → Visual Animation

This architecture creates a comprehensive productivity ecosystem that goes beyond simple voice assistance to provide intelligent, context-aware support for user focus and productivity.