import send_to_bot
import weather_services


def lambda_handler(event, context):
    print('Event: ', event)

    message = event['message'] if event.__contains__('message') else None
    query = event['inline_query'] if event.__contains__('inline_query') else None
    callback_query = event['callback_query'] if event.__contains__('callback_query') else None

    if query is not None:
        print('Inline Query: ', query)

    elif callback_query is not None:
        print('Callaback query: ', callback_query)
    elif message is not None:
        print('Message: ', message)
        if message.__contains__('text') and message['text'] == '/start':
            send_to_bot.sent_start_keyboard(message['chat']['id'])
        elif message.__contains__('location'):
            data = weather_services.get_by_location(None, latitude=message['location']['latitude'],
                                                    longitude=message['location']['longitude'])
            send_to_bot.send_message_get(data, chat_id=message['chat']['id'])

    return {
        "statusCode": 200,
        "body": "Successful",
    }
