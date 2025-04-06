# 📊 Real-Time Log Analytics System (Advanced Version)

## 🚀 Objective
Monitor application/server logs in real-time, detect anomalies, and visualize trends using AWS-managed services.

## 🧠 Overview
A scalable pipeline using AWS services to:
- Ingest logs in real time
- Perform ETL processing
- Store structured logs
- Enable SQL queries
- Visualize insights in dashboards

## 🔧 Tech Stack (AWS Services)

| Service | Purpose |
|--------|---------|
| **Amazon Kinesis Data Streams** | Real-time log ingestion |
| **Kinesis Firehose** | Delivers logs to S3 |
| **Amazon S3** | Data lake for raw/processed logs |
| **AWS Glue** | ETL (Crawlers + Jobs) |
| **Amazon EMR (Spark)** | Batch analytics and transformations |
| **Amazon Athena** | SQL queries on processed logs |
| **Amazon QuickSight** | Dashboards and visualizations |

## 🧰 Architecture Steps

1. Logs ingested via Python → Kinesis Data Stream
2. Streamed to S3 using Kinesis Firehose
3. Crawled and transformed using AWS Glue
4. Processed with Athena
5. Visualized in QuickSight

## 📂 Folder Structure

```
log-analytics-project/
├── kinesis_log_ingestion.py   # Real-time log ingestion script
├── README.md                  # Project overview
```

## 🧪 Python Log Ingestion Example

```python
import boto3
import json
import time
import random
from datetime import datetime

kinesis = boto3.client('kinesis', region_name='us-east-1')

def generate_log():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "level": random.choice(["INFO", "WARNING", "ERROR"]),
        "service": random.choice(["auth", "payments", "orders", "search"]),
        "message": random.choice(["Operation completed", "Timeout occurred", "Invalid input", "User logged in"])
    }

while True:
    log_entry = generate_log()
    kinesis.put_record(
        StreamName="your-kinesis-stream-name",
        Data=json.dumps(log_entry),
        PartitionKey="partitionKey")
    print(f"Sent: {log_entry}")
    time.sleep(1)
```

## ✅ Outcome

A real-time and batch-capable log analytics system with a serverless AWS architecture.
