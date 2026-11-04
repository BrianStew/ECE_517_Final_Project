# Final_Project

## GitHub Repo
[GitHub Link](https://github.com/BrianStew/ECE_517_Final_Project)

## Setup
 
This project uses [uv](https://docs.astral.sh/uv/) for dependency management. Python 3.12 or newer is recommended.
 
1. Install uv if you don't have it:
```bash
   # macOS / Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
 
   # Windows (PowerShell)
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Clone the repository and enter the project folder:
```bash
   git clone <repository-url>
   cd fencing-rl
```

3. Install dependencies. This creates the `.venv` and installs the packages pinned in `uv.lock`:
```bash
   uv sync
```

Prefixing commands with 'uv run' allows uv to automatically use the virtual environment.

## Running the project
 
Play a demo bout and print matchup results:
 
```bash
uv run python main.py
```