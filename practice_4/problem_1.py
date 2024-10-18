# Function definition
def parameter_types(positional1, positional2, *var_positional, kwarg1="default1", kwarg2="default2", **var_keyword):
    """
    Print different types of parameters.

    Parameters:
    - positional1: First positional parameter
    - positional2: Second positional parameter
    - var_positional: Var-positional parameters
    - kwarg1 (str): First var-keyword parameter (default is "default1")
    - kwarg2 (str): Second var-keyword parameter (default is "default2")
    - var_keyword: Additional var-keyword parameters

    Returns:
    None
    """
    print(f"Positional Parameter 1: {positional1}, Type: {type(positional1)}")
    print(f"Positional Parameter 2: {positional2}, Type: {type(positional2)}")

    print("\nVar-Positional Parameters:")
    for i, arg in enumerate(var_positional, 1):
        print(f"Var-Positional Parameter {i}: {arg}, Type: {type(arg)}")

    print(f"\nVar-Keyword Parameter 1: {kwarg1}, Type: {type(kwarg1)}")
    print(f"Var-Keyword Parameter 2: {kwarg2}, Type: {type(kwarg2)}")

    print("\nAdditional Var-Keyword Parameters:")
    for key, value in var_keyword.items():
        print(f"{key}: {value}, Type: {type(value)}")

parameter_types(10, "Hello", 3.14, [1, 2, 3], "Extra", kwarg2="Custom", color="Blue", size=42)
parameter_types("abc", 123, kwarg1="Overridden", extra_param="Additional", flag=True)
