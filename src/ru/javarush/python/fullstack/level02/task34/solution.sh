# Установите пароль для пользователя root как my-secret-pw и перенаправьте порт 3306 контейнера на порт 3306 хост-машины.
docker run -d -p 3306:3306 --name mysql_db -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:latest
