.PHONY: clean install test

install:
	. proj/bin/activate; pip install -Ur requirements.txt

clean:
	rm -r proj/
	rm -r dist/

test:
	. proj/bin/activate; python3 -m pytest -vr /tests

assemble:
	python3 setup.py sdist bdist_wheel

publish:
	python3 -m twine upload dist/*
	$(VENV_ACTIVATE)