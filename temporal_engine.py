from datetime import datetime

class TemporalEngine:
    def __init__(self):
        pass

    def perceive(self, sessions):
        now = datetime.now()
        hour = now.hour

        if 5 <= hour < 12:
            day_part = "MORNING"
        elif 12 <= hour < 17:
            day_part = "AFTERNOON"
        elif 17 <= hour <21:
            day_part = "EVENING"
        elif 21 <= hour < 24:
            day_part = "NIGHT"
        else:
            day_part = "LATE_NIGHT"

        perception = {
            "day_part": day_part
        }

        return perception
    

    def detect_anomaly(self, sessions):
        if len(sessions) <3:
            return None
        
        recent = sessions[-3:]
        times = []

        for s in recent:
            ts = s.get("timestamp")
            if not ts:
                continue
            hour = int(ts.split(":")[0])
            times.apped(hour)

        if len(times) < 3:
            return None
        
        avg_hour = sum(times) / len(times)
        now_hour = datetime.now().hour

        if abs(now_hour - avg_hour) >=3:
            return "UNUSUAL_TIME"
        
        return "NORMAL_TIME"
    

    def describe_time(self):
        hour = datetime.now().hour

        if 5 <= hour < 9:
            return "EARLY_MORNING"
        if 9 <= hour < 12:
            return "MORNING"
        if 12 <= hour < 16:
            return "AFTERNOON"
        if 16 <= hour < 19:
            return "EVENING"
        if 19 <= hour < 23:
            return "NIGHT"
        return "LATE_NIGHT"
    