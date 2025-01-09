# Итоговый проект

Данный проект позволяет выполнять миграцию и репликацию данных между postgresql и mysql с помощью spark и брокера сообщений kafka.

---
## 1. Как запускать  

- Клонируем проект на локальную машину и переходим в директорию проекта  

- Выполняем сборку  
```
docker build -t airflow .
```

- Запускаем докер-контейнер  
```
docker compose up  
```

## 2. Описание аналитических витрин    

 **2.1 all_orders**. Все заказы с информацией о пользователях и продуктах:

| Поле | Описание | 
|-------------------|--------------------------------------| 
| order_id | Номер заказа | 
| order_date | Дата заказа | 
| delivery_date | Дата доставки | 
| total_amount | Общая сумма заказа | 
| status | Статус заказа | 
| user_id | Идентификатор пользователя | 
| full_name | Полное имя пользователя | 
| email | Почта пользователя | 
| phone | Телефон пользователя | 
| loyalty_status | Статус карты лояльности | 
| product_id | Идентификатор продукта | 
| product_name | Имя продукта | 
| category_id | Идентификатор категории | 
| category_name | Имя категории | 
| quantity | Количество продукта в заказе | 
| price_per_unit | Цена за единицу продукта | 
| total_price | Общая цена за позицию в заказе |

**SQL-код:**  
```
CREATE TABLE all_orders AS (
SELECT
    o.order_id,
    o.order_date,
    o.delivery_date,
    o.total_amount,
    o.status,
    CONCAT_WS(' ', u.first_name, u.last_name) as full_name,    
    u.email,
    u.phone,
    u.loyalty_status,
    od.product_id,
    p.name as product_name,
    c.name as category_name,
    od.quantity,
    od.price_per_unit,
    od.total_price
FROM 
    Orders o
JOIN 
    Users u ON o.user_id = u.user_id
JOIN 
    OrderDetails od ON o.order_id = od.order_id
JOIN 
    Products p ON od.product_id = p.product_id
JOIN 
    ProductCategories c ON p.category_id = c.category_id
);
```

**Результат выборки:**    
  ![Иллюстрация к проекту № 1](https://github.com/MaxKots/Python_for_data_engineering/blob/main/Final_project/screenshot/2.jpg)  
  

- **2.2 amount_by_user**. Общее количество заказов и общей суммы по каждому пользователю:

| Поле | Описание |
|-------------------|----------------------------------------------------|
| user_id | Идентификатор пользователя | 
| full_name | Полное имя пользователя | 
| total_orders | Общее количество заказов пользователя | 
| total_spent | Общая сумма, потраченная пользователем |

**SQL-код:**  
```
CREATE TABLE amount_by_user AS (
SELECT 
    u.user_id,
    CONCAT_WS(' ', u.first_name, u.last_name) as full_name,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS total_spent
FROM 
    Users u
LEFT JOIN 
    Orders o ON u.user_id = o.user_id
GROUP BY 
    u.user_id, full_name
ORDER BY 
    total_spent DESC
);
```  

**Результат выборки:**    
  ![Иллюстрация к проекту № 2](https://github.com/MaxKots/Python_for_data_engineering/blob/main/Final_project/screenshot/3.jpg)  

## 3. Airflow  

Заходим по адресу: [http://127.0.0.0:8081/](http://127.0.0.0:8081/login/)  
Логин: admin  
Пароль: admin

Описание этого блока еще в процессе


## Как воспользоваться kafka  

- Cоздаем виртуальное окружение  
```
python3 -m venv venv  
```

- Активируем созданное окружение  
```
source venv/bin/activate
```

Устанавливаем требуемые зависимости для kafka:  
```
pip install -r kafka_req.txt
```
