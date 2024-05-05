import subprocess

races = ['china', 'miami']
formats = ['sprint', 'race']

with open('/Users/jackmassey/Desktop/Bureau/f1-standings-score/championship.txt', 'w') as file:
    for race in races:
        for format in formats:
            command = f'python3 score.py {race} {format}'
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            output = result.stdout.strip()
            file.write(output + '\n')

jack_total = 0
cristian_total = 0

with open('/Users/jackmassey/Desktop/Bureau/f1-standings-score/championship.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line.startswith("Jack's total points:"):
            jack_points = int(line.split(":")[1].strip())
            jack_total += jack_points
        elif line.startswith("Cristian's total points:"):
            cristian_points = int(line.split(":")[1].strip())
            cristian_total += cristian_points

print("Jack's total points:", jack_total)
print("Cristian's total points:", cristian_total)
