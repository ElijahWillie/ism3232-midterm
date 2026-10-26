## 1. Building the Project

# pwd
# mkdir ism3232-midterm
# cd ism3232-midterm
# pwd
# git init
# touch business_rules.py
# touch main.py
# touch commands.md
# touch README.md
# touch requirements.txt
# touch .gitignore
# tree -L2
# mkdir -p tests && touch tests/__init__.py tests/test_business_rules.py
# python3 -m venv .venv && source .venv/bin/activate
# pip install pytest ruff && pip freeze > requirements.txt 
# echo '.venv/' > .gitignore && echo '__pycache__/' >> .gitignore
# python3 -m pytest --version
# ruff --version
# git status
# git remote -v
# git remote add origin https://github.com/ElijahWillie/ism3232-midterm.git
# git branch -M main

## 2. The Virtual Environment

# After entering the command 'which python3' while the virtual environment was active, it returned '/home/lilwillie/ism3232/ism3232-midterm/.venv/bin/python3'

## 3. The project structure

# After performing the 'tree -L 2' command in the terminal, one of the files that are on my computer, but not in the repository for this midterm is the __pycache__ file. This is because it was echoed into the .gitignore file so that github wouldn't track it.

## 4. Every function and test

## There are 8 functions defined by business_rules.py and 30 functions defined by tests/test_business_rules.py.

## 5. Which files print

# The only python file that prints is the main.py file. The business_rules.py file wasn't included on the list because that file is only meant to hold functions for other files to pull from. This prevents breaking definitions and formulas by changing an external dependency. It also allows you to easily see the problems that the software solves an business_rules.py and what the startup sequence looks like in main.py

## 6. The commit history




 