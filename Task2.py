import requests
import json




with open(r"C:\test\new2.txt",mode= "rb" ) as file:

    f = file.read()


headers = {
"Content-Type": "application/json",
"Authorization": "OAuth y0_AgAAAABkjr10AADLWwAAAADYmR_pZCrArxp7StSZ5jX7Rjl16U7RPCQ"
}
params = {'path': "new2.txt"}
#
file_path = "https://cloud-api.yandex.net/v1/disk/resources/upload/"


upload_disk = requests.get(file_path, headers = headers, params=params)



new_link = upload_disk.json()["href"]

put_file = requests.put(new_link, data=f)
print(put_file)

