# Вывод списка всех запущенных контейнеров с именами, статусом и перенаправленными портами
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"