# Log Analyzer SaaS (Python + Flask)

A minimal **Flask API** that detects the type of log file automatically — built as an experiment on the line between *a simple script* and *a micro SaaS*.

##  Features
- Detects router, web server, system, and app error logs.
- One POST endpoint: `/analyze`
- Returns clean JSON response.
- Zero dependencies beyond Flask and regex.

##  Usage

```bash
pip install flask
python3 log_analyzer_flexible.py
```

Then upload a log file:

curl -X POST -F "file=@logs/sample_router.log" http://localhost:3000/analyze

Example Output:

{
  "detected_log_type": "router/network interface log",
  "total_lines": 11,
  "sample_preview": [...]
}

 Idea

This started as a small self-check tool for analyzing router traffic, and evolved into a simple API idea — part of exploring what makes a "micro SaaS" valuable.

 Repo Structure

app.py                    → Flask server
logs/                     → Sample logs
README.md                 → This file

