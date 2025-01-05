def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # Or handle it appropriately

result = function(10, 0)
print(result)