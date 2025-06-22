.PHONY: test install

PYTHON_EXE = c:\python27\python.exe

test:
	$(PYTHON_EXE) -m pytest

install:
	$(PYTHON_EXE) -m pip install .
