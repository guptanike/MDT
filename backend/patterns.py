DECISION_TYPE = {
    "D1": "bad", "D2": "bad", "D3": "bad", "D4": "bad", "D5": "bad",
    "G1": "good", "G2": "good", "G3": "good", "G4": "good", "G5": "good"
}

def detect_pattern(impact):
    negative_count = sum(1 for v in impact.values() if v < 0)
    positive_count = sum(1 for v in impact.values() if v > 0)

    if negative_count >= 2:
        return "Negative Habit Loop (Compounding Loss)"
    elif positive_count >= 2:
        return "Positive Growth Loop (Compounding Gain)"
    else:
        return "Neutral / Mixed Behavior Pattern"
