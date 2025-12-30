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


sessions = []
sessions = load_sessions()

for i in range (5):
 while True:
    value = input("Rate your energy (1-10): ")
    if value.isdigit() and 1 <= int(value) <= 10:
       energy = int(value)
       break
    else: 
       print("Please enter a number between 1 and 10")

 while True: 
    value = input("Rate your focus (1-10): ")
    if value.isdigit() and 1 <= int(value) <=10:
       focus = int(value)
       break
    else:
       print("Please enter a number between 1 and 10")

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
forecast = forecast_state(sessions)



print("\nPreparedness Forecast")
print("Guidance:", forecast["message"])






