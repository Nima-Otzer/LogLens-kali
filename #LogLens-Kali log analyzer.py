#LogLens-Kali log analyzer
error_count = 0
warning_count = 0
info_count = 0

with open('/home/manjusri/Documents/Terra/Loglens/sample.log') as file:
    for line in file:
        parts=line.split()
        print(parts[2])
        if 'error' in line.lower():
            print(f"Error found: {line.strip()}")
            error_count += 1
        elif 'warning' in line.lower():
            print(f"Warning found: {line.strip()}")
            warning_count += 1
        elif 'info' in line.lower():
            print(f"Info found: {line.strip()}")
            info_count += 1


print(f"Total errors: {error_count}")
print(f"Total warnings: {warning_count}")
print(f"Total info messages: {info_count}")   
