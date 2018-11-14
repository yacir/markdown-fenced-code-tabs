.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

clean-pyc: ## Remove python artifacts.
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	find . -name "*.pyo" -print0 | xargs -0 rm -rf

clean-build: ## Remove build artifacts.
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

clean: clean-pyc clean-build ## Remove both build and python artifacts.

build-docs: ## Build the docs.
	cd docs && mkdocs build

run-docs: ## Build the docs.
	cd docs && mkdocs serve

publish-package: ## Publish the package on PyPi
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*

publish-docs: ## Publish the docs on gh-pages
	cd docs && mkdocs gh-deploy