import json


def filter_users_by_name(name):
    """
    Filters users loaded from users.json by matching their name (case-insensitive).

    :param name: The name to filter users by.
    :type name: str
    :return: None. Matched users are printed to the console.
    :rtype: None
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    """
    Filters users loaded from users.json by matching their age.

    :param age: The age to filter users by.
    :type age: int
    :return: None. Matched users are printed to the console.
    :rtype: None
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    """
    Filters users loaded from users.json by matching their email exactly.

    :param email: The email address to filter users by.
    :type email: str
    :return: None. Matched users are printed to the console.
    :rtype: None
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"] == email]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input(
        "What would you like to filter by? (Currently, only 'name', 'age' and 'email' "
        "is supported): "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: "))
        filter_users_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter a email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")