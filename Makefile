help:
	@echo ""
	@echo "Usage:"
	@echo "	make <command>"
	@echo ""
	@echo "Commands:"
	@echo "	compile					Compile all python files into executables."

compile:
	python3 -m compileall .