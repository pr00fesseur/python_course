from pathlib import Path

ROOT_DIR: Path = Path(__file__).absolute().parent.parent

# file = open(ROOT_DIR / "rockyou.txt")
# lines: list[str] = file.readlines()
# file.close()
results: list[str] = []


def get_file_lines(filename: Path):
    file = open(filename)
    while True:
        line = file.readline()
        if not line:
            break

        yield line


for line in get_file_lines(ROOT_DIR / "rockyou.txt"):
    user_input = input(f"Do you wanna add the line: {line}")
    if "user" not in line:
        continue
    if user_input == "yes":
        results.append(line)
        print(f"Line: {line} is added")
    else:
        continue
