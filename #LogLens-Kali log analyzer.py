from datetime import datetime

severity_counts = {
    'EMERGENCY': 0,
    'ALERT': 0,
    'CRITICAL': 0,
    'ERROR': 0,
    'WARNING': 0,
    'NOTICE': 0,
    'INFO': 0,
    'DEBUG': 0
}

high_severity_levels = ['EMERGENCY', 'ALERT', 'CRITICAL', 'ERROR']

skipped_count = 0
unknown_count = 0
invalid_count = 0
high_severity_message_count = {}

with open('/home/manjusri/Documents/Terra/Loglens/sample.log') as file:
   
    events = []
    message_count = {}
    for line in file:
        parts=line.split()
        if len(parts) < 4:
            print(f"Skipping line due to insufficient data! {line.strip()}")
            skipped_count += 1
            continue
        if len(parts[0]) != 10 or len(parts[1]) != 8:
            print(f"skipping malformed record: {line.strip()}")
            skipped_count += 1
            continue
        timestamp = parts[0] + " " + parts[1]
        try:
            datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print(f"Invalid timestamp format: {timestamp}")
            invalid_count += 1
            continue   

        severity = parts[2]

        if severity in severity_counts:
            severity_counts[severity] += 1

            event={
                "timestamp": timestamp,
                "severity": severity,
                "message": " ".join(parts[3:])
            }
            events.append(event)

            print(f"{severity}: {line.strip()}")
        else:
            print(f"Unknown severity level: {line.strip()}")
            unknown_count += 1   
        if severity in high_severity_levels:
            error_message = " ".join(parts[3:]) 
            high_severity_message_count[error_message] = (high_severity_message_count.get(error_message, 0) + 1)

            message = " ".join(parts[3:])
            message_count[message] = message_count.get(message, 0) + 1
        
print("\nEvent timeline:")
    
for event in sorted(events, key=lambda event: event ["timestamp"]):
        print(
            f'{event["timestamp"]} |'
            f' {event["severity"]} |'
            f' {event["message"]}'
        )    
        

print("\nRecurring high-severity messages:")
for message, count in high_severity_message_count.items():
    if count > 1:
        print(f"{message}: {count} times")        

print("\nRecurring messeages:")
for message, count in message_count.items():
    if count > 1:
        print(f"{message}: {count} times")

print("\nSummary of log severity counts:")
for severity, count in severity_counts.items():
    print(f"{severity}: {count}")
Total_valid = sum(severity_counts.values())
Total_processed = (
    Total_valid
   +skipped_count
   +unknown_count
   +invalid_count
)
print(f"\nTotal valid log entries: {Total_valid}")
print(f"Total log entries processed: {Total_processed}")
print(f"Total skipped lines: {skipped_count}")
print(f"Total unknown severity entries: {unknown_count}")
print(f"Total invalid timestamps: {invalid_count}")