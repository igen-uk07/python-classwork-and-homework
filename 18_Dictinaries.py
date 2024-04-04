# in dictionary we can store a bunch of key values points
#each key should be unique
customer = {
    "name":"john",
    "age": 30,
    "is_verifies": True
}
customer["birthday"] = "jan 1 1999"
print(customer["birthday"])
print(customer.get("bday", "2004"))