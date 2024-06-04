def display_menu():
    print("\nChoose a list operation:")
    print("1. Append")
    print("2. Extend")
    print("3. Insert")
    print("4. Remove")
    print("5. Pop")
    print("6. Clear")
    print("7. Index")
    print("8. Count")
    print("9. Sort")
    print("10. Reverse")
    print("11. Copy")
    print("12. Exit")


lst = ["Test1", "Test2", 3]  # Temporary for testing


def handle_append(lst):
    try:
        user_input = input("Enter a value to append: ")
        if not user_input:  # Checks if the input is empty
            raise ValueError("Empty input, please try again.")
    except ValueError as e:
        print(e)
        return
    lst.append(user_input)
    print(lst)


def handle_extend(lst):
    try:
        user_input = input("Enter values to extend, comma separated: ").strip()
        if not user_input:
            raise ValueError("Empty input, please try again.")
        values = [
            value.strip() for value in user_input.split(",")
        ]  # Removes the whitespaces to check if the input is empty
        if not any(values):
            raise ValueError("Empty input, please try again.")
    except ValueError as e:
        print(e)
        return
    lst.extend(values)
    print(lst)


def handle_insert(lst):
    try:
        user_index = input("Please choose your index: ")
        if not user_index.isdigit():  # check if user_index is a digit
            raise ValueError("Index must be an integer, please try again.")
        user_index = int(user_index)  # Convert user_index to integer
        if user_index < 0 or user_index > len(lst):
            raise IndexError("Index doesn't exist, please try again.")
        user_input = input("Enter a string to insert: ")
        if not user_input:
            raise ValueError("Empty input, please try again.")
    except (ValueError, IndexError) as e:
        print(e)
        return
    lst.insert(user_index, user_input)
    print(lst)


def handle_remove(lst):
    try:
        user_input = input("Enter a value to be removed: ")
        if user_input not in lst:
            raise ValueError("Value not found in the list, please try again.")
    except ValueError as e:
        print(e)
        return
    lst.remove(user_input)
    print(lst)


def handle_pop(lst):
    try:
        user_input = input("Choose index to pop (leave empty to pop the last item): ")
        if user_input == "":
            user_index = -1  # Default to pop the last item if empty
        else:
            user_index = int(user_input)
            if user_index < 0 or user_index >= len(lst):
                raise IndexError("Index doesn't exist, please try again.")
    except ValueError:
        print("Index must be an integer, please try again.")
        return
    except IndexError as e:
        print(e)
        return
    lst.pop(user_index)
    print(lst)


def handle_clear(lst):
    lst.clear()
    print(lst)


def handle_index(lst):
    try:
        user_input = input()
        if user_input not in lst:
            raise ValueError("Value not found, please try again")
    except ValueError as e:
        print(e)
        return
    lst.index(user_input)
    print(lst)


def handle_count(lst):
    # TODO: Prompt the user for a value to count its occurrences in the list
    # Use the count() method to count how many times the value appears in the list
    # Print the count of the value
    pass


def handle_sort(lst):
    # TODO: Use the sort() method to sort the list in ascending order
    # Print the updated list
    pass


def handle_reverse(lst):
    # TODO: Use the reverse() method to reverse the order of the list
    # Print the updated list
    pass


def handle_copy(lst):
    # TODO: Use the copy() method to create a shallow copy of the list
    # Print the copied list
    pass


def main():
    # initial_values = input("Enter initial list values (comma-separated): ")
    # lst = initial_values.split(",")

    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ")
        if choice == "1":
            handle_append(lst)
        elif choice == "2":
            handle_extend(lst)
        elif choice == "3":
            handle_insert(lst)
        elif choice == "4":
            handle_remove(lst)
        elif choice == "5":
            handle_pop(lst)
        elif choice == "6":
            handle_clear(lst)
        elif choice == "7":
            handle_index(lst)
        elif choice == "8":
            handle_count(lst)
        elif choice == "9":
            handle_sort(lst)
        elif choice == "10":
            handle_reverse(lst)
        elif choice == "11":
            handle_copy(lst)
        elif choice == "12":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
