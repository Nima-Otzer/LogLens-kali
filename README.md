**LogLens-kali**  
LogLens-kali is a beginner-built, local-first Linux log analysis tool written in Python. It reads a log file, identifies entries by severity, checks timestamps and record structure, finds repeated messages, and displays recognized events in chronological order.  

**Current features**  
    • Recognizes the eight standard syslog severity names: EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFO, and DEBUG.  
    • Counts entries by recognized severity.  
    • Detects malformed records, unknown severity labels, and invalid timestamps.  
    • Reports recurring messages and recurring high-severity messages.  
    • Displays a chronological event timeline.  
    • Reports totals for valid entries, skipped lines, unknown severity entries, and invalid timestamps.  

**Requirements**  
    • Python 3  
    • No third-party Python packages are currently required.  

**Expected input format**  
The current parser expects each valid record to follow this format:  
YYYY-MM-DD HH:MM:SS SEVERITY Message text goes here  

**Example:**  
2026-10-18 08:03:04 ERROR Application failed to open configuration file  
2026-10-18 08:03:18 INFO Configuration loaded after retry  
The timestamp must match %Y-%m-%d %H:%M:%S, and the severity must be one of the eight names listed above. Lines that do not match the expected structure may be skipped or reported as invalid.  

**Running LogLens-kali**    
    1. Make sure Python 3 is installed.  
    2. Save your log data in a text file such as sample.log.  
    3. Open LogLens-kali.py and update the file path in open(...) to point to your log file.  
    4. Run the program from a terminal:  
       python3 LogLens-kali.py  

The current version uses a file path written directly in the script. A configurable command-line path is a possible future improvement.  

**Sample data**  
Use sample.log or the separate sample file provided with the project to test normal entries, repeated messages, and different severity levels. Add malformed lines and invalid timestamps when testing the parser's error handling.  

**Current limitations**  
    • The parser expects one specific text format; it does not yet support every Linux logging format.  
    • It reads a file supplied by the user rather than automatically collecting logs from the system.  
    • Recurring messages are grouped by their message text; context and severity relationships are not yet deeply analyzed.  
    • It does not prove that a system is compromised. Log messages are evidence to investigate, not definitive diagnoses.  
    • There is no graphical interface or real-time monitoring yet.  

**Development status**  
LogLens-kali is an early working prototype under active development. Planned improvements include severity filtering, more robust support for common Linux log formats, better event summaries, tests, and evidence-based correlation of related events.  

**Safety and privacy**  
LogLens-kali is intended to analyze logs locally. Logs can contain usernames, IP addresses, session details, and other sensitive information. Use sample or redacted logs when sharing examples, and review files before publishing them.

**Project goal**  
The long-term goal is to help users investigate Linux application failures, service problems, recurring errors, and security-relevant events while clearly separating observed facts from possible explanations.
