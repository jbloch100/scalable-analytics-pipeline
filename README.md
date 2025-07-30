# Scalable Analytics Pipeline

## Overview
Simulates a simple analytics event processor for backend engineering. Processes mock ad events in real-time and generates aggregated metrics.

## Features
- Processes click/view/impression events
- Aggregates data in real-time
- CLI output summary

## Run
```bash
python src/main.py
```

## Test
```bash
python -m unittest tests/test_main.py
```

---

## Docker

### Build
```bash
docker build -t scalable-analytics-pipeline .
```

### Run
```
docker run --rm scalable-analytics-pipeline
```

### Test
```
docker run --rm scalable-analytics-pipeline python -m unittest discover -s tests
```
