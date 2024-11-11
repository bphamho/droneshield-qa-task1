# droneshield-qa-task1
Droneshield QA Tech Challenge 1

- [droneshield-qa-task1](#droneshield-qa-task1)
  - [Prerequisites](#prerequisites)
  - [How to Install and Run Tests](#how-to-install-and-run-tests)


## Prerequisites
- Python 3.x installed on your system
- [Google Chrome](https://www.google.com/chrome/) (or another browser of choice)

## How to Install and Run Tests
1. Clone the repository to your local machine using:

```bash
git clone https://github.com/bphamho/droneshield-qa-task1.git
```

2. Navigate to the repository with

```bash
cd droneshield-qa-task
```

3. Create and activate virtual environment

- Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
- Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

5. Run all tests

```bash
pytest
```