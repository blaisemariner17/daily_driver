#!/usr/bin/env python3
import subprocess
from datetime import datetime
import os
import random


script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Constants
DAYS_TO_RUN = [0, 1, 2, 3, 4, 5, 6]  # Monday to Friday (0 = Monday, 1 = Tuesday, ..., 4 = Friday)
CHANCE_OF_SAT_SUN = 1  # 20% chance to run on Saturday or Sunday
MIN_RUN_DAYS = 1
MAX_RUN_DAYS = 4

def read_number():
    with open('number.txt', 'r') as f:
        return int(f.read().strip())

def write_number(num):
    with open('number.txt', 'w') as f:
        f.write(str(num))

def git_commit():
    # Stage the changes
    subprocess.run(['git', 'add', 'number.txt'])
    
    # Create commit with current date
    date = datetime.now().strftime('%Y-%m-%d')
    commit_message = f"Update number: {date}"
    subprocess.run(['git', 'commit', '-m', commit_message])

def git_push():
    # Push changes to GitHub
    subprocess.run(['git', 'push'])

def should_run_today():
    today = datetime.now().weekday()  # 0 = Monday, ..., 6 = Sunday
    run_on_day = today in DAYS_TO_RUN
    # Add a slight chance to include Saturday or Sunday
    if True: #random.random() < CHANCE_OF_SAT_SUN:
        run_on_day = True
    return run_on_day

def main():
    # Determine how many days this week the task will run
    total_days_to_run = random.randint(MIN_RUN_DAYS, MAX_RUN_DAYS)
    run_days = random.sample(DAYS_TO_RUN + [5, 6], total_days_to_run)  # Include Sat (5) and Sun (6) with a slight chance

    if True: #datetime.now().weekday() in run_days and should_run_today():
        try:
            current_number = read_number()
            new_number = current_number + 1
            write_number(new_number)
            git_commit()
            git_push()
            print(f"Task ran successfully today, updated number to {new_number}.")
        except Exception as e:
            print(f"Error: {str(e)}")
            exit(1)
    else:
        print("No task today. Waiting for the next scheduled run.")

if __name__ == "__main__":
    main()
