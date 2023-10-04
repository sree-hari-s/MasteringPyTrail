# Parking Operator Sim

## Overview

The Parking Operator Sim allows users to take on the role of managing a car park where they can add a car's number plate, calculate the cost of parking depending on the duration of the stay, and remove the car when they paid and exited.

## Features

- **Interactive Application**
  - Users can choose from a list of task on the command line.

- **State Tracking**
  - Keeps track of the current cars and saves a history of the stay.

- **Calculate Price**
  - The cost of the stay is calculted by getting the difference of the entry time and exit time in minutes after one minute. 
## How to Use

1. Run the Parking Operator on your device.

2. Enter the number of choice from the options below: 

    1. Display all cars.
    2. Add a car - The app will ask for the car's number plate.
    3. Pay for parking - The app will ask for the car's id and to type the price of the stay.
    4. Remove car - Asks users for the id; removes car from the car collection and add it to the history.
    5. Display history
    9. Quit program.

3. Enjoy the simulation and increase the maximum cars.

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Change directory to Quiz App: 
   ```bash
    cd "Quiz App"
   ```

3. Run the app:
   ```bash
   python main.py
   ```

## Contribution Guidelines

Contributions to the Quiz App are welcome! If you'd like to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature/fix: `git checkout -b feature/your-feature`.
3. Make your changes and commit them: `git commit -m 'Add feature/fix'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Create a pull request, explaining the changes made.


Replace `<repository_url>` with the actual URL of your repository. Customize the content according to your specific project and requirements.
