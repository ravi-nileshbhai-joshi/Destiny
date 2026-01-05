def classify_moment(session, recent_session): 
    energy = session["energy"]
    focus = session["focus"]
    derived = session.get("derived_state", {})

    core = "LIVELY"
    modifiers = []

    # Core state detection 
    if focus >= 7:
        core = "MEANINGFUL"
    elif energy >= 7:
        core = "LIVELY"
    else:
        core = "LIVELY"

    # Modifier detection
    if energy > focus and focus < 6 :
        modifiers.append("RECOVERING")
    
    if energy >= 7 and focus >= 7:
        modifiers.append("BUILDING")

    if energy < 5 and focus <5:
        modifiers.append("RESTING")

    if len(recent_session) >=2:
        last = recent_session[-2]
        last_avg = (last["energy"] + last["focus"]) / 2
        current_avg = (energy + focus) / 2

        if abs(current_avg - last_avg) > 1:
            modifiers.append("SHIFTING")

    # Confidence estimation
    confidence = round(min(1.0, (energy + focus) / 20), 2)
    
    return {
        "core": core,
        "modifiers": modifiers,
        "confidence": confidence
    } 
