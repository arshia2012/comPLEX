import perplexity
import burstiness

def extract(text):
    plex = perplexity.calculate_perplexity(text)
    burst = burstiness.calculate_brustiness(text)
    return [plex, burst]