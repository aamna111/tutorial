def find_number_in_array(arr, target):
    for num in arr:
        if num == target:
            return True
    return False

# Example usage:
my_array = [5, 12, 3, 8, 15, 7]
target_number = 8
found = find_number_in_array(my_array, target_number)

if found:
    print(f"{target_number} was found in the array.")
else:
    print(f"{target_number} was not found in the array.")
