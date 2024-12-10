# CODSOFT-2

## Project Title

**Password Generator**

## Description

The Password Generator is a graphical user interface (GUI) application built using Python's `tkinter` library. It allows users to generate strong, customizable passwords based on specified criteria such as length and character types (uppercase letters, lowercase letters, numbers, and special characters). The application also features a password strength checker and integrates with the clipboard to facilitate easy copying of generated passwords.

## API Reference

This project does not utilize any external APIs. All functionalities are implemented using Python's standard libraries (`tkinter`, `random`, `string`, `pyperclip`).

## Color Reference

The Password Generator GUI utilizes the following colors:
- **Background Color:** Light Blue (`#ADD8E6`)
- **Button Color:** Dark Cyan (`#008080`)
- **Strength Indicators:** Red for Weak, Orange for Medium, Green for Strong

## Features

- **Customizable Password Generation:** Users can specify the length of the password and select which types of characters to include (uppercase letters, lowercase letters, numbers, special characters).
- **Password Strength Checker:** Evaluates password strength based on criteria such as length, presence of uppercase and lowercase letters, digits, and special characters.
- **Clipboard Integration:** Copies generated passwords to the clipboard with a single click for easy use in other applications.

## Modules Used

- **tkinter**: Python's standard GUI library for creating graphical user interfaces.
- **random**: Python's standard library for generating random numbers and selections.
- **string**: Python's standard library providing constants and classes for string manipulation.
- **pyperclip**: Python module for cross-platform clipboard functions.

## Environment Variables

This project does not require any specific environment variables.

## Demo

Include screenshots or gifs demonstrating the application's functionality. Here's an example screenshot:
![Screenshot (104)](https://github.com/user-attachments/assets/42aed5d9-a3ff-4ead-aa31-0bed9eb44c37)

## Installation

To run the Password Generator locally, ensure you have Python installed on your system. Install the required Python modules using pip:

```bash
pip install tkinter pyperclip
```

## Lessons Learned

- **GUI Development:** Enhanced understanding of developing GUI applications using `tkinter`.
- **Password Generation:** Learned techniques for generating secure and customizable passwords.
- **Clipboard Management:** Utilized `pyperclip` for copying passwords to the clipboard.

## Optimizations

Future enhancements for the Password Generator could include:
- **Password Policy Options:** Adding options for enforcing specific password policies.
- **User Preferences:** Allowing users to save their preferred settings.
- **Enhanced UI:** Improving the user interface with themes or customization options.

## Run Locally

To run the Password Generator locally after installation, execute the following command:

```bash
python password_generator.py
```

## Running Tests

This project does not currently include automated tests. Manual testing has been conducted to ensure functionality and correctness of the app.

## Usage/Examples

After running the application, specify the desired password length and select the types of characters to include (uppercase, lowercase, numbers, special characters). Click "Generate Password" to create a password, which can then be copied to the clipboard using the "Copy" button.

## Sample output
![Screenshot (104)](https://github.com/user-attachments/assets/cfe704a5-e006-4682-9c46-a59cc484a45b)
![Screenshot (103)](https://github.com/user-attachments/assets/1e77e833-708b-4ce4-822b-b093be611456)
![Screenshot (102)](https://github.com/user-attachments/assets/26b778dd-2743-4f15-ad9d-c586b17472c7)
![Screenshot (101)](https://github.com/user-attachments/assets/ec7dd1bb-6dc1-401a-81fd-31b83dc47773)
![Screenshot (100)](https://github.com/user-attachments/assets/221cabaf-5b10-4232-92e7-508e3e8cf110)
![Screenshot (99)](https://github.com/user-attachments/assets/b5b55d72-0e29-4c22-8543-8476a9c335e6)
