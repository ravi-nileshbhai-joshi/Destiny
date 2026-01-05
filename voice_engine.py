class VoiceEngine:
    def __init__(self):
        pass

    def speak(self, message, mode, tempo, life_phase):
        # Tone shaping happens here
        if mode == "QUIET_MODE":
            return self.quiet_voice()

        if tempo == "EXPRESSIVE":
            return self.steady_voice(message)

        if tempo == "ENGAGED":
            return self.present_voice(message)

        if tempo == "CALM":
            return self.minimal_voice(message)

        return message

    def quiet_voice(self):
        return "Take your time. I’m here when you’re ready."

    def steady_voice(self, message):
        return message

    def present_voice(self, message):
        return message

    def minimal_voice(self, message):
        return message
