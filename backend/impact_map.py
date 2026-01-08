def calculate_total_impact(impact):
    total_score = 0
    for value in impact.values():
        total_score += value
    return total_score


def calculate_butterfly_intensity(impact, frequency, time_period):
    base_impact = sum(impact.values())
    intensity = base_impact * frequency * time_period
    return intensity
