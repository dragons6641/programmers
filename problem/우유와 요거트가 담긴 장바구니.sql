-- 코드를 입력하세요
SELECT M.CART_ID
FROM (SELECT DISTINCT CART_ID
      FROM CART_PRODUCTS
      WHERE NAME = 'Milk') M, 
     (SELECT DISTINCT CART_ID
      FROM CART_PRODUCTS
      WHERE NAME = 'Yogurt') Y
WHERE M.CART_ID = Y.CART_ID
ORDER BY M.CART_ID
