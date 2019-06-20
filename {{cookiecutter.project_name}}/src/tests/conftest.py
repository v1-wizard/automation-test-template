from src.settings import SETTINGS_TEXT


def pytest_report_header(config):
    return SETTINGS_TEXT
