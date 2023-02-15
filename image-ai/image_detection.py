# Use openvisionapi to classify and get bounding box

import json
import os
import requests as req
import requests_toolbelt as rt


def detect(file_data):
    # Write to file
    tmp_filename = "TEMP_IMG.jpg"
    with open(tmp_filename, 'wb') as f:
        f.write(file_data)

    # Run curl
    os.system("curl -X POST -F model=yolov4 -F image=@TEMP_IMG.jpg http://170.64.128.182:8000/api/v1/detection > result.txt")

    # Read result
    with open("result.txt", "r") as f:
        result = json.loads(f.read())

    os.remove("result.txt")
    os.remove(tmp_filename)

    return result
