import math
import math

def calculate_horizon_distance(height_meters):
    """
    Calculates the distance to the horizon in kilometers.
    
    Args:
        height_meters: The height of the observer in meters.
        
    Returns:
        The distance to the horizon in kilometers.
    """
    distance_km = 3.57 * math.sqrt(height_meters)
    return distance_km

# Example usage:
# height = float(input("Enter the observer's height in meters: "))
# horizon_distance = calculate_horizon_distance(height)
# print(f"The distance to the horizon is {horizon_distance:.2f} km.")
height = float(input("Enter the observer's height in meters: "))
horizon_distance = calculate_horizon_distance(height)
print(f"The distance to the horizon is {horizon_distance:.2f} km.")
