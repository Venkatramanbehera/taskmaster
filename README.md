# TaskMaster

TaskMaster is a lightweight, modular RESTful API built with **FastAPI** and modern Python dependency management using **uv**. It demonstrates clean API versioning, Pydantic data validation, and strict code quality enforcement using **Ruff** and **Mypy**.

---

## 📁 Project Structure

```text
taskmaster/
├── app/
│   ├── __init__.py
│   ├── main.py                  # FastAPI application entrypoint & root routes
│   └── api/
│       ├── __init__.py
│       └── v1/
│           ├── __init__.py
│           └── endpoints.py     # Version 1 Task API endpoints & Pydantic models
├── examples/
│   └── typing.ipynb             # Jupyter notebook for experiments & typing references
├── pyproject.toml               # Project configuration, dependencies, and tool settings
├── uv.lock                      # Exact lockfile for reproducible uv installs
├── requiremetnts.txt            # Fallback pip requirements file
└── README.md                    # Project documentation
```

### Module Breakdown
- **`app/main.py`**: Initializes the FastAPI instance, mounts the `/v1` router, and provides a root health probe endpoint (`/health`).
- **`app/api/v1/endpoints.py`**: Houses the Task schema (`Task`), in-memory storage, and CRUD route handlers under prefix `/v1`.
- **`pyproject.toml`**: Unified configuration file for dependencies, FastAPI entrypoint (`tool.fastapi`), Ruff linter/formatter rules, and Mypy strict typing configurations.

---

## 🚀 Getting Started

### Prerequisites
- **Python**: `>=3.12` (configured with support for Python 3.12+)
- **uv** (recommended): [Astral uv](https://github.com/astral-sh/uv) fast Python package manager

### 1. Installation

#### Using `uv` (Recommended)
Clone the repository and synchronize the environment:
```bash
# Sync dependencies including dev tools (ruff, mypy)
uv sync
```

#### Using standard `pip` and virtual environment
```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requiremetnts.txt
pip install ruff mypy
```

---

## 🏃 Running the Application

### Development Mode (with hot-reload)
```bash
# Using uv:
uv run fastapi dev

# Or with virtual environment activated:
fastapi dev
```
The server will start at `http://127.0.0.1:8000`.

### Production Mode
```bash
uv run fastapi run app/main.py
```

### Interactive API Documentation
Once running, open your browser to:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📡 API Endpoints

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| `GET` | `/health` | Service health check | `200 OK` |
| `GET` | `/v1/tasks/` | Retrieve list of all tasks | `200 OK` |
| `POST` | `/v1/tasks` | Create a new task | `201 Created` |
| `GET` | `/v1/tasks/{task_id}` | Fetch a task by its ID | `200 OK` / `404 Not Found` |

### Example Request Payloads

#### Create a Task (`POST /v1/tasks`)
```json
{
  "id": 1,
  "name": "Complete documentation",
  "description": "Write comprehensive README with Ruff and Mypy guides"
}
```

---

## 🛠️ Code Quality Tools: Ruff & Mypy

This project enforces strict code quality and typing standards defined in [`pyproject.toml`](file:///Users/chiku/Desktop/Backend-Projects/taskmaster/pyproject.toml).

---

### 1. Ruff (Linter & Formatter)

[Ruff](https://docs.astral.sh/ruff/) is an extremely fast Python linter and code formatter written in Rust. It replaces Flake8, Black, isort, pyupgrade, and more.

#### Configuration in `pyproject.toml`
- **Line Length**: `88` characters
- **Target Version**: Python 3.12 (`py312`)
- **Enabled Rule Sets**:
  - `E` / `W`: Pycodestyle (errors and warnings)
  - `F`: Pyflakes (logical & syntax checks, unused imports)
  - `I`: isort (import sorting)
  - `B`: flake8-bugbear (common bug & design anti-patterns)
  - `UP`: pyupgrade (modern Python syntax upgrades)

#### Common Ruff Commands

```bash
# 1. Run linter checks across the codebase
uv run ruff check .

# 2. Automatically fix safe lint issues (e.g. unused imports, sorting)
uv run ruff check --fix .

# 3. Check code formatting without making changes
uv run ruff format --check .

# 4. Format all Python files
uv run ruff format .
```

> **Tip:** If running inside an activated virtualenv (`source .venv/bin/activate`), you can omit `uv run` and run `ruff check .` or `ruff format .` directly.

---

### 2. Mypy (Static Type Checker)

[Mypy](https://mypy.readthedocs.io/) is an optional static type checker for Python that catches type mismatches, missing annotations, and `None`-handling bugs before runtime.

#### Configuration in `pyproject.toml`
- `python_version = "3.12"`
- `warn_return_any = true`: Warns when returning a value with type `Any`.
- `warn_unused_configs = true`: Warns about unparsed configuration settings.
- `disallow_untyped_defs = true`: Requires all function definitions to have explicit argument and return type annotations.
- `ignore_missing_imports = true`: Silences missing stub warnings for third-party packages without typing stubs.

#### Common Mypy Commands

```bash
# Run type check on the app module
uv run mypy app

# Run type check across the entire project
uv run mypy .
```

#### Writing Type-Safe Code for TaskMaster
Because `disallow_untyped_defs = true` is enabled, all route handlers and functions must declare return types:

```python
# ✅ Correct: Explicit argument and return type
@router.get("/tasks/", status_code=status.HTTP_200_OK)
async def all_task() -> list[Task]:
    return tasks


# ❌ Incorrect: Missing return type annotation (causes Mypy error)
@router.get("/tasks/", status_code=status.HTTP_200_OK)
async def all_task():
    return tasks
```

---

### 🚀 All-in-One QA Script

Run all linting, formatting checks, and type validation in one command:

```bash
uv run ruff check . && uv run ruff format --check . && uv run mypy app
```
