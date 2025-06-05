# Math Expression Parser

This project features a straightforward arithmetic expression parser, with implementations available in both **Python** and **C#**. It handles fundamental mathematical operations such as addition, subtraction, multiplication, division, and parentheses.

---

## Project Structure

* `python-version/`: Contains the Python implementation of the parser.
* `csharp-version/`: Contains the C# implementation using .NET.
* `README.md`: This project documentation file.

---

## Running the Python Version

1.  Navigate to the `python-version/` directory.
2.  Execute the script:
    ```bash
    python main.py --math "test.math"
    ```

---

## Running the C# Version

1.  Navigate to the `csharp-version/` directory.
2.  Build and run the project using the .NET CLI:
    ```bash
    dotnet build
    dotnet run
    ```
    **Note:** This requires the [.NET SDK](https://dotnet.microsoft.com/download) to be installed on your system.

---

## Example Inputs and Outputs

Here are some examples of expressions the parser can handle, along with their expected results:

* `2 + 3 * 4` → `14`
* `-(5 + 2)` → `-7`
* `3 * (1 + 2)` → `9`
* `10 / (2 + 3)` → `2`

---

## Purpose

This parser serves as a demonstration of how to construct a **recursive descent parser** for arithmetic expressions. It's intended as a learning resource and a comparative study between the Python and C# programming languages.

---

## License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).
