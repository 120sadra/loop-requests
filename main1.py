import requests
import time

headers = {
    "User-Agent" : "your user agent"
}
i = 1
while True :
    try:
        response =  requests.get("https://your url/" , headers=headers)
        status = response.status_code
        print(status)
        if status == 200 :
            print(f"ok number of requests = {i}")
            i+=1
        elif status == 404 :
            print("no site")
        elif status == 403:
            print("no access")
        else :
            print ("unknown eror")
            
        time.sleep(1)
    except  Exception as e:
        print (f"another code eror {e}")
        
        time.sleep(5)
