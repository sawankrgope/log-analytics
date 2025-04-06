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
