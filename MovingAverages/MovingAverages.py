def running_averages(samples):
    if not samples:
        return []
    
    result = []
    current_sum = 0
    
    for i, x in enumerate(samples, 1):
        current_sum += x
        result.append(current_sum / i)
        
    return result