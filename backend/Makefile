# Makefile

run:
	source venv/bin/activate && uvicorn main:app --reload

install:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

test:
	pytest

clean:
	rm -rf __pycache__ .pytest_cachec