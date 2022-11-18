import os
import requests
from dotenv import load_dotenv
import time

from .models import Mailing, Client, Message

load_dotenv()

URL = os.getenv("URL")
TOKEN = os.getenv("TOKEN")


def send_message(ids, url=URL, token=TOKEN):
    header = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'}

    mailing = Mailing.objects.filter(id=ids).first()
    clients = Client.objects.filter(code=mailing.mobile_codes).all()

    for client in clients:
        messages = Message.objects.filter(
            client_id=client.id
        ).select_related(
            'client', 'mailing'
        ).all()

        for message in messages:
            data = {
                'id': message.id,
                "phone": client.phone,
                "text": mailing.text
            }
            
            count = 0
            
            try:
                response = requests.post(
                    url=url + str(message.id),
                    headers=header,
                    json=data)
                
                print(response.status_code)
                
                while response.status_code != 200 and count < 200:
                    time.sleep(2)
                    count += 1
                    
            except ConnectionError:
                return f'Connection error, contact your network administrator'