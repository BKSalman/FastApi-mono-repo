# FastApi mono repo template [WIP]

## this project is a template ment to be used as a refrince or a starting point for a mono repo for a restApi backend

### Mono Repo ?

### assumptions ...

### fast start with docker

1. install docker and docker-compose
2. run `docker compose up api-${app name}`
3. run `docker exec -it [CONTAINER_ID] bash` on a separate terminal

# remove later
users container: 9c42fb7405b6c96c6f5ad956b52cb7bc08238f07586dc55bd5c583e3ec9aa832
resorts container: 64a941e7fd75363af83a73dddae98dd3f1534f4b699317be82b57f059848e7e2


### to create migration file run

`alembic revision -m "short message" --autogenerate`

### to run the tests

`docker compose run --rm pytest-${app name}`
