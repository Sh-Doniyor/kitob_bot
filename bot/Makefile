extract:
	pybabel extract --input-dirs=. -o locales/messages.pot

init:
	pybabel init -i locales/messages.pot -d locales -D messages - l en
	pybabel init -i locales/messages.pot -d locales -D messages - l uz

update:
	pybabel update -d locales -D messages -i locales/messages.pot
compile:
	pybabel compile -d locales -D messages


mig:
	alembic revision --autogenerate -m
head:
	alembic upgrade head

downgrade:
	alembic downgrade head

upgrade:
	alembic upgrade head
