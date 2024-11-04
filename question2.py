def unique(cus_ids):
    unique_list = set(cus_ids)
    print(f"The unique customer ids are: {unique_list}")

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
unique(customer_ids)