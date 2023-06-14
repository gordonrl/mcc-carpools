.ONESHELL:

setup: environment.yml
	conda env create -f environment.yml

carpools:
	python3 main.py

clean:
	rm -rf __pycache__ tuesday.csv thursday.csv sunday.csv

.PHONY: basic clean carpools