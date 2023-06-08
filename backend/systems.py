import json
import os 
 
global log_metric
log_metric = [] 


def create_metrics(log_metric):
    data = {}
    for metric in log_metric:
        data[metric[0]] = metric[1]
    print(data)
    json_data = json.dumps(data)

    with open( "metrics.json", "w") as f:
        json.dump(data, f)

    return data


def log_metrics(topic, grading_scale):
    log_metric.append([topic, grading_scale])


def alter_metrics(topic, new_scale):
    with open("metrics.json") as f:
        data = json.load(f)
        print(data)

        data["3"] = new_scale
        json.dump(data, f)
        print("error in altering")


if __name__ == "__main__":
    for i in range(101):
        log_metrics(i, i)
    print(log_metric)
    create_metrics(log_metric)

    # alter_metrics("3", "new_scale") 
