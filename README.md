# FastApi mono repo template [WIP]

## this project is a template ment to be used as a refrince or a starting point for a mono repo for a restApi backend

### Mono Repo ?

### assumptions ...

### fast start with docker

1. install docker and docker-compose
2. run `docker compose up api-${app name}`
3. run `docker exec -it [CONTAINER_ID] bash` on a separate terminal

### to create migration file run

`alembic revision -m "short message" --autogenerate`

### to run the tests

`docker compose run --rm pytest-${app name}`
