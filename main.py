import requests

bot_token = '6463933281:AAGszgq83HSCSmWfCm3kWKatoFqYYpuhVHA'
api_endpoint = f'https://api.telegram.org/bot{bot_token}/getUpdates'
response = requests.get(api_endpoint)
updates = response.json()

# Replace 'STORED_USER_ID' with the actual user ID you want to compare
stored_user_id = '6457812945'

# Iterate through updates in reverse order to process the last message
for update in reversed(updates['result']):
    chat_id = update['message']['chat']['id']
    user_id = update['message']['from']['id']
    message_text = update['message']['text']

    # Check if the user ID matches the stored ID
    if user_id == int(stored_user_id):
        # User ID matches, proceed with further checks or actions

        # Check if the received message is a number with a minimum of 10 digits and a maximum of 10 digits
        if message_text.isdigit() and len(message_text) == 10:
            # If it's a valid number, send a response
            response_message = f'You entered a valid number: {message_text}'
        else:
            # If it's not a valid number, or has less than 10 digits, send a different response
            response_message = 'Please enter a valid number with a minimum of 10 digits.'

        # Send the response back to the user
        send_message_endpoint = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={response_message}'
        requests.get(send_message_endpoint)

        # Break out of the loop after processing the last message
        break
    else:
        # User ID does not match the stored ID, you can handle this case as needed
        response_message = 'You are Not Subscribed'
        send_message_endpoint = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={response_message}'
        requests.get(send_message_endpoint)

        # Break out of the loop after processing the last message
        break
