# Python for AI

A hands-on collection of Python lessons and small projects. It starts with the
language basics, moves into object-oriented programming, and then applies those
ideas to web data, charts, files, and a small sales analysis.

> **Learning tip:** Work through the numbered scripts in order when you are
> starting out. Each file is a small example you can run, change, and run again.

## How the repository is organized

The folders show a natural learning path: begin with short, focused scripts;
group related object-oriented lessons together; then keep the code, data, and
outputs of practical projects in their own folders. The
[`my_uv_project/`](my_uv_project/) folder is a separate example of a Python
package managed with `uv`.

```text
Python-for-AI/
├── 01_basics.py ... 07_formatting_with_ruff.py   # Core Python and practical tools
├── python_oops/                                   # Classes and object-oriented Python
├── sales-analysis-project/                        # A small CSV sales analysis
├── my_uv_project/                                 # A packaged project using uv
├── data/                                          # Weather data saved by an example
├── 00-Resources/                                  # Reference PDFs
├── requirements.txt                               # Dependencies for the root examples
└── PYTHON-AI.code-workspace                       # VS Code workspace
```

In short:

```text
Python basics -> reusable functions -> classes and objects -> real data -> projects
```

## What you will learn

### 1. Python fundamentals

The numbered scripts in the repository root introduce the building blocks of
Python:

| File | What it covers |
| --- | --- |
| [`01_basics.py`](01_basics.py) | Variables, comments, common data types, operators, strings, conditions, loops, and lists. |
| [`02_functions.py`](02_functions.py) | Defining and calling functions, passing parameters, and returning results. |
| [`03_external_tools.py`](03_external_tools.py) | Importing standard-library modules, making a web request with `requests`, and reading JSON data. |
| [`04_get_data.py`](04_get_data.py) | Fetching Paris weather data, putting it in a pandas table, drawing a chart, and saving a CSV and image. |
| [`05_error_handling.py`](05_error_handling.py) | Catching a `ValueError` when text entered by a user cannot be converted to an integer. |
| [`06_env_variables.py`](06_env_variables.py) | Reading settings from environment variables and loading a local `.env` file with `python-dotenv`. |
| [`07_formatting_with_ruff.py`](07_formatting_with_ruff.py) | A small function example and notes about formatting Python code with Ruff. |

These examples demonstrate a useful pattern: get information, transform it,
then present or save the result. For example, the weather script requests data,
organizes it into columns, plots temperatures, and writes files for later use.

### 2. Object-oriented Python

[`python_oops/`](python_oops/) collects lessons about classes, objects, and
methods. A class is a reusable description; an object is one particular
instance made from that description. The examples use students, cars, accounts,
and orders to make the ideas concrete.

| File | Main idea |
| --- | --- |
| [`01_basics.py`](python_oops/01_basics.py) | Creating a class and objects, using `__init__` to set up an object, and referring to that object with `self`. |
| [`02_attributes.py`](python_oops/02_attributes.py) | The difference between attributes shared by a class and attributes belonging to each object. |
| [`03_methods.py`](python_oops/03_methods.py) | Defining methods that use an object's data. |
| [`04_practise_question1.py`](python_oops/04_practise_question1.py) | Practice: store a student's marks and calculate their average. |
| [`05_static_methods.py`](python_oops/05_static_methods.py) | Static methods for utility behavior, alongside an instance method that calculates an average. |
| [`06_abstraction.py`](python_oops/06_abstraction.py) | Providing a simple operation while keeping its internal steps out of the way. |
| [`07_encapsulation.py`](python_oops/07_encapsulation.py) | Keeping related data and behavior together in a class. |
| [`08_practise_question2.py`](python_oops/08_practise_question2.py) | Practice: model an account with credit, debit, and balance operations. |
| [`09_del_keyword.py`](python_oops/09_del_keyword.py) | Removing a variable reference with `del`. |
| [`10_private_att_and_methods.py`](python_oops/10_private_att_and_methods.py) | Double-underscore attribute and method names, and accessing them from within a class. |
| [`11_inheritance.py`](python_oops/11_inheritance.py) | Reusing behavior by deriving one class from another, including examples of single, multilevel, and multiple inheritance. |
| [`12_super_keyword.py`](python_oops/12_super_keyword.py) | Calling a parent-class initializer or method with `super()`. |
| [`13_class_method.py`](python_oops/13_class_method.py) | Instance, class, and static methods, and how a class method receives the class as `cls`. |
| [`14_property_decorator.py`](python_oops/14_property_decorator.py) | Calculating a value with `@property` so it reflects the object's current data. |
| [`15_polymorphism.py`](python_oops/15_polymorphism.py) | The same operation behaving differently for different types, including custom addition with `__add__`. |
| [`16_practise_question3.py`](python_oops/16_practise_question3.py) | Practice: calculate the area and perimeter of a circle. |
| [`17_practise_question4.py`](python_oops/17_practise_question4.py) | Practice: extend an employee class to represent an engineer. |
| [`18_practise_question5.py`](python_oops/18_practise_question5.py) | Practice: compare orders by price with the `__gt__` special method. |

The word "private" in the filename is a useful starting point, but Python's
double-underscore naming is not a security boundary. It changes how an
attribute name is stored; it does not protect secrets from determined access.
Similarly, `del` removes a name or attribute reference; it does not promise that
an object's memory is immediately reclaimed if other references still exist.

### 3. Small, practical projects

#### Weather data

[`04_get_data.py`](04_get_data.py) requests daily weather values for Paris from
the Open-Meteo API. It uses pandas to organize the response and Matplotlib to
plot minimum and maximum temperatures. When run from the repository root, it
saves a chart as [`weather_chart.png`](weather_chart.png) and writes the table
to [`data/paris_weather.csv`](data/paris_weather.csv). It needs an internet
connection to request the data.

#### Sales analysis

[`sales-analysis-project/`](sales-analysis-project/) separates a small analysis
into reusable helpers and a script:

- [`analyzer.py`](sales-analysis-project/analyzer.py) reads
  [`data/sales.csv`](sales-analysis-project/data/sales.csv), calculates each
  row's total, and prints formatted line totals and a grand total.
- [`helpers.py`](sales-analysis-project/helpers.py) contains the calculations
  and currency formatting used by the analyzer.
- [`output/`](sales-analysis-project/output/) contains CSV, JSON, and Excel
  sales files already in the repository. The current `analyzer.py` prints its results; it does not write
  those output files.

This project illustrates why it helps to split work into small functions and
keep input data and output files in clearly named folders.

#### A `uv` package

[`my_uv_project/`](my_uv_project/) is a minimal installable Python package,
rather than a set of standalone lessons:

- [`pyproject.toml`](my_uv_project/pyproject.toml) describes the package, its
  Python requirement (Python 3.13 or newer), its pandas dependency, and the
  `my-uv-project` command.
- [`uv.lock`](my_uv_project/uv.lock) records the resolved dependency versions.
- [`src/my_uv_project/__init__.py`](my_uv_project/src/my_uv_project/__init__.py)
  contains the package's `main()` function.
- [`.python-version`](my_uv_project/.python-version) records the Python version selected for this project.

The package has its own environment and dependency setup; treat it separately
from the root-level examples.

### 4. Reference material and workspace files

- [`00-Resources/`](00-Resources/) contains a Git cheat sheet and Windows
  keyboard shortcuts.
- [`python_oops/python_oops_notes.pdf`](python_oops/python_oops_notes.pdf)
  contains additional object-oriented Python notes.
- [`requirements.txt`](requirements.txt) lists the pinned packages for the
  root examples, including `requests`.
- [`PYTHON-AI.code-workspace`](PYTHON-AI.code-workspace) opens this repository
  as a VS Code workspace.
- [`.gitignore`](.gitignore) excludes `.env` files so local environment
  settings need not be committed.

## Getting started

Use Python 3 and a terminal opened at the repository root. Create and activate
a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux, activate it with:

```sh
source .venv/bin/activate
```

Install the root requirements:

```sh
python -m pip install -r requirements.txt
```

Some lessons use additional packages not listed in the root
`requirements.txt`. To run the weather chart and `.env` examples, install:

```sh
python -m pip install pandas matplotlib python-dotenv
```

For example, run a beginner lesson or the weather script from the repository
root:

```sh
python 01_basics.py
python 04_get_data.py
```

Run an object-oriented exercise the same way, using its path:

```sh
python python_oops/01_basics.py
```

For the sales example, change into its folder first because its input path is
relative to that folder:

```sh
cd sales-analysis-project
python analyzer.py
```

To try the package project, install `uv`, then run these commands from its
folder:

```sh
cd my_uv_project
uv sync
uv run my-uv-project
```

## A few helpful habits

- Run one lesson at a time and change a small part to see what happens.
- Keep input data, source code, and generated results easy to tell apart.
- Use functions for repeated tasks and clear names for variables and files.
- Handle expected errors close to where they can occur.
- Keep real passwords, API keys, and other secrets out of source control. The
  environment-variable lesson prints its example API key; use only a dummy
  value when trying it, and do not print real secrets.
- Some scripts use relative file paths, so run them from the folder specified
  above.

This repository is a learning workspace, not a single application. Its examples
are meant to be explored independently, and the projects show how those basic
ideas can grow into more organized code.
