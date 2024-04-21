import os

def read_standings(filename):
    """Reads standings from a file, returning a dictionary of drivers to their positions."""
    with open(filename, 'r') as file:
        standings = {line.strip(): idx + 1 for idx, line in enumerate(file.readlines())}
    return standings

def calculate_scores(predictions, actuals, values):
    """Calculates scores based on the difference between predicted and actual positions."""
    scores = {}
    for driver, predicted_pos in predictions.items():
        actual_pos = actuals.get(driver)
        if actual_pos:
            position_diff = abs(predicted_pos - actual_pos)
            score = values.get(position_diff, 0)  # 0 points for diffs > 10
            scores[driver] = score
        else:
            scores[driver] = 0  # Driver not found in actual standings
    return scores

def main(track, event_type):
    values = {
        0: 25, 1: 18, 2: 15, 3: 12, 4: 10, 5: 8,
        6: 6, 7: 4, 8: 2, 9: 1, 10: 0
    }
    
    # File paths
    actuals_path = f'standings/{track}/{event_type}/{event_type}-standings.txt'
    prediction_jack_path = f'predictions/{track}/predictions-jack.txt'
    prediction_cristian_path = f'predictions/{track}/predictions-cristian.txt'
    
    # Check if files exist
    if not os.path.exists(actuals_path) or not os.path.exists(prediction_jack_path) or not os.path.exists(prediction_cristian_path):
        print("One or more required files are missing.")
        return
    
    # Read standings and predictions
    actuals = read_standings(actuals_path)
    predictions_jack = read_standings(prediction_jack_path)
    predictions_cristian = read_standings(prediction_cristian_path)
    
    # Calculate scores
    score_jack = calculate_scores(predictions_jack, actuals, values)
    score_cristian = calculate_scores(predictions_cristian, actuals, values)
    
    # Sum up total scores and compare
    total_score_jack = sum(score_jack.values())
    total_score_cristian = sum(score_cristian.values())
    print(f"Jack's total points: {total_score_jack}")
    print(f"Cristian's total points: {total_score_cristian}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Calculate F1 prediction scores.')
    parser.add_argument('track', type=str, help='Track location (e.g., china)')
    parser.add_argument('event_type', choices=['race', 'sprint'], help='Type of event: race or sprint')
    args = parser.parse_args()
    
    main(args.track, args.event_type)
