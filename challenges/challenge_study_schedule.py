def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    max_count = 0
    count = 0

    for period in permanence_period:
        if not isinstance(period[0], int) or not isinstance(period[1], int):
            return None
        if period[0] <= target_time <= period[1]:
            count += 1
        if count > max_count:
            max_count = count

    return max_count
