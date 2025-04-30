import sys
import clipboard
import json

# print(cpydata)sdfasdfas
# print(sys.argv)  

saved_data = "clipboard.json"

def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_items(filepath):
    try:
        with open(filepath,"r") as f:
            data = json.load(f)
            return data
    except:
        return{}


if len(sys.argv)==2:
    command = sys.argv[1]
    data = load_items(saved_data)
    
    if command == "save":
        key = input("enter the key:")
        # ctrl_v = clipboard.paste()
        data[key]= clipboard.paste()
        save_items(saved_data, data)
        print("data saved!")    
    elif command == "load":
        key = input("enter the key")
        if key in data:
            # ctrl_c = clipboard.copy()
            clipboard.copy(data[key])
            print("data copied to clipboard")
        else:
            print("key does not exist")

    elif command == "list":
        print(data)
    else:
        print("unkown command")
else:
    print("pass exactly one command.")









