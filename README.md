
# Health Monitoring System
The Health Monitoring System is a Python-based application that uses fuzzy logic to assess a person's health based on body temperature, pulse rate, and SpO2 levels. It calculates a severity level and provides recommendations, offering an intuitive, visual, and interactive experience with real-time feedback and alerts.

![Screenshot 2024-11-08 031503](https://github.com/user-attachments/assets/67d58b14-755a-47f6-84c1-f208e0c92da6)


## Table of Contents

- **Features**
- **Installation**
- **Usage**
- **Code Structure**
- **Example Scenarios**
- **Future Enhancements**
- **Contributions**
- **License**

## Features

- **Fuzzy Logic-based Health Evaluation**: Determines severity based on body temperature, pulse rate, and SpO2 level using fuzzy inference.
- **Dynamic GUI**: Interactive user interface with real-time input validation and color-coded alerts for health severity.
- **Visualizations**: Membership function plots provide visual feedback on input values and their interpretation by the fuzzy logic system.
- **Error Handling**: Alerts for invalid inputs and cases where no fuzzy rule matches the given inputs.

## Installation

### Prerequisites

- **Python 3.x**
- **Required libraries**: numpy, scikit-fuzzy, matplotlib, tkinter

### Step-by-Step Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/health-monitoring-system.git
    cd health-monitoring-system
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Application**:
    ```bash
    python main.py
    ```

2. **Input Data**: Enter values for:
   - **Body Temperature (°C)**
   - **Pulse Rate (BPM)**
   - **SpO2 Level (%)**

3. **Evaluate Health Status**: Click "Evaluate Health Status" to calculate severity. The system displays severity level, recommendation, and visualizations.

4. **Error Handling**: Guides user on invalid inputs and unrecognized combinations.

## Code Structure

The codebase is organized for modularity and readability:

```
health-monitoring-system/
|
├── main.py             # Main file for GUI setup and program execution
├── fuzzy_logic.py      # Defines fuzzy logic variables, rules, and severity calculation
├── validation.py       # Handles input validation and error handling
├── plotting.py         # Manages the plotting of membership functions
├── style.py            # Stores styling configurations for the GUI
└── README.md           # Project documentation
```

## Example Scenarios

1. **Normal Health Condition**:
   - Inputs: Body Temperature: 37.0, Pulse Rate: 80, SpO2 Level: 98
   - Output: Low severity, stable condition.

2. **Medium Severity**:
   - Inputs: Body Temperature: 38.5, Pulse Rate: 95, SpO2 Level: 90
   - Output: Medium severity, regular monitoring suggested.

3. **Very High Severity (Critical)**:
   - Inputs: Body Temperature: 40.0, Pulse Rate: 50, SpO2 Level: 82
   - Output: Very high severity with recommendation for immediate medical attention.

## Future Enhancements

- **Historical Data Tracking**: Save and view data trends.
- **Enhanced Rules and Membership Functions**: More complex health assessments.
- **Mobile and Web Versions**: Wider accessibility.
- **Multi-Language Support**: Options for non-English users.

## Contributions

Contributions are welcome!

1. **Fork the repository**.
2. **Create a new branch** (git checkout -b feature-branch).
3. **Commit your changes** (git commit -m 'Add new feature').
4. **Push to the branch** (git push origin feature-branch).
5. **Open a Pull Request**.

## License

This project is licensed under the MIT License.
