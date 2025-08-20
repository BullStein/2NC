import json
import os

new_data = {
    "data": {
        "user": {
            "theme" : "light",
            "terms" : "not accepted"
        },
        "window": {
            "window_height": 900,
            "window_width": 1800
        },
        "server history":{
            
        },

        "names history" : {

        }
    }
}
path = "config/data/data.json"


            
def create_new_data():
    with open(path, "w", encoding="utf-8") as f:
        json.dump(new_data, f, indent=4)
    return new_data

def check_data_existance():
    if not os.path.exists(path):
        return False
    else:
        return True

def modify_data(data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def read_data():
    if check_data_existance():
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = create_new_data()
    return data

if __name__ == "__main__":
    pass
    # data = new_data
    # read_data()
    # modify_data(data)
    # create_new_data()