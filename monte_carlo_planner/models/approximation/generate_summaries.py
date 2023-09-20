def mean(data):
    return sum(data) / len(data)

def mode(data):
    from collections import Counter
    count = Counter(data)
    max_count = max(count.values())
    modes = [x for x, count in count.items() if count == max_count]
    
    if len(modes) == 1:
        return modes[0]
    else:
        return "No unique mode"

def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

def describe_distribution(data):
    data_mean = mean(data)
    data_mode = mode(data)
    data_median = median(data)
    data_max = max(data)
    data_min = min(data)
    data_range = data_max - data_min
    
    return f"(Mean: {data_mean}, Mode: {data_mode}, Median: {data_median}, Max: {data_max}, Min: {data_min}, Range: {data_range})"

# Example usage
data = [1, 2, 3, 4, 5, 5, 6]
result = describe_distribution(data)
print(result)
