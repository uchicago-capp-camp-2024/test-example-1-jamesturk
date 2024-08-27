# CAPP Camp Git Lab

Like yesterday's lab, today's lab will ask you to take some steps with git and run a `check.py` script as you go.

Additionally, today you'll be submitting at the end via Gradescope-- a tool used in many classes.

Don't worry, we won't be grading your work, submitting is merely to help you get acquainted with tools you'll be using in many classes.

## Part 1 - Making a First Commit

Whenever you have made a change that you wish to keep, you'll make a git commit.

Open up 'part1.txt' using `code` and answer the questions.

When you've done so, add a commit with the message "part 1 done!"

Run `python3 check.py 1` to check that your commit exists and is correct.

## Part 2 - Making & Reverting Changes with `git restore`

Open up the file 'part2.txt' and make the modifications it describes. (Do not commit them yet!)

Run the command `python3 check.py 2` which will verify that these changes are made.

Once you've run this command, undo the changes using git restore and run `python3 check.py 2` again.

## Part 3 - Viewing Changes with `git diff`

Run the command `python3 changes.py` this will make some changes to your local files, but will not commit them. (Do not commit them either!)

Then take a look at these changes with `git diff`, open up part3.txt and answer the questions based on the changes you see.

Be sure to commit your changes! There is no `check.py` step for this part.

## Part 4 - Finding a Change in the `git log`

The answer to part 4 is in the git history. Use `git log` to find the commit in question.

You'll see that each commit has a hash, like 'de8e74bc2c3ec106554440021efd1ec6808486c2'.
These uniquely identify each commit.

Once you find it, you can use `git show <hash-id>` to show what changed in that commit.

**Tip:** If you are typing hashes instead of copying & pasting, you can type the first 4-5 characters instead of the entire thing.

Use `git log` and `git show` to discover what used to be in the 'secret' file and add this text to part4.txt. You may use `python3 check.py 4` to confirm.

You can also try this using the GitHub interface which offers an alternative interface to view the log:

![](readme-screenshot.png)

### A Note About Secrets

Consider what part 4 means for actual secrets, such as a password or other sensitive information.

It is difficult to _actually remove_ sensitive information from a published Git repository.

For this reason, be sure to avoid committing passwords or other information that you wouldn't want someone to see.
