import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load():
    assert REPORT.exists()
    return json.loads(REPORT.read_text())


def test_report_exists():
    """Success Criterion 1"""
    assert REPORT.exists()


def test_valid_json():
    """Success Criterion 2"""
    load()


def test_total_requests():
    """Success Criterion 3"""
    assert load()["total_requests"] == 6


def test_unique_ips():
    """Success Criterion 4"""
    assert load()["unique_ips"] == 3


def test_top_path():
    """Success Criterion 5"""
    assert load()["top_path"] == "/index.html"
