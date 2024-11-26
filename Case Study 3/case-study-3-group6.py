import math
 
def reward_function(params):

    # Constants
    CENTER_WEIGHT = 1
    BORDER_PENALTY = -2.0
    TIME_REWARD = 1.0
    SMOOTH_PENALTY = -0.2
    
    # Get relevant data
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    waypoints = params['waypoints']
    all_wheels_on_track = params['all_wheels_on_track']
    steps = params['steps']
 
    
    # Reward for following the center line
    center_reward = 1.0 - (distance_from_center / (track_width / 2))
    center_reward = max(0.0, center_reward)

    collision_penalty = 0
    # Penalty for going outside the borders
    border_penalty = 0.0
    if abs(distance_from_center) > (track_width / 2):
        border_penalty = BORDER_PENALTY
    # Reward for completing the track quickly
    time_reward = TIME_REWARD * (1.0 - (steps / 1000))  # Assuming 1000 steps maximum
    # Smooth driving penalty
    smooth_penalty = 0.0
    if len(waypoints) > 2:
        prev_point = waypoints[-2]
        current_point = waypoints[-1]
        prev_angle = math.atan2(current_point[1] - prev_point[1], current_point[0] - prev_point[0])
        if 'prev_angle' in params:
            prev_angle = params['prev_angle']
            diff_angle = abs(prev_angle - math.degrees(math.atan2(current_point[1] - prev_point[1], current_point[0] - prev_point[0])))
            if diff_angle > 6:  # Tolerance angle for penalizing zigzag
                smooth_penalty = SMOOTH_PENALTY
    # Combine rewards and penalties
    reward = (CENTER_WEIGHT * center_reward) + collision_penalty + border_penalty + time_reward + smooth_penalty
    return float(reward)