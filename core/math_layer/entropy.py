# ARES-X File 09: Encryption Strength Calculator
import math

def calculate_entropy(data):
    """
    Industrial Math: Calculates the randomness of data.
    0-3: Weak (Easy to hack)
    4-6: Medium (Takes time)
    7-8: High (Military Grade)
    """
    if not data:
        return 0
    
    entropy = 0
    for x in range(256):
        p_x = float(data.count(chr(x))) / len(data)
        if p_x > 0:
            entropy += - p_x * math.log(p_x, 2)
            
    return round(entropy, 2)

def success_probability(entropy_score):
    """Predicts the probability of a successful breach based on math."""
    # If entropy is 8, probability is near 0. If entropy is 2, probability is 90%.
    prob = (1 - (entropy_score / 8)) * 100
    return max(0, round(prob, 2))
