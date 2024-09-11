cart1 = {
    "id": 5,
    "userId": 3,
    "date": "2020-03-01T00:00:00.000Z",
    "products": [
    {
        "productId": 7,
        "quantity": 1
    },
    {
        "productId": 8,
        "quantity": 1
    }
    ],
}

print(cart1["products"])

for product in cart1["products"]:
    print(f"Product ID: {product['productId']}")
    print(f"Product Quantity: {product['quantity']}\n")