.PHONEY: build-zero

deps:
	bash scripts/build.sh

build:
	docker compose up --build

build-zero: deps build