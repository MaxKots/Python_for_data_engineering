--Создание табличек

CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20),
    registration_date TIMESTAMP,
    loyalty_status VARCHAR(20)
);

CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    category_id INT,
    price DECIMAL(10,2),
    stock_quantity INT,
    creation_date TIMESTAMP
);

CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES Users(user_id),
    order_date TIMESTAMP,
    total_amount DECIMAL(10,2),
    status VARCHAR(20),
    delivery_date TIMESTAMP
);

CREATE TABLE OrderDetails (
    order_detail_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES Orders(order_id),
    product_id INT REFERENCES Products(product_id),
    quantity INT,
    price_per_unit DECIMAL(10,2),
    total_price DECIMAL(10,2)
);

CREATE TABLE ProductCategories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    parent_category_id INT
);

-- Заполнение таблицы Users
INSERT INTO Users (first_name, last_name, email, phone, registration_date, loyalty_status)
VALUES 
('Иван', 'Иванов', 'ivan.ivanov@example.com', '+79001234567', CURRENT_TIMESTAMP, 'Золотой'),
('Мария', 'Петрова', 'maria.petrovna@example.com', '+79007654321', CURRENT_TIMESTAMP, 'Серебряный'),
('Алексей', 'Сидоров', 'alexey.sidorov@example.com', '+79003456789', CURRENT_TIMESTAMP, 'Обычный'),
('Анна', 'Кузнецова', 'anna.kuznetsova@example.com', '+79005678912', CURRENT_TIMESTAMP, 'Золотой'),
('Дмитрий', 'Попов', 'dmitry.popov@example.com', '+79009876543', CURRENT_TIMESTAMP, 'Серебряный'),
('Елена', 'Морозова', 'elena.morozova@example.com', '+79007654321', CURRENT_TIMESTAMP, 'Обычный'),
('Сергей', 'Семенов', 'sergey.semenov@example.com', '+79004567890', CURRENT_TIMESTAMP, 'Золотой'),
('Ольга', 'Федорова', 'olga.fedorova@example.com', '+79005432167', CURRENT_TIMESTAMP, 'Серебряный'),
('Игорь', 'Григорьев', 'igor.grigoryev@example.com', '+79006789012', CURRENT_TIMESTAMP, 'Обычный'),
('Татьяна', 'Лебедева', 'tatiana.lebedeva@example.com', '+79007890123', CURRENT_TIMESTAMP, 'Золотой');

-- Заполнение таблицы ProductCategories
INSERT INTO ProductCategories (name, parent_category_id)
VALUES 
('Электроника', NULL),
('Одежда', NULL),
('Дом и сад', NULL),
('Книги', NULL),
('Спорт', NULL),
('Авто', NULL),
('Красота', NULL),
('Игрушки', NULL),
('Продукты', NULL),
('Мебель', NULL);

-- Заполнение таблицы Products
INSERT INTO Products (name, description, category_id, price, stock_quantity)
VALUES 
('Смартфон', 'Современный смартфон с отличными характеристиками.', 1, 29999.99, 50),
('Ноутбук', 'Мощный ноутбук для работы и игр.', 1, 59999.99, 30),
('Футболка', 'Удобная хлопковая футболка.', 2, 999.99, 100),
('Джинсы', 'Классические джинсы синего цвета.', 2, 2499.99, 50),
('Гардина', 'Легкая гардина для окон.', 3, 1499.99, 20),
('Книга по программированию', 'Изучите программирование с нуля.', 4, 1999.99, 15),
('Теннисный мяч', 'Мяч для игры в теннис.', 5, 499.99, 200),
('Автомобильные шины', 'Новые шины для вашего автомобиля.', 6, 12000.00, 10),
('Крем для лица', 'Увлажняющий крем для лица.', 7, 899.99, 40),
('Конструктор LEGO', 'Конструктор для создания различных моделей.', 8, 4999.99, 25);

-- Заполнение таблицы Orders
INSERT INTO Orders (user_id, order_date, total_amount, status, delivery_date)
VALUES 
(1, CURRENT_TIMESTAMP, 29999.99, 'Доставлено', CURRENT_TIMESTAMP + INTERVAL '3 days'),
(2, CURRENT_TIMESTAMP, 2499.99, 'В процессе', CURRENT_TIMESTAMP + INTERVAL '5 days'),
(3, CURRENT_TIMESTAMP, 1999.99, 'Доставлено', CURRENT_TIMESTAMP + INTERVAL '2 days'),
(4, CURRENT_TIMESTAMP, 59999.99, 'Отменено', NULL),
(5, CURRENT_TIMESTAMP, 499.99, 'Доставлено', CURRENT_TIMESTAMP + INTERVAL '1 day'),
(6, CURRENT_TIMESTAMP, 899.99, 'В процессе', CURRENT_TIMESTAMP + INTERVAL '4 days'),
(7, CURRENT_TIMESTAMP, 12000.00, 'Доставлено', CURRENT_TIMESTAMP + INTERVAL '3 days'),
(8, CURRENT_TIMESTAMP, 4999.99, 'Доставлено', CURRENT_TIMESTAMP + INTERVAL '2 days'),
(9, CURRENT_TIMESTAMP, 29999.99, 'Отменено', NULL),
(10, CURRENT_TIMESTAMP, 1499.99, 'В процессе', CURRENT_TIMESTAMP + INTERVAL '5 days');

-- Заполнение таблицы OrderDetails
INSERT INTO OrderDetails (order_id, product_id, quantity, price_per_unit, total_price)
VALUES 
(1, 1, 1, 29999.99, 29999.99),
(2, 4, 1, 2499.99, 2499.99),
(3, 5, 1, 1999.99, 1999.99),
(4, 2, 1, 59999.99, 59999.99),
(5, 8, 1, 499.99, 499.99),
(6, 7, 1, 899.99, 899.99),
(7, 6, 1, 12000.00, 12000.00),
(8, 9, 1, 4999.99, 4999.99),
(9, 3, 1, 29999.99, 29999.99),
(10, 10, 1, 1499.99, 1499.99);
