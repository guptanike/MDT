def calculate_impact(decision_id):
    """
    Calculates micro-level impacts of a decision.
    Butterfly Effect: small action → multi-dimensional impact
    """

    impact_map = {
        "D1": {"health": -3, "focus": -4, "career": -2},
        "D2": {"health": -1, "focus": -3, "career": -4},
        "D3": {"health": -2, "focus": -4, "career": -3},
        "D4": {"health": -4, "focus": -2, "career": -1},
        "D5": {"health": -3, "focus": -2, "career": -2},

        "G1": {"health": 3, "focus": 2, "career": 1},
        "G2": {"health": 1, "focus": 3, "career": 3},
        "G3": {"health": 2, "focus": 3, "career": 2},
        "G4": {"health": 4, "focus": 2, "career": 1},
        "G5": {"health": 2, "focus": 2, "career": 3}
    }

    return impact_map.get(decision_id, {
        "health": 0,
        "focus": 0,
        "career": 0
    })
