# Student_Manager
This program is a menu-driven application written in Python. It allows users to manage student records by storing names and marks, checking student details, and evaluating results. A dictionary (student = {}) is used to store student data, where the student’s name is the key and their marks are the value.

🔹 Features:
Add Student

The user enters the student’s name and marks.

This data is stored in the dictionary.

A confirmation message is displayed: “Successfully Added”.

Check Student

If the dictionary is empty, the program shows: “Student not found”.

Otherwise, it lists all students with their marks.

Check Result

The user enters a student’s name.

If the student exists, their marks are checked.

Marks greater than 33 → “PASS :)”

Marks 33 or below → “FAIL!”

If the student does not exist, the program shows: “Student not found”.

Exit

Ends the program with the message: “Exiting…”.

🔹 Flow:
The program runs continuously (while True) until the user chooses the Exit option.

Each loop displays the menu and waits for the user’s choice.

Invalid inputs are handled with the message: “Invalid Input”.
