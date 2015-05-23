## simple makefile - currently *nix like
default: docs tests


pep8:
	@echo "   === pep8          ==="
	autopep8 --in-place utils/*.py

checker:
	- mv utils/Leap.py utils/Leap.pold
	-pychecker -b Leap utils/*.py
	- mv utils/Leap.pold utils/Leap.py

lint:
	- mv utils/Leap.py utils/Leap.pold
	-pylint utils/*.py
	- mv utils/Leap.pold utils/Leap.py

checks: checker lint

docs:
	@echo "   === documentation ==="
	@cd utils ; pwd ; \
	for p in *.py  \
	; do \
	pydoc -w `basename $$p .py` \
	;done 
	mkdir -p documentation/html
	mv utils/*.html documentation/html


tests:
	@echo "   === tests TODO need various suites ==="

