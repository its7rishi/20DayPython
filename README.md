# A 20 Day Python Learning Plan

## Days 1–7 — Foundations

### Day 1 — Setup + First steps

#### Goals: Install Python, VS Code, create venv, run scripts, use REPL.

- Do: Write a "Hello, <name>" program, practice running it, commit to Git.

### Day 2 — Variables, types, I/O

- Topics: int, float, str, bool, type conversion, print, input, f-strings.

- Exercises: calculator (add/sub/mul/div), parse input, format output.

### Day 3 — Control flow

- Topics: if, elif, else, boolean logic, truthiness.

- Exercises: grade calculator, number sign checker, simple login/password check.

### Day 4 — Loops & comprehensions

- Topics: for, while, break, continue, list comprehensions.

- Exercises: iterate lists, sum numbers, generate squares with comprehension.

### Day 5 — Collections

- Topics: list, tuple, set, dict, common methods (append, pop, get, keys, items).

- Exercises: frequency counter for words, unique items, dict lookup tasks.

### Day 6 — Functions

- Topics: def, parameters, default args, \*args, \*\*kwargs, return values, docstrings, anonymous lambda.

- Exercises: write reusable functions (e.g., is_prime(n), factorial(n)).

### Day 7 — Strings & file I/O

- Topics: slicing, .split(), .join(), .format()/f-strings, reading/writing files, CSV basics.

- Exercises: read a text file and count word frequency, write results to CSV.

## Days 8–14 — Core Python skills & tooling

### Day 8 — Modules, packages, pip, venv deeper

- Topics: import, module search path, creating packages, pip install, requirements.txt.

- Exercises: build a small package, use requests (or similar) to fetch a web page.

### Day 9 — Errors, debugging, and testing

- Topics: exceptions (try/except/finally), inspect tracebacks, assert, intro to testing with unittest or pytest.

- Exercises: add input validation to earlier scripts; write a couple of unit tests.

### Day 10 — Object-Oriented Programming (OOP)

- Topics: classes, objects, **init**, instance vs class attributes, methods.

- Exercises: model a BankAccount or Book class with deposit/withdraw or borrow/return.

### Day 11 — Advanced OOP & patterns

- Topics: inheritance, composition, **repr**, **str**, @property, static & class methods.

- Exercises: extend previous class with subclass (e.g., SavingsAccount).

### Day 12 — Iterators & generators

- Topics: iter, next, writing iterator classes, yield, generator expressions.

- Exercises: implement generator for Fibonacci, streaming file processing.

### Day 13 — Standard library essentials

- Topics: os, pathlib, sys, datetime, collections (Counter, defaultdict), itertools.

- Exercises: write a script to walk directories and produce a file report (sizes, counts).

### Day 14 — Working with data (JSON, CSV, HTTP)

- Topics: json module, CSV module / pandas intro, requests for HTTP, basic scraping with BeautifulSoup (ethics/legal caution).

- Exercises: fetch a public API (e.g., open data), parse JSON, save results.

## Days 15–18 — Applied Python

### Day 15 — Intro to web apps (Flask or FastAPI)

- Topics: routes, request/response, templates (Jinja2), simple REST endpoints.

- Exercises: build a tiny Flask app with 2 routes and one HTML template (To-Do list backend).

### Day 16 — Databases & persistence

- Topics: SQLite basics, SQL queries (SELECT/INSERT/UPDATE/DELETE), ORM intro (SQLAlchemy).

- Exercises: connect your Flask app to SQLite and save/retrieve tasks.

### Day 17 — Data analysis & plotting

- Topics: pandas (DataFrame, read_csv, groupby), matplotlib basics.

- Exercises: analyze a CSV dataset (sales/grades), produce simple plots, export cleaned CSV.

### Day 18 — Testing, debugging, packaging & style

- Topics: pytest (tests, fixtures), debugging with breakpoints, logging, flake8/PEP8, type hints (mypy basics), packaging (setup.cfg, pyproject.toml high level).

- Exercises: write tests for your app functions, add logging, run linters.

## Days 19–20 — Capstone & deployment

### Day 19 — Capstone build day

- Pick one capstone (see options below). Build core features and tests:

- Solid README, git history, unit tests, basic UI or CLI.

- Break tasks into: data model → core logic → interface → tests.

### Day 20 — Polish & deploy

- Polish UX, add input validation, finalize tests.

- Deploy: push repo, pick a simple host (for web apps: Render, Railway, or similar) or package as CLI / share Jupyter notebook.

- Create a 2–3 minute demo (screen record or README GIF), show how to run.
