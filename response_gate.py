from silence_engine import SilenceEngine

silence_engine = SilenceEngine()

def decide_gate(tempo, life_phase, stability, burnout_risk):
    # 🕊️ Rule 1 — Quiet is sacred
    if tempo == "QUIET":
        style = silence_engine.choose()
        return {
            "mode": "QUIET_MODE",
            "silence_style": style
        }

    # 🪵 Rule 2 — Fragile states
    if life_phase in ["STUCK", "DECLINING"] and tempo in ["CALM", "QUIET"]:
        return {"mode": "LISTEN_MODE"}

    # 🧭 Rule 3 — When clarity is possible
    if life_phase in ["RECOVERING", "BUILDING"] and tempo in ["ENGAGED", "EXPRESSIVE"]:
        return {"mode": "GUIDE_MODE"}

    # 🔥 Rule 4 — Strong momentum
    if life_phase == "BUILDING" and stability == "STABLE" and tempo == "EXPRESSIVE":
        return {"mode": "FLOW_MODE"}

    # 🧯 Safety override — burnout protection
    if burnout_risk == "HIGH":
        return {"mode": "LISTEN_MODE"}

    # Default
    return {"mode": "LISTEN_MODE"}
