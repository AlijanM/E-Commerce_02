# https://www.tutorialspoint.com/requests/requests_file_upload.htm

import requests

# files can be uploaded in two methods
url = 'https://httpbin.org/post'


# method 1: upload a file using request and read the contents of the file uploaded using the 'files' param
filePath = "C:\\Users\\AlijanMo\\Desktop\\Selenium\\07_GuruEcommerce\\Requests_Library\\fileUpload.txt"
myFile = {"file": open(filePath, "rb")}
uploadedFile = requests.post(url, files=myFile)

# response (contains the content of the uploaded file) in text
uploadedFileT = uploadedFile.text

print("Uploaded text: %s \n" % uploadedFileT)

'''
# method 2: sending the string/text with post() method
myFile = {'file': ('test1.txt', 'Method 2: Welcome to TutorialsPoint')}
uploadedFile = requests.post(url, files=myFile)

# response (contains the uploaded text) in text
uploadedFileT = uploadedFile.text

print("Uploaded text: %s \n" % uploadedFileT)
'''


# python -s Requests_Library\09_file_upload.py