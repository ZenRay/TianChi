#-*-coding:utf8-*-
import json
def print_hello():
    return "Hello world"

def check_sum(file):
    with open(file, "r") as file:
        data = file.readlines()
    return sum([float(i) for i in data])

def check_top10(file):
    with open(file, "r") as file:
        data = sorted([float(i) for i in file.readlines()], reverse=True)
    
    return data[:10]

    
if __name__ == "__main__":
    try:
        file = "/tcdata/num_list.csv"
        result = {
            "Q1": print_hello(),
            "Q2": check_sum(file),
            "Q3": check_top10(file)
        }
    except:
        file = "./tcdata/num_list.csv"
        result = {
            "Q1": print_hello(),
            "Q2": check_sum(file),
            "Q3": check_top10(file)
        }

    # result = json.dumps(result)
    with open("./result.json", "w") as file:
        json.dump(result, file)