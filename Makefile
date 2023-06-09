carpools:
	python3 main.py

clean:
	rm -rf __pycache__ tuesday.csv thursday.csv sunday.csv

setup: requirements.txt
	python3 -m pip install -r requirements.txt