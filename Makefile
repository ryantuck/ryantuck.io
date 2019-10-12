serve:
	mkdocs serve

build:
	mkdocs build

deploy: build
	aws --profile rt s3 sync site s3://ryantuck.io
