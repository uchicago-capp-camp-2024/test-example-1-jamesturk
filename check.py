import sys
import subprocess
import pathlib

HIDDEN_FILE = ".part2-done"


def check_git_output(command, contains):
    output = subprocess.run(["git", command], capture_output=True).stdout.decode()
    if contains in output.lower():
        return True
    else:
        return False


def check_status_clean():
    if not check_git_output("status", "nothing to commit, working tree clean"):
        print(
            "Ensure that you have committed or  any changes before running, run `git status` to check."
        )
        return False
    return True


def check_part1():
    # ensure that the repo has a commit with 'part 1 done'
    check_status_clean()
    if not check_git_output("log", "part 1 done"):
        print(
            "Part 1: Ensure that you have made a commit with the message 'part 1 done', run `git log` to check."
        )
    else:
        print("Part 1: Complete!")


def check_part2():
    # once file exists, check that change was reverted
    if pathlib.Path(HIDDEN_FILE).exists():
        if check_status_clean():
            print("Part 2: Complete!")
    else:
        # file doesn't exist yet, ask for change
        part2_text = pathlib.Path("part2.txt").read_text()
        if ":)" not in part2_text:
            print(
                "Be sure to add the happy face in part2.txt before running this command."
            )
        else:
            print(
                "OK, I've observed your change. Go ahead and undo it now using `git restore`"
            )
            with open(HIDDEN_FILE, "w") as f:
                f.write(":)")


def check_part4():
    part4_text = pathlib.Path("part4.txt").read_text()
    if "snowfall" not in part4_text:
        print("Be sure to add the secret word to part4.txt.")
    else:
        print("Great job, all done!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Be sure to pass the part you are checking, e.g. `python3 check.py` 1 for part 1"
        )
    if sys.argv[1] == "1":
        check_part1()
    elif sys.argv[1] == "2":
        check_part2()
    elif sys.argv[1] == "3":
        print("There is no automated checking for part 3.")
    elif sys.argv[1] == "4":
        check_part4()
