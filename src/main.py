#src => https://stackoverflow.com/questions/11914472/how-to-use-stringio-in-python3

import pycurl
import json
import io

curl = pycurl.Curl()
curl.setopt(pycurl.URL, 'http://212.227.148.73:8080/api/internal/login')
curl.setopt(pycurl.HTTPHEADER, ['Accept: application/json',
                                'Content-Type: application/json'])
curl.setopt(pycurl.POST, 1)

# If you want to set a total timeout, say, 3 seconds
curl.setopt(pycurl.TIMEOUT_MS, 3000)

## depending on whether you want to print details on stdout, uncomment either
# curl.setopt(pycurl.VERBOSE, 1) # to print entire request flow
## or
# curl.setopt(pycurl.WRITEFUNCTION, lambda x: None) # to keep stdout clean

# preparing body the way pycurl.READDATA wants it
# NOTE: you may reuse curl object setup at this point
#  if sending POST repeatedly to the url. It will reuse
#  the connection.
body_as_dict = {"email": "admin", "password": "admin"}
body_as_json_string = json.dumps(body_as_dict) # dict to json
body_as_file_object = io.StringIO(body_as_json_string)

# prepare and send. See also: pycurl.READFUNCTION to pass function instead
curl.setopt(pycurl.READDATA, body_as_file_object) 
curl.setopt(pycurl.POSTFIELDSIZE, len(body_as_json_string))
curl.perform()

# you may want to check HTTP response code, e.g.
status_code = curl.getinfo(pycurl.RESPONSE_CODE)
if status_code != 200:
    print("Aww Snap :( Server returned HTTP status code {}".format(status_code))

# don't forget to release connection when finished
curl.close()
