import json
from incidents import analyze_incidents

def test_valid_incident(tmp_path):
    input_path = tmp_path / "test_incidents.csv"
    output_path = tmp_path / "test_report.json"
    with open(input_path, 'w') as f:
        f.write("service,status,duration\n")
        f.write("service1,resolved,5\n")
    report = analyze_incidents(input_path, output_path)
    assert report['valid_incidents'] == 1
    assert report['invalid_incidents'] == 0
    assert report['resolved_duration'] == 5
    assert report['service_counts'] == {'service1': 1}

def test_invalid_incident(tmp_path):
    input_path = tmp_path / "test_incidents.csv"
    output_path = tmp_path / "test_report.json"
    with open(input_path, 'w') as f:
        f.write("service,status,duration\n")
        f.write("service1,resolved,abc\n")
    report = analyze_incidents(input_path, output_path)
    assert report['valid_incidents'] == 0
    assert report['invalid_incidents'] == 1
    assert report['resolved_duration'] == 0
    assert report['service_counts'] == {}


def test_no_incidents(tmp_path):
    input_path = tmp_path / "test_incidents.csv"
    output_path = tmp_path / "test_report.json"
    with open(input_path, 'w') as f:
        f.write("service,status,duration\n")
    report = analyze_incidents(input_path, output_path)
    assert report['valid_incidents'] == 0
    assert report['invalid_incidents'] == 0
    assert report['resolved_duration'] == 0
    assert report['service_counts'] == {}


def test_all_valid_incidents(tmp_path):
    input_path = tmp_path / "test_incidents.csv"
    output_path = tmp_path / "test_report.json"
    with open(input_path, 'w') as f:
        f.write("service,status,duration\n")
        f.write("service1,resolved,5\n")
        f.write("service2,resolved,10\n")
    report = analyze_incidents(input_path, output_path)
    assert report['valid_incidents'] == 2
    assert report['invalid_incidents'] == 0
    assert report['resolved_duration'] == 15
    assert report['service_counts'] == {'service1': 1, 'service2': 1}
    
def test_negative_duration(tmp_path):
    input_path = tmp_path / "test_incidents.csv"
    output_path = tmp_path / "test_report.json"
    with open(input_path, 'w') as f:
        f.write("service,status,duration\n")
        f.write("service1,resolved,-5\n")
    report = analyze_incidents(input_path, output_path)
    assert report['valid_incidents'] == 0
    assert report['invalid_incidents'] == 1
    assert report['resolved_duration'] == 0
    assert report['service_counts'] == {}

    
def test_json_output(tmp_path):
    input_path = tmp_path / "test_incidents.csv"
    output_path = tmp_path / "report.json"
    input_path.write_text("service,status,duration\nservice1,resolved,5\nservice2,resolved,10\n", encoding="utf-8")

    report = analyze_incidents(input_path, output_path)

    with open(output_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert data == report
    


    