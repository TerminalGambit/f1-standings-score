import subprocess

class ScoreCalculator:
    def __init__(self, races, formats, output_path):
        self.races = races
        self.formats = formats
        self.output_path = output_path

    def calculate_scores(self):
        with open(self.output_path, 'w') as file:
            for race in self.races:
                for formated in self.formats:
                    command = f"python3 score.py {race} {formated}"
                    result = subprocess.run(command, shell=True, capture_output=True, text=True)
                    output = result.stdout.strip()
                    file.write(output + '\n')

    def get_totals(self):
        jack_total = 0
        cristian_total = 0

        with open(self.output_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("Jack's total points:"):
                    jack_points = int(line.split(":")[1].strip())
                    jack_total += jack_points
                elif line.startswith("Cristian's total points:"):
                    cristian_points = int(line.split(":")[1].strip())
                    cristian_total += cristian_points

        return jack_total, cristian_total

def championship_total():
    races = ['china', 'miami', 'imola', 'monaco']
    formats = ['sprint', 'race']
    output_path = '/Users/jackmassey/Desktop/Bureau/f1-standings-score/statistics/log/championship.txt'

    calculator = ScoreCalculator(races, formats, output_path)
    calculator.calculate_scores()

    jack_total, cristian_total = calculator.get_totals()

    print("Jack's total points:", jack_total)
    print("Cristian's total points:", cristian_total)

if __name__ == '__main__':
    championship_total()
