def study_schedule(permanence_period, target_time):
    if target_time is None or not all(
        isinstance(period[0], int) and isinstance(period[1], int)
            for period in permanence_period):
        return None

    max_count = 0
    count = 0

    for period in permanence_period:
        if period[0] <= target_time <= period[1]:
            count += 1
        if count > max_count:
            max_count = count

    return max_count
