def study_schedule(permanence_period, target_time):
    result = 0
    if (target_time is None):
        return None
    for start, end in permanence_period:
        if (not type(start) == int or not type(end) == int):
            return None
        if (target_time >= start and target_time <= end):
            result += 1
    return result
