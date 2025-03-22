# Загрузка образа nginx:latest из Docker Hub
docker pull nginx:latest

# Запуск контейнера с переадресацией порта 80 контейнера на порт 8080 локальной машины
docker run --name my_nginx -d -p 8080:80 nginx:latest