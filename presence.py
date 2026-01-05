class PresenceEngine:
    def __init__(self):
        self.last_presence = None

    def decides(self, tempo, life_phase, stability, burnout):
        # Quiet always wins
        if tempo == "QUIET":
            return "WAITING"

        # High burnout → hold space, not advice
        if burnout.lower() == "high":
            return "HOLDING_SPACE"

        # Stuck or declining → walk alongside
        if life_phase in ["STUCK", "DECLINING", "UNSTABLE"]:
            return "WALKING_WITH"

        # Building → arrive with grounded direction
        if life_phase == "BUILDING":
            return "ARRIVING"

        # Default human posture
        return "WALKING_WITH"

    def presence_message(self, presence_state, user_name=None):
        if presence_state == "WAITING":
            return "I'm here whenever you feel ready."

        if presence_state == "HOLDING_SPACE":
            return "Let's slow this moment down. You don't have to carry it alone."

        if presence_state == "ARRIVING":
            return "It feels like the right moment to move forward."

        if presence_state == "WALKING_WITH":
            return "Let's walk through this together."

        return ""

  