mocked_all_pizzas = [
    {
        "_id": {"$oid": "622c7b8c0c6f5f197f7c4140"},
        "name": "TEST_PIZZA_NAME",
        "toppings": ["TOMATO SAUCE", "CHEESE", "OREGANO"],
        "average_rate": 4.5,
        "rate": {"1": 5, "2": 4},
    },
    {
        "_id": {"$oid": "622c7c870c6f5f197f7c4142"},
        "name": "TEST_PIZZA_NAME_2",
        "toppings": ["TOMATO SAUCE", "CHEESE", "TOMATO"],
        "average_rate": 0,
        "rate": {},
    },
]

mocked_one_pizza = {
        "_id": {"$oid": "123456"},
        "name": "PIZZA_NAME",
        "toppings": ["TOMATO SAUCE", "CHEESE", "OREGANO"],
        "average_rate": 0,
        "rate": {},
    }

expected_all_pizzas = {
    "pizzas": [
        {
            "_id": {"$oid": "622c7b8c0c6f5f197f7c4140"},
            "name": "TEST_PIZZA_NAME",
            "toppings": ["TOMATO SAUCE", "CHEESE", "OREGANO"],
            "average_rate": 4.5,
            "rate": {"1": 5, "2": 4},
        },
        {
            "_id": {"$oid": "622c7c870c6f5f197f7c4142"},
            "name": "TEST_PIZZA_NAME_2",
            "toppings": ["TOMATO SAUCE", "CHEESE", "TOMATO"],
            "average_rate": 0,
            "rate": {},
        },
    ]
}

expected_one_pizza = {
    "pizza":
        {
            "_id": {"$oid": "123456"},
            "name": "PIZZA_NAME",
            "toppings": ["TOMATO SAUCE", "CHEESE", "OREGANO"],
            "average_rate": 0,
            "rate": {},
        }
}
