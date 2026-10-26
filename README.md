# ISM3232 Midterm: [Copper Kettle Coffee Roasters]

- **Name:** [Elijah Willie]
- **Version:** [Version ZETA]
- **Date:** [October 25th, 2026]

## What This Program Does
- This program establishes the shipping report for Copper Kettle Coffee Roasters. It lays out the shops and hotels that Copper Kettle ships to, along with the amount that each shop/hotel paid for their shipment, whether each shop/hotel had prepaid or not, whether each shipment requires a pallet or not, the total amount of both the shipments and the cash total that all of the shipments amounted to. The program also shows the average amount paid for a shipment and the largest shipment out of all of the shops/hotels. 

## Business Rules
- The first rule establishes the cost of the beans, which can be calculated by multiplying the price per bag by the number of bags
- The discount given is dependent on the number of bags being bought:
   - If you order less than 20 bags, you receive no discount.
   - If you order anywhere between 20 to 79 bags, you receive a 9% discount.
   - If you order 80 bags or more, you receive a 14% discount.
- If you're a partner of Coffee Kettle Coffee Roasters, you can receive an additional 4% discount on top of the discount that you're receiving already, but only if the order is 20 bags or more.
- If the discounted cost of an order is less than $250, a $35 shipping fee will be added to your order cost.
- If your shipment costs $1500 or more, you are required to make a prepayment on your order.
- If  your shipment amounts to 60 bags or more, and totals to $700 or more, the shippment requires a freight pallet.

## How to Run
- Commands for Creating the environment and Installing the Requirements
    ```
    - mkdir ism3232-midterm
    - cd ism3232-midterm
    - pwd
    - git init
    -  touch business_rules.py
    - touch main.py
    - touch commands.md
    - touch README.md
    - touch requirements.txt
    - touch .gitignore
    - tree -L2
    - mkdir -p tests && touch tests/__init__.py tests/test_business_rules.py
    - python3 -m venv .venv && source .venv/bin/activate
    - pip install pytest ruff && pip freeze > requirements.txt 
    - echo '.venv/' > .gitignore && echo '__pycache__/' >> .gitignore
    ```
- Command to run the test
    ```
    - python3 main.py
    ```
## How to Test
```
ruff format .
ruff check .
pytest -v
```
- There were 30 tests wrote for this program. 

## Files in This Repository
- main.py: imports and calls the functions for this program
- business_rules.py: holds only the functions for this program
- __init__.py: makes the tests/ a package
- .gitignore: Holds the files/folders that we want github to ignore
- README.md: Gives a description of the program, how it functions, and how to use the program
- tests/test_business_rules.py: Imports, holds and tests the functions
- Commands.md: Holds the commands used to set up this program, discusses the functions/tests used in this program, as well as the commands used to help service this program
- requirements.txt: Lists all of the libraries and packages that the program needs to run 
## AI Use Statement
- I did not use AI to complete this exam. 
