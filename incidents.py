import csv
import json

def analyze_incidents(input_path, output_path):
    with open(input_path, 'r') as file:
        reader = csv.DictReader(file)
        valid_incidents = 0
        invalid_incidents = 0
        resolved_duration = 0 
        service_counts = {}
        for row in reader:
            try:
                duration = int(row['duration'])
                if duration < 0:
                    raise ValueError("Negative duration")
                valid_incidents += 1
                if row['status'] == 'resolved':
                    resolved_duration += duration
                service_counts[row['service']] = service_counts.get(row['service'], 0) + 1
            except ValueError:
                invalid_incidents += 1

    report = {
        'valid_incidents': valid_incidents,
        'invalid_incidents': invalid_incidents,
        'resolved_duration': resolved_duration,
        'service_counts': service_counts
    }

    with open(output_path, 'w') as outfile:
        json.dump(report, outfile)


    return report

if __name__ == "__main__":
    analyze_incidents("incidents.csv", "report.json")   

