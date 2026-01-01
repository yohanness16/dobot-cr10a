# Robotics Project with Peter Corke's Robotics Toolbox

This project uses Python and Peter Corke’s [Robotics Toolbox](https://petercorke.com/toolboxes/robotics-toolbox/) for robotics simulations and analysis.

## Prerequisites

- Python 3.11.2 installed on your system
- Git installed
- `pip` installed
- `virtualenv` or `venv` for creating virtual environments
- Jupyter Notebook

---

## Clone the Project

Clone this repository to your local machine:

```bash
git clone <your-repo-link>
cd <your-project-folder>

```

## Create Python Virtual Environment

Create a virtual environment with Python 3.11.2:

```bash
python3.11 -m venv venv

```

Activate the environment:

On Linux/macOS:

```bash
source venv/bin/activate
```
On Windows (Command Prompt):
```bash

venv\Scripts\activate

```

## install Requirements

Install the required Python packages listed in requirements.txt:
```bash
pip install --upgrade pip
pip install -r requirements.txt

```
This will install petercorke/roboticstoolbox-python and other dependencies.



## Run the code

Launch Jupyter Notebook:
```bash
jupyter notebook
```


Then open the notebooks in your project folder and start running your robotics simulations.

## Notes

Make sure your virtual environment is activated before running the notebooks.

If you face any issues installing packages, check Python version and package compatibility.