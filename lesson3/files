from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent.parent

results = []

with open(ROOT_DIR / "rockyou.txt", encoding='utf-8') as file:
    for line in file:
        if 'user' in line:
            print("Line:", line)
            user_input = input("Do you want to add this line to results? (yes/no(for no press any key)): ")
            if user_input.lower() == 'yes':
                results.append(line.strip())

file.close()

print("Results:", results)
print("Number of added lines:", len(results))