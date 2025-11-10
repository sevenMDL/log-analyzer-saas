# Log Analyzer SaaS (Python + Flask)

A minimal Flask API that automatically detects log file types — built as an experiment exploring the boundary between a simple script and a micro SaaS.

## Features

-Identifies router, web server, system, and application error logs
- Single POST endpoint: /analyze
- Provides clean JSON output
- No dependencies beyond Flask and regex

## Usage

```bash
pip install flask
python3 log_analyzer_flexible.py
```

Submit a log file:

```bash
curl -X POST -F "file=@logs/sample_router.log" http://localhost:3000/analyze
```

Example Response:

```json
{
  "detected_log_type": "router/network interface log",
  "total_lines": 11,
  "sample_preview": [...]
}
```

## Concept

This began as a personal tool for router traffic analysis and grew into a simple API concept — part of investigating what constitutes a "micro SaaS" offering.

## Repository Structure

```
app.py                    → Flask server
logs/                     → Sample log files  
README.md                 → This document
```
