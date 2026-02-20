# Advanced Scientific & Physics Calculator

A robust, engineering-focused calculator built with Python and PySide6. This tool goes beyond basic arithmetic by integrating a comprehensive library of physical constants and advanced mathematical functions.

## Key Features

* **Comprehensive Math Suite:** Supports trigonometric, hyperbolic, logarithmic, and factorial operations.
* **Physics Library:** Instant access to constants across multiple fields:
    * **Quantum Mechanics:** Planck constant ($h$), Bohr radius ($a_0$), etc.
    * **Electromagnetism:** Speed of light ($c$), vacuum permittivity ($\varepsilon_0$), and more.
    * **Astronomy:** Masses and radii for the Earth, Sun, Moon, and even the Milky Way.
    * **Thermodynamics:** Boltzmann constant ($k$) and Rydberg constant ($R$).
* **Memory Management:** Store and recall values using 7 dedicated registers ($x, y, z, t, a, b, c$).
* **Calculation History:** A dedicated log panel to keep track of your previous results.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/physics-calculator.git](https://github.com/yourusername/physics-calculator.git)
    cd physics-calculator
    ```

2.  **Install dependencies:**
    This project requires `PySide6`.
    ```bash
    pip install PySide6
    ```

3.  **Run the application:**
    ```bash
    python calculator.py
    ```

## Usage Tips

* **Variable Assignment:** To save a result, click the `x=` (or $y, z$, etc.) button. To use it in a new formula, simply click the corresponding `x` button.
* **Dynamic Functions:** Buttons like `sqrt`, `sin`, or `log` wrap your current input automatically for faster workflow.
* **Error Handling:** If an expression is invalid, the display will show "hatalı deneme" (invalid attempt).

## Preview
<img width="1001" height="478" alt="image" src="https://github.com/user-attachments/assets/5385ef54-d577-4264-9784-f20c2139d5c5" />

<img width="1001" height="478" alt="image" src="https://github.com/user-attachments/assets/0200b351-afa5-40c6-ac12-9b8e4b2a426c" />
