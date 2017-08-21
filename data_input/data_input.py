import json
import requests
import datetime


def post_data(line):
    event_json = json.loads(line)

    envelope = {
        "sensor": "KERIS-test",
        "sendTime": datetime.datetime.now().isoformat(),
        "data": [event_json]
    }

    headers = {
        "Authorization": "05d0a15d-76c3-4a87-b45e-661af9a76425",
        "Content-Type": "application/json"
    }

    r = requests.post('http://localhost:9966/key/caliper', headers=headers, data=json.dumps(envelope))

    return r.status_code

if __name__ == "__main__":

    succeed = 0
    failed = 0

    with open("/home/yungon/workspace/umich_caliper_events_deperson_99k.jsonl") as f:
        for line in f:
            status_code = post_data(line)

            if status_code != 200:
                print("Failed to POST Caliper Event (" + str(status_code) + ")")
                failed = failed + 1
            else:
                succeed = succeed + 1

    print("------ RESULT ------")
    print("Succeed : " + str(succeed))
    print("Failed : " + str(failed))
