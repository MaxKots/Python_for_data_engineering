DROP TABLE IF EXISTS all_orders;


CREATE TABLE all_orders AS
SELECT 
    o.order_id,
    o.order_date,
    o.delivery_date,
    o.total_amount,
    o.status,
    u.full_name,
    u.email,
    u.phone,
    u.loyalty_status,
    od.product_id,
    p.product_name,
    c.category_name,
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
    ProductCategories c ON p.category_id = c.category_id;


DROP TABLE IF EXISTS amount_by_user;

CREATE TABLE amount_by_user AS
SELECT 
    u.user_id,
    u.full_name,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS total_spent
FROM 
    Users u
LEFT JOIN 
    Orders o ON u.user_id = o.user_id
GROUP BY 
    u.user_id, u.full_name
ORDER BY 
    total_spent DESC;


