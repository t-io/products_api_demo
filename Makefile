build:
	docker-compose build

run:
	docker-compose up -d

init: build run
	docker-compose exec api flask db init
	docker-compose exec api flask db migrate && flask db upgrade
	@echo "Init done, containers running"

serve init:
	docker-compose run api flask run

test:
	docker-compose run api py.test
