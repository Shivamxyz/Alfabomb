import requests
import json
import time

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = 'YOUR_BOT_TOKEN'
api_endpoint = f"https://api.telegram.org/bot{bot_token}/getUpdates"

def send_telegram_message(chat_id, text):
    send_message_endpoint = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {'chat_id': chat_id, 'text': text}
    requests.get(send_message_endpoint, params=params)

# Replace 'STORED_USER_ID' with the actual user ID you want to compare
stored_user_id = '6457812945'

while True:
    try:
        response = requests.get(api_endpoint)
        updates = response.json()

        # Iterate through updates in reverse order to process the last message
        for update in reversed(updates['result']):
            chat_id = update['message']['chat']['id']
            user_id = update['message']['from']['id']
            message_text = update['message']['text']

            # Check if the user ID matches the stored ID
            if user_id == stored_user_id:
                # User ID matches, proceed with further checks or actions

                # Check if the received message is a number with a minimum of 10 digits
                if message_text.isdigit() and len(message_text) == 10:
                    # If it's a valid number, send a response
                    response_message = f"You entered a valid number: {message_text}"
                else:
                    # If it's not a valid number, or has a different length, send a different response
                    response_message = "Please enter a valid number with exactly 10 digits."

                # Send the response back to the user
                send_telegram_message(chat_id, response_message)

                # Break out of the loop after processing the last message
                break
            else:
                # User ID does not match the stored ID, handle this case as needed
                response_message = "You are Not Subscribed"
                send_telegram_message(chat_id, response_message)

                # Break out of the loop after processing the last message
                break

    except Exception as e:
        # Handle exceptions, you may want to log them for debugging
        print(f"An error occurred: {e}")

    # Add a delay to avoid constant polling and rate limiting
    time.sleep(2)
