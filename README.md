# API псевдорулетки

## Запуск
1. Клонируйте репозиторий
2. Запустите сборку командой: 
```shell
docker-compose up -d --build
```
3. Для просмотра лога используйте:
```shell
docker-compose logs -f
```
## Технологии
* Django/DRF
* PostgreSQL
* Docker + docker-compose


## Использование
* API будет запущено по ссылке: http://0.0.0.0:8000/api/
* Используйте метод GET, чтобы просмотреть список всех раундов
и количество людей, которые в них участвовали,
а также список топ 5 пользователей и информацией о 
количестве раундов где они участвовали и среднем кол-ве
прокручиваний рулетки за раунд (при первом запуске приложения списки буду пусты)
* Используйте метод POST, чтобы прокрутить рулетку. 
В методе POST необходимо отправить  id пользователя, который
крутит рулетку, например:
{"user_id": 18}. В ответ на корректный POST запрос придет id пользователя, id раунда, 
и номер выпавшей ячейки  cell (ячейка 11 = jackpot)