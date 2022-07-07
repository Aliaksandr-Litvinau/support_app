.PHONY: celery
.SHELL := $(shell which bash)

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


postgres: ## Run postgres
	@docker run -d -p 5432:5432 \
                  -e POSTGRES_PASSWORD=support \
                  -e POSTGRES_USER=support_user \
                  -e POSTGRES_DB=support_db \
                  --name support_db \
                  --restart always \
                  postgres:13;


redis:
	@docker run --name hockey_redis \
                -p 6379:6379 \
                -d redis;



