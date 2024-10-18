def display_info(**kwargs):
    """
    Display information about a person.
    """
    print("Personal Information:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print("")

# Example usage:
display_info(name='Kit Kit', age=30, city='Mandalay', occupation='Software Engineer')
#display_info(name='Thida', age=25, city='Yangon')
#display_info(name='Mi Mi', occupation='Teacher')
