from datetime import datetime

class EmotionalTempo:
    def __init__(self):
        self.history = []
        self.last_active = None

    def observe(self, message: str):
        now = datetime.now()

        signal = {
            "length" : len(message),
            "time" : now
        }

        self.history.append(signal)
        self.last_active = now

    def get_tempo(self):
        if not self.history:
            return "NEUTRAL"
       
        # If the most recent message is empty or near-empty, enter QUIET immediately 
        last = self.history[-1]
        if last["length"] <= 1:
            return "QUIET"
                
        recent = self.history[-5:]

        avg_length = sum(s["length"] for s in recent) / len(recent)

        if avg_length > 80:
            return "EXPRESSIVE"
        elif avg_length > 30:
            return "ENGAGED"
        elif avg_length > 10:
            return "CALM"
        else:
            return "QUIET"
    
    
    def analyze(self, message: str):
        self.observe(message)
        return self.get_tempo()

