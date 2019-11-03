clean:
	rm -r proj/
	rm -r dist/

assemble:
	python3 setup.py sdist bdist_wheel

publish:
	python3 -m twine upload dist/*

test:
	cd tests/ && python3 -m pytest .
