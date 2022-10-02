import sys
import pyperclip
import json

SAVED_DATA = "clipboard.json"


# this function creates the file if it doesn't exist or overwrites the file
# then dumps all the data into the new file.
def save_items(filepath, data):
    print(data)
    with open(filepath, "w") as f:
        json.dump(data, f)


# open the file and return all data as a dictionary
def load_json(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        # return empty dict
        return {}


def main():

    # check if the command line argument has filename, arg
    if len(sys.argv) == 2:
        # save the command
        command = sys.argv[1]
        data = load_json(SAVED_DATA)

        if command == "save":
            new_key = input("Enter a key: ")
            data[new_key] = pyperclip.paste()
            save_items(SAVED_DATA, data)
            print("Clipboard data saved")
        elif command == "load":
            key = input("Enter a key: ")
            if key in data:
                pyperclip.copy(data[key])
                print("Data loaded!")
            else:
                print("Invalid key, please try again")
        elif command == "list":
            # print the whole dictionary
            print("{key : saved clipboard}")
            print(data)
        elif command == "help" or command == "h":
            # print help block
            print("List of commands: ")
            print("save: saves the current clipboard value")
            print("load: loading asks for a key then copies to clipboard")
            print("list: listing out every saved key and clipboard")
            print("Please run again.")
        else:
            print("Unknown Command")
    else:
        print("Please enter a single command, type h or help for a list of commands.")


if __name__ == '__main__':
    main()
