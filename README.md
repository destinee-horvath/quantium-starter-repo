# Quantium starter repo

## Prerequisites

- Python 3.8+
- `pip` 

## Setup

1. Create a virtual environment:

```bash
python -m venv venv
```

2. Activate the virtual environment:

Windows:
```bash
venv\Scripts\activate
```

Linux: 
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Project 
To process the data: 
```bash
python data_processing.py
```

To run the visualiser: 
```bash
python dash_visualiser.py
```

## Running Tests 
To run the test suite: 
```bash
pytest
```