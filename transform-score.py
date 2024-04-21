def read_standings(filename):
    with open(filename, 'r') as file:
        standings = {line.strip(): idx + 1 for idx, line in enumerate(file.readlines())}
    return standings

def calculate_scores(predictions, actuals, values):
    scores = {}
    for driver, predicted_pos in predictions.items():
        actual_pos = actuals.get(driver)
        if actual_pos:
            position_diff = abs(predicted_pos - actual_pos)
            score = values.get(position_diff, 0)  # Assuming 0 points for position diffs > 10
            scores[driver] = score
        else:
            scores[driver] = 0  # Driver not found in actual standings, might assign penalties or 0
    return scores

def main():
    # Scoring values based on position differences
    values = {
        0: 25, 1: 18, 2: 15, 3: 12, 4: 10, 5: 8,
        6: 6, 7: 4, 8: 2, 9: 1, 10: 0  # Assuming you assign 0 points for diff > 10
    }
    
    # Read and parse standings from files
    predictions_jack = read_standings('china.txt')
    predictions_cristian = read_standings('chine.txt')
    actuals = read_standings('sprint-standings.txt')
    
    # Calculate scores based on prediction accuracy
    score_jack = calculate_scores(predictions_jack, actuals, values)
    score_cristian = calculate_scores(predictions_cristian, actuals, values)
    
    # Output results
    total_score_jack = sum(score_jack.values())
    total_score_cristian = sum(score_cristian.values())
    if total_score_jack > total_score_cristian:
        print(f"Jack wins with {total_score_jack} points! Cristian has {total_score_cristian} points.")
    elif total_score_jack < total_score_cristian:
        print(f"Cristian wins with {total_score_cristian} points! Jack has {total_score_jack} points.")

if __name__ == "__main__":
    main()
