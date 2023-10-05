import json

with open('sample.json', 'r') as json_file:

    json_data = json.load(json_file)
    print(json_data)
    print(json.dumps(json_data, indent=4))

    courses = []

    for Course in json_data["certifications"]:
        courses.append(Course['courses'])

    print(json.dumps(courses, indent=2))
