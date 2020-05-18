from dotenv import load_dotenv
load_dotenv()

import os

import datetime
import logging

import azure.functions as func

import requests

from twilio.rest import Client

account_sid = "YOUR SID"
auth_token = "YOUR AUTH TOKEN"
my_twilio_number = "YOUR TWILIO NUMBER"
receiver_number = "+918888076752"


def main(mytimer: func.TimerRequest) -> None:
    response = requests.get('https://api.covid19api.com/summary')
    response_json = response.json()

    total_confirmed = response_json['Countries'][76]['TotalConfirmed']
    total_deaths = response_json['Countries'][76]['TotalDeaths']

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=f'As of today, there are {total_confirmed} cases and {total_deaths} deaths in India',
            from_=my_twilio_number,
            to=receiver_number
            )

    print(message.sid)
