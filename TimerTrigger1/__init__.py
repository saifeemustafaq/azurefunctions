from dotenv import load_dotenv
load_dotenv()

import os

import datetime
import logging

import azure.functions as func

import requests

from twilio.rest import Client

account_sid = "AC5825e12c1429c24d528f5579be9bc9de"
auth_token = "27c68fe2570463de93102a1f7817fcbc"
my_twilio_number = "+12067361237"
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