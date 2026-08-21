DOCKER_USERNAME := softdevashish
IMAGE_NAME := todo
.PHONEY: build-zero

deps:
	bash scripts/build.sh

build:
	docker compose up --build --remove-orphans

build-zero: deps build

up:
	docker compose up

up-d:
	docker compose up -d

down-v:
	docker compose down -v --remove-orphans

down:
	docker compose down

docker-push:
	docker tag $(IMAGE_NAME):latest $(DOCKER_USERNAME)/$(IMAGE_NAME):$(v)
	docker tag $(IMAGE_NAME):latest $(DOCKER_USERNAME)/$(IMAGE_NAME):latest
	docker push $(DOCKER_USERNAME)/$(IMAGE_NAME):$(v)
	docker push $(DOCKER_USERNAME)/$(IMAGE_NAME):latest

git-push:
	git add . && \
	git commit -m $(msg) && \
	git push -u origin $(branch)

