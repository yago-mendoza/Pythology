##----------------------------------------------------------------------------------------------
## 3.2 The 'match' keyword
##----------------------------------------------------------------------------------------------

# The match-case structure is a newer Python feature that is useful
# for handling complex decision trees with many cases.

def calculate(operation, a, b):

    match operation:
        case "add":
            return a + b
        case "subtract":
            return a - b
        case "multiply":
            return a * b
        case "divide":
            # Guard against division by zero
            return "Error: Division by zero" if b == 0 else a / b
        case _:
            # Fallback for unknown operations
            return "Unknown operation"

# However, for simple cases with a limited set of possible operations,
# a dictionary-based approach is typically more concise and just as readable.

def calculate(op, a, b):
    # This is often cooler in regular Python usage due to its simplicity.
    operations = {
        "add": lambda: a + b,
        "subtract": lambda: a - b,
        "multiply": lambda: a * b,
        "divide": lambda: "Error: Division by zero" if b == 0 else a / b
    }
    # Execute the function corresponding to the provided operation, or return
    # a default value if the operation is unknown.
    return operations.get(op, lambda: "Unknown operation")()