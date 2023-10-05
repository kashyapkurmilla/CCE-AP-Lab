# json object - python dictonary string
# or use loads and
import json


def stringToJson():
    s = input("Enter key and value separated by commas : ")
    pairs = s.split(',')
    print(pairs)
    d = {}
    for i in pairs:
        key, value = i.split(':')
        d[key] = value
    print(d)
    # json_string = '{"name": "kashyap", "age": 19, "city": "hyd"}'
    # data = json.loads(json_string)
    # print("Data as Python Dictionary:", data)


def jsonToString():
    json_data = {
        "name": "kashyap",
        "age": 19,
        "city": "hyd"
    }
    json_str = json.dumps(json_data)
    print("JSON String:", json_str)


def main():
    n = int(input("1.convert json object into string \n2.Covert string to json object\n>"))
    if n == 1:
        jsonToString()
    elif n == 2:
        stringToJson()
    else:
        exit(0)


main()
