# TeReoCounter

A simple Maori language learning quiz application written in Python.

## Features
- Two quiz modes:
  - **Input Mode**: Type the Maori translation for a given English word.
  - **Multi-Choice Mode**: Select the correct Maori translation from multiple choices.
- Randomized questions to keep the quiz fresh.
- User-friendly error handling and feedback.
- Graceful exit options and input validation.

## Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

### Quick Start
1. Clone or download this repository
2. Navigate to the project directory
3. Run the program using one of the methods below

## How to Run

### Method 1: Direct Python Command
```bash
python "Inputmode - Maori check complete.py"
```

### Method 2: Windows Users (Double-click)
- Double-click `run_tereocounter.bat` to start the program
- The program will run in a command prompt window

### Method 3: Unix/Linux/Mac Users
```bash
# Make the script executable (first time only)
chmod +x run_tereocounter.sh

# Run the program
./run_tereocounter.sh
```

### Method 4: Python Module
```bash
python -m "Inputmode - Maori check complete"
```

## File Descriptions
- **`Inputmode - Maori check complete.py`**: Main Python script for the quiz application
- **`Maori2Eng.txt`**: Comma-separated list of Maori and English word pairs
- **`run_tereocounter.bat`**: Windows batch file launcher
- **`run_tereocounter.sh`**: Unix/Linux/Mac shell script launcher
- **`requirements.txt`**: Python dependencies (standard library only)
- **`.gitignore`**: Git ignore rules for Python projects

## Example Usage
```
==================================================
           TEREOCUNTER QUIZ
==================================================
Welcome to the Maori language learning quiz!
Choose your quiz mode:
1. Input Mode - Type the Maori translation
2. Multi-Choice Mode - Select from options
3. Exit
==================================================
Please select your mode (1, 2, or 3): 1

==================================================
           INPUT MODE QUIZ
==================================================
You will be given 10 English words.
Type the Maori translation for each word.
Type 'exit' at any time to quit the quiz.

       Your english word is  HELLO
       Please provide Maori translation: kia ora

          Congratulations, You are correct!
              KIA ORA is the right answer!
```

## Controls
- **Exit**: Type 'exit', 'quit', or 'q' at any prompt
- **Menu Navigation**: Use numbers 1, 2, or 3
- **Multi-choice**: Select options 1, 2, 3, or 4
- **Interrupt**: Press Ctrl+C to exit immediately

## Credits
- Developed by harry0537

---
Feel free to contribute or suggest improvements! 