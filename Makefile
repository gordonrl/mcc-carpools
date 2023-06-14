.DEFAULT_GOAL := carpools

carpools:
	python3 main.py

clean:
	rm -rf __pycache__ tuesday.csv thursday.csv sunday.csv

.PHONY: carpools clean