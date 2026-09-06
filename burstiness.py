import statistics
import re

def calculate_brustiness(text):
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    if len(sentences) < 2:
        return 0
    
    lengths = [len(s.strip()) for s in sentences]
    mean_length = statistics.mean(lengths)
    std_dev = statistics.stdev(lengths)

    burstiness = std_dev / mean_length if mean_length > 0 else 0
    return burstiness