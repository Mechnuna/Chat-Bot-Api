all:	up

up:
		@docker-compose -f docker-compose.yml up -d

# Команда docker-compose down остановит ваши контейнеры, но также удалит остановленные контейнеры,
# а также все созданные сети
down:
		@docker-compose -f docker-compose.yml down

# Список контейнеров
ps:
		@docker-compose -f docker-compose.yml ps

# Создавайте или перестраивайте сервисы
re:
		@docker-compose -f docker-compose.yml down
		@docker-compose -f docker-compose.yml build
		docker-compose -f docker-compose.yml up -d

.PHONY:	all up down ps fclean re