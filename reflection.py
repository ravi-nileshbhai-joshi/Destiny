import json
from datetime import datetime

def load_reflection_memory():
    try:
        with open("reflection_memory.json", "r") as file:
            return json.load(file)
    except:
        return {}

def save_reflection_memory(memory):
    with open("reflection_memory.json", "w") as file: 
        json.dump(memory, file, indent= 4)

def generate_reflection(sessions, preparedness):
    memory = load_reflection_memory()

    current_moment = sessions[-1].get("moment", {})
    core = current_moment.get("core", "")
    modifiers = current_moment.get("modifiers", [])


    if len(sessions) < 2:
        return "Let today unfold naturally. When you're ready, we continue."
    
    today = sessions[-1]
    yesterday = sessions[-2]
    
    today_score = (today["energy"] + today["focus"]) / 2
    yesterday_score = (yesterday["energy"] + yesterday["focus"]) / 2
    delta = round(today_score - yesterday_score, 2)

    trend = preparedness.get("trend", "stable")
    mode = preparedness.get("mode", "steady")

    # --- CONDITION AWARENESS ---
    if today_score >= 7:
        condition = "high"
    elif today_score >= 5:
        condition = "medium"
    else:
        condition = "low"
    
    today_context = {
        "condition" : condition,
        "trend" : trend,
        "mode" : mode
    }
    
    # --- REFLECTING LOGIC ---

    # Low condition + improving  
    
    if today["energy"] < 4 or today["focus"] < 4:
            reflection = "Today is asking for a gentler pace. Rest will sharpen tomorrow."

    elif core == "MEANINGFUL" and "BUILDING" in modifiers:
        reflection = "You're in a powerful building phase. Stay with this momentum."
   
    elif condition == "low" and delta > 0.5:
        reflection = "You're recovering from a heavy stretch. Let this improvement settle."
    
    elif delta < -0.5:
        if condition == "high":
            reflection = "You've slowed slightly from yesterday. A steady pace will restore your flow."
        else: 
            reflection = "Today feels heavier than yesterday. A lighter approach will help."
   
    elif abs (delta) <= 0.5:
        if condition == "high":
            reflection = "Your consistency is becoming a strength. Stay with this rhythm."
        elif condition == "medium":
            reflection = "You're steady. Keep moving with intention."
        else:
            reflection = "You're holding things together. Give yourself some breathing room."

   
    else: 
        reflection = "You're steady. Let the day shape itself."

    # --- Recovery persistence check ---
    recent = sessions[-5:]
    low_count = sum(
    1 for s in recent
    if (s["energy"] + s["focus"]) / 2 < 4
    )

    if low_count >= 4:
       reflection = (
        "You've been carrying a heavy stretch for a while. "
        "A small meaningful action — even ten minutes — can begin a shift."
    )

    # --- Non-repetition memory check ---
    last_context = memory.get("context")
    last_message = memory.get("message")

   # --- Non-repetition memory check ---
    if last_context == today_context and last_message == reflection and low_count < 4:
        save_reflection_memory({
            "context" : today_context,
            "message" : reflection,
            "time" : str(datetime.now())})
        return ""

    # --- Save new memory ---
    save_reflection_memory({
        "context" : today_context,
        "message" : reflection,
        "time" : str(datetime.now())
    })
    return reflection

