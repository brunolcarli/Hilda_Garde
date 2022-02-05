install:
	pip3 install --no-binary :all -r hilda_garde/requirements/development.txt

run:
	python3 main.py

help:
	python3 manage.py help

pipe:
	make install
	make run
