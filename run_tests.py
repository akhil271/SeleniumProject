import pytest

if __name__ == "__main__":
    pytest.main(["tests","-v","--html=reports/report.html","--self-contained-html","-n","2"])
