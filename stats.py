import statistics


def calculate_statistics(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    try:
        mode = statistics.mode(numbers)
    except statistics.StatisticsError:
        mode = "No unique mode"
    minimum = min(numbers)
    maximum = max(numbers)
    range_value = maximum - minimum
    stdev = statistics.stdev(numbers)
    variance = statistics.variance(numbers)
    
    return {
        "Mean": mean,
        "Median": median,
        "Mode": mode,
        "Minimum": minimum,
        "Maximum": maximum,
        "Range": range_value,
        "Standard Deviation": stdev,
        "Variance": variance
    }


