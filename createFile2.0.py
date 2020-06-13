import simplejson as json
import os  # OS methods

# check if file exits AND if its no 0 size
if os.path.isfile("./test.json") and os.stat('./test.json').st_size != 0:
    old_file = open("./test.json", "r+")  # open file with read permission
    data = json.loads(old_file.read())  # load JSON as py obj
    print("Current Level is", data["Level"], "--Increasing the level by 1")
    data['Level'] = data["Level"] + 1
    print("New level is", data["Level"])
else:  # if file doesnt exist ,create it
    old_file = open("test.json", "w+")  # create file with write permission
    data = {"Name": "Alex", "Level": 50}
    print("File does not exist, Creating ....", data)

old_file.seek(0)
old_file.write(json.dumps(data))  # dump data frm py obj to JSON
