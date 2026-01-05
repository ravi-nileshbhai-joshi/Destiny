def compute_average(sessions):
    total_energy = sum(s["energy"] for s in sessions)
    total_focus = sum(s["focus"] for s in sessions)

    avg_energy = total_energy / len(sessions)
    avg_focus = total_focus / len(sessions)

    return avg_energy, avg_focus

def analyze_trends(sessions):
    if len(sessions) < 5:
        return "Not enough data yet."
    
    recent = sessions[-5:]
    avg_energy = sum(s["energy"] for s in recent) / 5
    avg_focus = sum(s["focus"] for s in recent) / 5

    if avg_energy < 4 or avg_focus < 4:
        return "Risk of burnout. Take recovery time."
    elif avg_energy > 7 and avg_focus > 7:
        return "Strong performance trend."
    else:
        return "Stable performance"
    
def performance_score(avg_energy, avg_focus):
    return round((avg_energy + avg_focus) / 2, 2)

def update_streak(sessions):
    streak = 0
    for s in reversed(sessions):
        if s ["energy"] >= 6 and s["focus"] >=6:
            streak += 1
        else:
            break
        return streak

def session_summary(sessions):
    today = sessions[-5:]
    avg_energy = sum(s["energy"] for s in today) / 5
    avg_focus = sum(s["focus"] for s in today) / 5

    best = max(today, key=lambda s: s["energy"] + s["focus"])
    worst = min(today, key=lambda s: s["energy"] + s["focus"])

    return{
        "avg_energy" : round(avg_energy, 2),
        "avg_focus" : round(avg_focus, 2),
        "best" : best,
        "worst" : worst
    }

def temporal_patterns(sessions):
    if len(sessions) < 10:
        return "Not enough data for ttemporal pattern analysis."
    recent = sessions[-10:]

    avg_energy = sum(s["energy"] for s in recent) / 10
    avg_focus = sum(s["focus"] for s in recent) / 10
    
    valid = [s for s in recent if "derived_state" in s and "risk_level" in s["derived_state"]]

    if not valid:
        return "Insufficient derived data for temporal analysis"
    high = sum(1 for s in recent if s ["derived_state"]["risk_level"] == "Low")
    low = sum(1 for s in recent if s["derived_state"]["risk_level"] == "High")

    if high >= 7:
        return "Sustained high performance pattern."
    elif low >=4:
        return "Burnout risk pattern detected."
    else: 
        return "Fluctuating performance pattern."

def forecast_state(sessions):
    if len(sessions) < 5:
        return {
            "burnout" : "Low",
            "stability" : "Stable",
            "mode" : "BUild",
            "message" : "You're just getting started. Establish a steady rhythm and build calmly."

        }
    recent = sessions[-10:] if len(sessions) >= 10 else sessions
    
    moments = [s.get("moment", {}) for s in sessions[-5:]]
    cores = [m.get("core") for m in moments]
    modifiers = [mod for m in moments for mod in m.get("modifiers", [])]
    
    recent_moments = [s.get("moment", {}) for s in sessions[-5:]]
    modifiers = [m for moment in recent_moments for m in moment.get("modifiers", [])]
    cores = [moment.get("core") for moment in recent_moments] 

    recovering_count = modifiers.count("RECOVERING")
    building_count = modifiers.count("BUILDING")
    meaningful_count = cores.count("MEANINGFUL")
    lively_count = cores.count("LIVELY")

    if recovering_count >=3:
        return {
            "mode" : "Re-entry",
            "guidance" : "Let your body come alive first - a walk, some movement, a breath of fresh air. Then, when it feels natural, return to something meaningful"
        } 

    energies = [s["energy"] for s in recent] 
    focuses = [s["focus"] for s in recent]
    risks = [s["derived_state"]["Risk level"] for s in recent if "derived_state" in s]

    avg_energy = sum(energies) / len(energies)
    avg_focus = sum(focuses) / len(focuses)

    variance = max(energies) - min(energies) + max(focuses) - min(focuses)

    stability = "Stable" if variance <=6 else "Unstable"

    high_risk = risks.count("High")
    medium_risk = risks.count("Medium")

    if high_risk >= 3 or avg_energy <= 4:
        burnout = "High"
    elif medium_risk >=3 or avg_energy <= 6:
        burnout = "Medium"
    else:
        burnout = "Low"

    if burnout == "High":
        mode = "Perfect"
        message = "You've been carrying a lot. Let's slow the pace today and protect your energy."
    elif burnout == "Medium":
        mode = "Build"
        message = "You're in a good rhythm. This is a great moment to build momentum."
    else:
        mode = "Push"
        message = "Everything looks aligned. If you want, this is a strong moment to push forward."

    return {
            "burnout" : burnout,
            "stability" : stability,
            "mode" : mode,
            "message" : message
    }

def extract_life_states(sessions): 
    recent_sessions = sessions[-5:]
    states =[]
    for s in recent_sessions:
        score = (s["energy"] + s["focus"]) / 2
        if score < 4 :
          state = "LOW"
        elif score < 7:
          state = "MEDIUM"
        else:
           state = "HIGH"
        states.append(state)
    return states

def classify_life_phase(life_states):
    if len(life_states) < 3:
        return "FORMING"
    
    recent = life_states[-5:] #last 5 states
    low = recent.count("LOW")
    medium = recent.count("MEDIUM")
    high = recent.count("HIGH")

    # Pattern detection
    if low >= 3 and high == 0:
        return "STUCK"

    if recent[0] == "LOW" and recent[-1] == "HIGH":
        return "RECOVERING"

    if high >=3 and recent[-1] == "HIGH":
        return "BUILDING"

    if recent[0] == "HIGH" and recent[-1] == "LOW":
        return "DECLINING"
    
    return "UNSTABLE"



