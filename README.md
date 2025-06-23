# todoList.py

A command-line To-Do List in Python, enabling users to manage tasks with options to add, delete, display, and mark tasks as complete. 
This program provides a efficient way to organize and track tasks, making it easier to stay productive and focused.
Todo-List allows users to manage their tasks by adding, deleting, displaying and marking tasks as complete.
1. The program runs in an infinite loop, presenting the user with options to:
- Add a task
- Delete a task
- Display tasks
- Mark a task as complete
- Exit the program
2. Based on the user's input, the corresponding action is performed:
- Add task : Prompts the user to enter a task name, adds it to the list with an "incomplete" state, and displays a confirmation message.
- Delete task : Prompts the user to enter a task name, removes it from the list if found, and displays a confirmation message or an error message if not found.
- Display tasks : Lists all tasks with their current state (incomplete or complete) or displays a message if there are no tasks.
- Mark as complete : Prompts the user to enter a task name, updates its state to "complete" if found, and displays a confirmation message or an error message if not found.
- Exit : Displays a farewell message and breaks the loop, ending the program.

# passwordManager.py

A Password Manager helps to store and retrieve the details securely. 
It was built using the python programming language.
It can store various username and passwords for the websites and apps.
It uses encryption and decryption to provide security.
The security can be increased by using encryption libraries (e.g., cryptography...)

The steps of password manager is as follows:

Step-1 : Authentication

The user needs to enter a main password (“pwd135”) for authentication.
If the entered password matches then authentication successful.
Now user can store and retrieve the passwords.

Step-2 : Options

There will be three options after the authentication.
1. Store password : 
The passwords are stored in a dictionary with the page name as the key and the username and password as values.
2. Retrieve password :
The user can retrieve passwords for a particular page by entering the page name.
3. Exit :
When exiting the encrypted and decrypted passwords are shown.
The password manager provides passwords to encrypt and decrypt using a simple Caesar cipher. 
The Caesar cipher shift the 3 characters in the process and provides security for the passwords.

# numberGuess.py

This Python-based Number Guessing Game, is a command-line interactive application where users try to guess a randomly generated number between 1 and 100.
We can also specify the range of numbers that makes the game more interesting. 
The game offers two difficulty levels - Easy and Hard, which determine the number of allowed attempts. 
The player must guess the correct number within a limited number of attempts. 
Attempts decide how many chances the player gets to guess the number. 
The game also encourages critical thinking and improves decision-making within a set of constraints (limited attempts).
It demonstrates fundamental programming concepts such as conditions, loops, functions, and user input handling. 
The structure allows for future enhancements like session tracking and performance analytics using data analysis libraries such as pandas.

The game's logic is structured into modular components as described below:

Step-1 : User Interface

Displays welcome message and prompts for game mode and guesses.

Step-2 : Random Number Generator 

Uses the random module to select a number between 1 and 100.

Step-3 : Mode Selector 

Two modes - Easy-10 attempts, Hard-5 attempts

Step-4 : Game Loop 

Runs until the player guesses the number or runs out of attempts. Provides feedback for each guess (too high, too low).

Step-5 : Result Display 
Congratulates the player or displays the correct number after the game ends.
