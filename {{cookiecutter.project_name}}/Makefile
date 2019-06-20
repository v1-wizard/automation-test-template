.PHONY: help venv test report

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  clean       => to clean clean all automatically generated files"
	@echo "  venv        => to create a virtualenv"
	@echo "  test        => to run pytest"
	@echo "  report      => to generate static html with test results"
	@echo "  all         => venv test report"

all: venv test report

clean:
	@find . -name \*.pyc -delete
	@find . -name \*__pycache__ -delete
	@find . -name \.pytest_cache -exec rm -r {} +
	@rm -rf allure_results || true
	@rm -rf allure_report || true
	@rm -f junit.xml || true
	@rm -rf ./dist || true
	@rm -rf ./{{cookiecutter.project_name}}.egg-info || true

venv:
	@python3 -m venv venv
	@venv/bin/pip install -U -r requirements.txt

test:
	@PYTHONPATH=/$(shell pwd) venv/bin/python3 -m pytest src/tests --alluredir=./allure_results --junitxml=junit.xml || true

report:
	@cp -r ./allure_report/history ./allure_results/ || true
	@allure generate ./allure_results -o ./allure_report --clean
