import requests
link = requests.get("https://directory.ntschools.net/api/System/GetAllSchools")
print(link.content)

import json
parsed_data = json.loads(link.content)
parsed_data

new_link = "https://directory.ntschools.net/api/System/GetSchool?itSchoolCode="

school_codes = []
for i in parsed_data:
    school_codes.append(i["itSchoolCode"])    

nest_list = []

for i in range(50):
    school_data = requests.get(new_link + school_codes[i])
    data = json.loads(school_data.content)
    singleSch_data = []
    singleSch_data.append(data['name'])
    singleSch_data.append(data['physicalAddress']['displayAddress'])
    singleSch_data.append(data['schoolManagement'][0]['firstName'] + data['schoolManagement'][0]['lastName'])
    singleSch_data.append(data['schoolManagement'][0]['position'])
    singleSch_data.append(data['schoolManagement'][0]['email'])
    singleSch_data.append(data['telephoneNumber'])
    nest_list.append(singleSch_data)

import csv
with open("school_data.csv", "w") as file:
    file_writer = csv.writer(file, delimiter=',')
    head_list = ["Name", "Address", "Principal/Admin Name", "Principal/Admin Position", "Principal/Admin E-mail", "TelePhone"]
    file_writer.writerow(head_list)
    for i in range(len(nest_list)):
        file_writer.writerow(nest_list[i])




