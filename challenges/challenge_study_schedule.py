def study_schedule(permanence_period, target_time):
    try:
        result = 0
        if (target_time is None):
            raise TypeError
        for period in permanence_period:
            if (target_time in range(period[0], period[1] + 1)):
                result += 1
        return result
    except TypeError:
        return None
