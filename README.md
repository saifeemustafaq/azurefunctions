# azurefunctions_covid19

- Built an automated system using Azure Functions and Twilio. 
- Time interval, country, Sender and Receiver number needs to be specified and the user will receive a given country’s status such as 
  - New Confirmed 
  - Total Confirmed 
  - New Deaths
  - Total Deaths
  - New Recovered
  - Total Recovered  

on the given phone number via SMS (Microsoft Azure Functions, Twilio, Python, JSON, VSCode)

---
---
---

> ### Detailed Explanation

I will explain the working of the project here.

Tools and Tech needed:

- [Microsoft Azure](https://azure.microsoft.com/en-in/)  

- [VSCode](https://code.visualstudio.com/)

- [Twilio](https://www.twilio.com/)

- [Covid-19 Database JSON](https://api.covid19api.com/summary)

So first, there's a *Python* code.

The code needs a few parameters from the user:
- [x] Time Interval
- [x] Twilio Account ID
- [x] Twilio Account Auth Passkey
- [x] Sender Number
- [x] Receiver Number

After these details, the user can request these parameters from [Covid-19 Database JSON](https://api.covid19api.com/summary):

  -  New Confirmed
  -  Total Confirmed
  -  New Deaths
  -  Total Deaths
  -  New Recovered
  -  Total Recovered

An SMS on phone will be received on given Time Interval with the specified parameters about the latest data in the Covid-19 database of that country.

Example of an SMS:

> As of today there are xxx New Confirmed cases, xxx Total Confirmed, xxx New Deaths, xxx New Recovered, and xxx Total Recovered in *country_name*

Sample:
`Response: { "Countries": [ { "Country": "Afghanistan", "NewConfirmed": 5, "TotalConfirmed": 16, "NewDeaths": 0, "TotalDeaths": 0, "NewRecovered": 0, "TotalRecovered": 0 }, .. "Date": "2020-03-16T21:10:53.86852587Z" }`
