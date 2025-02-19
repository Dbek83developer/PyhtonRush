// Создание массива чисел от 1 до 10
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Инициализация переменной для хранения суммы элементов
let sum = 0;

// Перебор элементов массива с использованием цикла for...of
for (const number of numbers) {
  // Вывод каждого элемента массива в консоль
  console.log(number);

  // Добавление текущего элемента к сумме
  sum += number;
}

// Вывод суммы всех элементов массива в консоль
console.log('Сумма:', sum);