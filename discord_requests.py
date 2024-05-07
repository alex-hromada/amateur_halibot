import requests
import json

channel = '1192565748883796048'
user = '74416268211388416'

def retrieve_messages_by_user(channelid, userid):
    headers = {
        'Authorization':'NzQ0MTYyNjgyMTEzODg0MTY.G4G7tu.Fcq2VFWamsID05aUCGlJmmpCqw2C9uKyZjdiXQ'
    }
    
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers = headers)
    
    jsonn = json.loads(r.text)
    
    # for value in jsonn:
    #     print(value['author']['id'] == userid, '\n')
        
    messages = [message['content'] for message in jsonn if message['author']['id'] == userid]
    print(messages)
    

    
retrieve_messages_by_user(channel, user)