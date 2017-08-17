import caliper
import json
import requests
import datetime

the_config = caliper.HttpOptions(
      host='http://localhost:9966/api/caliper',
      auth_scheme='Yungon',
      api_key='05d0a15d-76c3-4a87-b45e-661af9a76425')

the_sensor = caliper.build_sensor_from_config(
        sensor_id='http://learning-app.your-school.edu/sensor',
        config_options=the_config)

# Here, you will have caliper entity representations of the various
# learning objects and entities in your wider system, and you provide
# them into the constructor for the event that has just happened.
#
# Note that you don't have to pass an action into the constructor because
# the NavigationEvent only supports one action, part of the
# Caliper base profile: caliper.profiles.CaliperProfile.Actions['NAVIGATED_TO']
#
the_event = """{"@context":"http://purl.imsglobal.org/ctx/caliper/v1/Context","@type":"http://purl.imsglobal.org/caliper/v1/AssessmentItemEvent","action":"http://purl.imsglobal.org/vocab/caliper/v1/action#Started","actor":{"@context":"http://purl.imsglobal.org/ctx/caliper/v1/Context","@id":"https://umich.edu/user/0fa0be48fb4b5abe568829b52a3d986663870176","@type":"http://purl.imsglobal.org/caliper/v1/lis/Person","name":"0fa0be48fb4b5abe568829b52a3d986663870176"},"edApp":{"@context":"http://purl.imsglobal.org/ctx/caliper/v1/Context","@id":"https://problem_roulette.umich.edu/","@type":"http://purl.imsglobal.org/caliper/v1/SoftwareApplication"},"eventTime":"2017-04-20T16:35:26.289Z","group":{"@context":"http://purl.imsglobal.org/ctx/caliper/v1/Context","@id":"https://umich.edu/courses/9","@type":"http://purl.imsglobal.org/caliper/v1/lis/CourseOffering","name":"PolSci 250"},"object":{"@context":"http://purl.imsglobal.org/ctx/caliper/v1/Context","@id":"https://umich.edu/d/1yUBvOeIVhS6tCuQBmCwNkj5lU_ExvOx9ZoscJVHGf1A/pub","@type":"http://purl.imsglobal.org/caliper/v1/AssessmentItem","isPartOf":{"@context":"http://purl.imsglobal.org/ctx/caliper/v1/Context","@id":"https://umich.edu/courses/9/topics/46","@type":"http://purl.imsglobal.org/caliper/v1/Assessment","name":"11. Regression"},"name":"PolSci 250 Final Exam W13 Problem 4F"}}"""

event_json = json.loads(the_event)

envelope = {
    "sensor": "KERIS-test",
    "sendTime": datetime.datetime.now().isoformat(),
    "data": [event_json]
}

headers = {
    "Authorization": "05d0a15d-76c3-4a87-b45e-661af9a76425",
    "Content-Type": "application/json"
}

# Once built, you use your sensor to send your event
r = requests.post('http://localhost:9966/key/caliper', headers=headers, data=json.dumps(envelope))

print("Status Code: " + str(r.status_code))
