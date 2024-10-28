# Метод run()
import asyncio

# Напишите асинхронную программу, которая выводит на экран "Начало", затем делает паузу на 3 секунды,
# выводит "В процессе", снова делает паузу на 2 секунды и выводит "Конец".
# Используйте метод asyncio.run() для запуска основной корутины.


async def msg():
    print("Начало")
    await asyncio.sleep(3)
    print("В процессе")
    await asyncio.sleep(2)
    print("Конец")

asyncio.run(msg())
