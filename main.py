from utils import get_data, get_filtered_data, get_last_data, get_formatted_data


def main():
    FILENAME = 'operations.json'
    COUNT_LAST_VALUES = 5
    FILTERED_EMPTY_FROM = True

    data, info = get_data(FILENAME)
    if not data:
        exit(info)
    print(info, end="\n\n")

    data = get_filtered_data(data, FILTERED_EMPTY_FROM)
    data = get_last_data(data, COUNT_LAST_VALUES)
    data = get_formatted_data(data)
    for row in data:
        print(row)


if __name__ == "__main__":
    main()