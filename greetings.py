class GreetingEngine:
    def generate(self, time_state, user_name=None):
        name = f", {user_name}" if user_name else ""

        if time_state == "LATE_NIGHT":
            return f"You're here{name}. Nights have a way of slowing the world. We can take this moment quietly."

        if time_state == "MORNING":
            return f"Good morning{name}. A new stretch of time is in front of you — no rush, just direction."

        if time_state == "AFTERNOON":
            return f"Hey{name}. The afternoon carries its own momentum. Let's shape it with care."

        if time_state == "EVENING":
            return f"Evening{name}. The day is settling. This is a good time to reflect and choose your next step."

        if time_state == "NIGHT":
            return f"You're here{name}. The world is quieter now. We can move gently from here."

        return f"I'm here{name}. Let's begin."
