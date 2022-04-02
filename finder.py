import csv


def binary_search(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if int(arr[mid][0]) == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif int(arr[mid][0]) > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


def finder(credential):
    with open("users.csv", "r") as impf:
        reader = list(csv.reader(impf))[1:]
        index = binary_search(reader, 0, len(reader) - 1, credential)
        if index != -1:
            return reader[index][1], reader[index][2]
            

print(finder(107551))
