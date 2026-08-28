# Automated Financial Audit Pipeline

A lightweight Python-based audit utility designed to help teams review financial transactions quickly and consistently. The script simulates transaction loading, identifies suspicious or negative orders, and calculates a simple 8% tax estimate for the filtered records.

## Problem Statement

Financial review processes often require manual inspection of large transaction sets, which consumes valuable time and increases the risk of human error. This project addresses that need by automating the first layer of audit analysis: detecting unusual amounts and preparing a basic tax calculation for further review.

By automating these checks, the solution helps reduce manual effort, speeds up the audit workflow, and improves consistency in identifying potentially problematic orders.  

## Features

- Load sample financial transactions from a simulated dataset.
- Filter suspicious orders based on a configurable limit.
- Detect negative or erroneous amounts that should be flagged.
- Calculate an 8% tax estimate for valid positive amounts.
- Keep the implementation clean, modular, and easy to extend.

## How to Run

1. Make sure you have Python 3 installed on your system.
2. Open a terminal in the project folder.
3. Run the script:

```bash
python audit_processor.py
```

You should see output showing the loaded transactions, the suspicious orders detected, and the total tax calculation.

## Project Structure

```text
financial-audit-script/
├── audit_processor.py
└── README.md
```

## Notes

This project is intentionally simple and educational. It is designed to demonstrate core Python concepts such as function decomposition, type hints, and basic financial data processing.

## License
MIT 
