# ------ IMPORTS --------
from storage import load_sessions
from storage import save_sessions
from analytics import compute_average
from engine import recommend
from analytics import analyze_trends
from analytics import performance_score
from analytics import update_streak
from analytics import session_summary
from datetime import datetime
from analytics import temporal_patterns
from analytics import forecast_state
from reflection import generate_reflection
from moment_engine import classify_moment
from analytics import extract_life_states, classify_life_phase
from response_gate import decide_gate
from tempo import EmotionalTempo
from presence import PresenceEngine
from voice_engine import VoiceEngine
from temporal_engine import TemporalEngine
from greetings import GreetingEngine



# ------ IMPORT ENGINES -------
tempo_engine = EmotionalTempo()
presence_engine = PresenceEngine()
voice = VoiceEngine()
time_engine = TemporalEngine()
greeting_engine = GreetingEngine() 



# Test mode
TEST_MODE = True


sessions = []
sessions = load_sessions()

if TEST_MODE:
    # Quick testing input
    value = input("Rate your energy (1-10): ")
    energy = int(value)

    value = input("Rate your focus (1-10): ")
    focus = int(value)

    for i in range(5):
        current_datetime = datetime.now() 
        formatted_time = current_datetime.strftime("%H:%M:%S")

        session_performance = (energy + focus) / 2

        if energy < 4 or focus < 4: 
            risk_level = "High"
        elif energy >= 7 and focus >= 7: 
            risk_level = "Low"
        else :  
            risk_level = "Medium" 

        derived_state = {
            "Perfoemance Score" : round(session_performance, 2),
            "Risk level" : risk_level
        }

        session = {
            "energy": energy,
            "focus": focus,
            "timestamp": formatted_time,
            "derived_state": derived_state
        }

        moment_signature = classify_moment(session, sessions)
        session["moment"] = moment_signature
        sessions.append(session)

else:
    # Full real input mode
    for i in range(5):
        ...
        # (keep your existing original loop here)


current_datetime = datetime.now() 
formatted_time = current_datetime.strftime("%H:%M:%S")

 # Session performance 
session_performance = (energy + focus) / 2
 
 # Risk level logic
if energy < 4 or focus < 4: 
    risk_level = "High"
elif energy >= 7 and focus >= 7: 
    risk_level = "Low"
else :  
    risk_level = "Medium" 
 
 # Derived state
derived_state = {
    "Perfoemance Score" : round(session_performance, 2)  ,
     "Risk level" : risk_level
}

 # Final session object
session = {"energy" : energy ,
            "focus" : focus ,
            "timestamp" : formatted_time,
            "derived_state" : derived_state
}
moment_signature = classify_moment(session, sessions)
session["moment"] = moment_signature
sessions.append(session)
session_include = (formatted_time)


save_sessions(sessions)


pattern_message = temporal_patterns(sessions)
avg_energy , avg_focus = compute_average(sessions)
Performance_score = performance_score(avg_energy, avg_focus)
recommendation = recommend(avg_energy, avg_focus)
trend_message = analyze_trends(sessions)
streak = update_streak(sessions)
summary = session_summary(sessions)

# --- Temporal Engine ---
time_state = time_engine.describe_time()

# --- Greeting Engine ---
greeting = greeting_engine.generate(time_state)
print("\nDestiny:", greeting)

# --- User input ---
user_text = input("\nYou:")

# --- TEMPO ---
current_tempo = tempo_engine.analyze(user_text)

# --- LIFE STATE + PHASE ---
life_states = extract_life_states(sessions)
life_phase = classify_life_phase(life_states)

# --- Forecast State ---
forecast = forecast_state(sessions)
stability = forecast.get("stability", "Stable")
burnout_risk = forecast.get("burnout", "Low")

# --- RESPONSE GATE ---
gate = decide_gate(current_tempo, life_phase, stability, burnout_risk)

# --- PRESENCE ENGINE ---
presence_state = presence_engine.decides(current_tempo, life_phase, stability, burnout_risk)
presence_text = presence_engine.presence_message(presence_state)

# --- OUTPUT CONTROL ---
if gate["mode"] == "QUIET_MODE":
    from silence_engine import SilenceEngine
    silence_engine = SilenceEngine()
    silence_text = silence_engine.message(gate["silence_style"])

    if silence_text:
        print("\nDestiny:", silence_text)
    else:
        print("\nDestiny")
else:
    reflection_message = generate_reflection(sessions, forecast)
    print("\nDestiny:", reflection_message)

# --- DEBUG / EXPLANATION LAYER ---
print("Life States:", life_states)
print("Life Phase:", life_phase)


















