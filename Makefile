install:
	brew install hugo

install_themes:
	git submodule update --init --recursive

compile:
	python3 compile.py

serve:
	hugo serve

build:
	rm -r public && hugo

deploy: build
	aws --profile rt s3 sync public s3://ryantuck.io
