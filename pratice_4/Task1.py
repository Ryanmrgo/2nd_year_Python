    

def parameter_types(param1, param2, *var_args, **var_kwargs):
    '''    Print different types of parameters.

    Parameters:
    - param1: First positional parameter
    - param2: Second positional parameter
    - var_args: Var-positional parameters
    - var_kwarg1 (str): First var-keyword parameter (default is "default1")
    - var_kwarg2 (str): Second var-keyword parameter (default is "default2")
    - var_keyword: Additional var-keyword parameters

    Returns:
    None'''
    print(f"Positional Parameter 1 ({type(param1)}): {param1}")
    print(f"Positional Parameter 2 ({type(param2)}): {param2}")

    print("\nVar-Positional Parameters:")
    for i, var_arg in enumerate(var_args, start=1):
        print(f"Var-Positional Parameter {i} ({type(var_arg)}): {var_arg}")

    print("\nVar-Keyword Parameters:")
    for key, value in var_kwargs.items():
        print(f"Var-Keyword Parameter '{key}' ({type(value)}): {value}")


parameter_types(10, "Hello", True, [1, 2, 3], name="John", age=25, is_student=True)
print("\n---------------------------------------------------------------------------\n")
parameter_types("apple", 3.14, (1, 2, 3), color="red", size="medium", is_fruit=True)
