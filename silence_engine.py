import random

class SilenceEngine:
    def __init__(self):
        # remember last few silence styles to avoid patterns.
        self.history = []

        # available silence styles
        self.styles = ["A", "B", "C"]

    def choose(self):
        # Choose a silence style in a non-repetitive, non-patterned way.

        # if history is short, allow full randomness
        if len(self.history) < 2:
            choice = random.choice(self.styles)
        else:
            # Avoid repeting the last style too often
            last = self.history[-1]
            second_last = self.history[-2]

            options = self.styles.copy()

            # Strongly discourage repeating same style twice
            if last in options:
                options.remove(last)

            # Slightly discourage repeating the same pattern
            if len(options) > 1 and second_last in options:
                options.remove(second_last)

            if not options:
                options = self.styles.copy()

            choice = random.choice(options)

        self.history.append(choice)

        # Keep history small
        if len(self.history) > 6:
            self.history.pop(0)

        return choice
    

    def message(self, style):

        # Return the actual response for each silence style.

        if style == "A":
            return "" # Stillness - no extra words
        
        if style == "B":
            return "Let's slow this moment down."
        
        if style == "C":
            return "I'm here with you."
        
        return ""
    