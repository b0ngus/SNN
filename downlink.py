import requests
import time

# Define your payloads
login_payload = { 
  "login": "prath",
  "password": "Balloon_8902",
  "lastName": "string",
  "role": "string",
  "avatar": "string",
  "enabled": True,
  "firstName": "string",
  "validated": True,
  "phone": "string",
  "requestMaxRateDuration": 0,
  "requestMaxRate": 0,
  "links": [
    {
      "rel": "string",
      "href": "string"
    }
  ],
  "id": 0,
  "email": "string",
  "expirationDate": 0,
  "customer": {
    "maxEndDevices": 0,
    "maxUsers": 0,
    "maxGateways": 0,
    "geolocationExpirationDate": 0,
    "name": "string",
    "logo": "string",
    "links": [
      {
        "rel": "string",
        "href": "string"
      }
    ],
    "geolocationAuthorized": True,
    "id": 0,
    "billing": True}}  # Your login payload dictionary

payload_k = {
    
    "fPort": 7,
    "payload": "B39293CB3E2034A1AA03003B00036DDD",
    "confirmed": False,
    "contentType": "text",
    
    "endDevice": {      
        "devEui": "506F980000003872",
        "devAddr": "string",
        "country": "string",
        "cluster": {
            "pushConfiguration": {
                "mqttWillTopic": "string",
                "mqttTlsEnabled": True,
                "mqttQoS": 0,
                "type": "string",
                "tlsKeyFileName": "string",
                "tlsCertFileName": "string",
                "mqttDataDownEventTopic": "string",
                "password": "string",
                "mqttClientId": "string",
                "httpDataUpRoute": "string",
                "msgDetailLevel": "string",
                "links": [
                    {
                        "rel": "string",
                        "href": "string"
                    }
                ],
                "mqttWillQoS": 0,
                "id": 0,
                "mqttHost": "string",
                "mqttPassword": "string",
                "headers": [
                    {
                        "value": "string",
                        "key": "string"
                    }
                ],
                "mqttWillPayload": "string",
                "mqttConnectTimeout": 0,
                "url": "string",
                "mqttCleanSession": True,
                "httpDataDownEventRoute": "string",
                "mqttUser": "string",
                "tlsCaFileName": "string",
                "name": "string",
                "mqttDataUpTopic": "string",
                "user": "string",
                "mqttKeepAlive": 0,
                "mqttPort": 0,
                "customer": {
                    "maxUsers": 0,
                    "maxEndDevices": 0,
                    "maxGateways": 0,
                    "geolocationExpirationDate": 0,
                    "name": "string",
                    "logo": "string",
                    "links": [
                        {
                            "rel": "string",
                            "href": "string"
                        }
                    ],
                    "id": 0,
                    "geolocationAuthorized": True,
                    "billing": True
                }
            },
            "hexa": True,
            "pushEnabled": True,
            "name": "string",
            "geolocEnabled": True,
            "links": [
                {
                    "rel": "string",
                    "href": "string"
                }
            ],
            "id": 0,
            "customer": {
                "maxUsers": 0,
                "maxEndDevices": 0,
                "maxGateways": 0,
                "geolocationExpirationDate": 0,
                "name": "string",
                "logo": "string",
                "links": [
                    {
                        "rel": "string",
                        "href": "string"
                    }
                ],
                "id": 0,
                "geolocationAuthorized": True,
                "billing": True
            },
            "geolocExpirationDate": 0
        },
        "altitude": 0,
        "appSKey": "string",
        "lastDataUpDataRate": "string",
        "downlinkSlotFreq": 0,
        "nwkSKey": "string",
        "latitude": 0,
        "fcntUp": 0,
        "adrEnabled": True,
        "fNwkSIntKey": "string",
        "cfList": [
            "string"
        ],
        "devNonceCounter": True,
        "lastDataUpDate": 0,
        "links": [
            {
                "rel": "string",
                "href": "string"
            }
        ],
        "appKey": "string",
        "rx1DrOffset": 0,
        "longitude": 0,
        "downlinkSlotDr": "string",
        "rx1Delay": 0,
        "rfRegion": "string",
        "rx2Dr": 0,
        "profile": "string",
        "rx2Freq": 0,
        "lastDataDownDate": 0,
        "sNwkSIntKey": "string",
        "rxWindows": "string",
        "regParamsRevision": "string",
        "name": "string",
        "appEui": "string",
        "activation": "string",
        "macVersion": "string",
        "fcntDown": 0,
        "dwellTime": True,
        "classType": "string",
        "status": "string",
        "geolocation": "string"
    },
    "historic": [
        {
            "date": 0,
            "event": "string",
            "status": "string"
        }
    ],
    "gwEui": "string",
    "ttl": 0,
    "nbAttempts": 0,
    "maxAttempts": 0,
    "fCntDown": 0,
    "encodingType": "string",
    "links": [
        {
            "rel": "string",
            "href": "string"
        }
    ],
    "id": "string",
    "dlParameters": [
        {
            "rxWindow": "string",
            "freq": 0,
            "dataRate": "string"
        }
    ],
    "event": "string",
    "status": "string",
    "timestamp": 0
    }
 # Payload for extracting value A
payload_eb = {
    "fPort": 7,
    "payload": "B39293CB3E2034A1AA03000100028C10",
    "confirmed": False,
    "contentType": "text",
    "endDevice": {
        "devEui": "506F980000003872",
        "devAddr": "string",
        "country": "string",
        "cluster": {
            "pushConfiguration": {
                "mqttWillTopic": "string",
                "mqttTlsEnabled": True,
                "mqttQoS": 0,
                "type": "string",
                "tlsKeyFileName": "string",
                "tlsCertFileName": "string",
                "mqttDataDownEventTopic": "string",
                "password": "string",
                "mqttClientId": "string",
                "httpDataUpRoute": "string",
                "msgDetailLevel": "string",
                "links": [
                    {
                        "rel": "string",
                        "href": "string"
                    }
                ],
                "mqttWillQoS": 0,
                "id": 0,
                "mqttHost": "string",
                "mqttPassword": "string",
                "headers": [
                    {
                        "value": "string",
                        "key": "string"
                    }
                ],
                "mqttWillPayload": "string",
                "mqttConnectTimeout": 0,
                "url": "string",
                "mqttCleanSession": True,
                "httpDataDownEventRoute": "string",
                "mqttUser": "string",
                "tlsCaFileName": "string",
                "name": "string",
                "mqttDataUpTopic": "string",
                "user": "string",
                "mqttKeepAlive": 0,
                "mqttPort": 0,
                "customer": {
                    "maxUsers": 0,
                    "maxEndDevices": 0,
                    "maxGateways": 0,
                    "geolocationExpirationDate": 0,
                    "name": "string",
                    "logo": "string",
                    "links": [
                        {
                            "rel": "string",
                            "href": "string"
                        }
                    ],
                    "id": 0,
                    "geolocationAuthorized": True,
                    "billing": True
                }
            },
            "hexa": True,
            "pushEnabled": True,
            "name": "string",
            "geolocEnabled": True,
            "links": [
                {
                    "rel": "string",
                    "href": "string"
                }
            ],
            "id": 0,
            "customer": {
                "maxUsers": 0,
                "maxEndDevices": 0,
                "maxGateways": 0,
                "geolocationExpirationDate": 0,
                "name": "string",
                "logo": "string",
                "links": [
                    {
                        "rel": "string",
                        "href": "string"
                    }
                ],
                "id": 0,
                "geolocationAuthorized": True,
                "billing": True
            },
            "geolocExpirationDate": 0
        },
        "altitude": 0,
        "appSKey": "string",
        "lastDataUpDataRate": "string",
        "downlinkSlotFreq": 0,
        "nwkSKey": "string",
        "latitude": 0,
        "fcntUp": 0,
        "adrEnabled": True,
        "fNwkSIntKey": "string",
        "cfList": [
            "string"
        ],
        "devNonceCounter": True,
        "lastDataUpDate": 0,
        "links": [
            {
                "rel": "string",
                "href": "string"
            }
        ],
        "appKey": "string",
        "rx1DrOffset": 0,
        "longitude": 0,
        "downlinkSlotDr": "string",
        "rx1Delay": 0,
        "rfRegion": "string",
        "rx2Dr": 0,
        "profile": "string",
        "rx2Freq": 0,
        "lastDataDownDate": 0,
        "sNwkSIntKey": "string",
        "rxWindows": "string",
        "regParamsRevision": "string",
        "name": "string",
        "appEui": "string",
        "activation": "string",
        "macVersion": "string",
        "fcntDown": 0,
        "dwellTime": True,
        "classType": "string",
        "status": "string",
        "geolocation": "string"
    },
    "historic": [
        {
            "date": 0,
            "event": "string",
            "status": "string"
        }
    ],
    "gwEui": "string",
    "ttl": 0,
    "nbAttempts": 0,
    "maxAttempts": 0,
    "fCntDown": 0,
    "encodingType": "string",
    "links": [
        {
            "rel": "string",
            "href": "string"
        }
    ],
    "id": "string",
    "dlParameters": [
        {
            "rxWindow": "string",
            "freq": 0,
            "dataRate": "string"
        }
    ],
    "event": "string",
    "status": "string",
    "timestamp": 0
    }  # Payload for extracting value B
payload_vi = {"fPort": 7,
    "payload": "B39293CB3E2034A1AA03001A00087C10",
    "confirmed": False,
    "contentType": "text",
    "endDevice": {
        "devEui": "506F980000003872",
        "devAddr": "string",
        "country": "string",
        "cluster": {
            "pushConfiguration": {
                "mqttWillTopic": "string",
                "mqttTlsEnabled": True,
                "mqttQoS": 0,
                "type": "string",
                "tlsKeyFileName": "string",
                "tlsCertFileName": "string",
                "mqttDataDownEventTopic": "string",
                "password": "string",
                "mqttClientId": "string",
                "httpDataUpRoute": "string",
                "msgDetailLevel": "string",
                "links": [
                    {
                        "rel": "string",
                        "href": "string"
                    }
                ],
                "mqttWillQoS": 0,
                "id": 0,
                "mqttHost": "string",
                "mqttPassword": "string",
                "headers": [
                    {
                        "value": "string",
                        "key": "string"
                    }
                ],
                "mqttWillPayload": "string",
                "mqttConnectTimeout": 0,
                "url": "string",
                "mqttCleanSession": True,
                "httpDataDownEventRoute": "string",
                "mqttUser": "string",
                "tlsCaFileName": "string",
                "name": "string",
                "mqttDataUpTopic": "string",
                "user": "string",
                "mqttKeepAlive": 0,
                "mqttPort": 0,
                "customer": {
                    "maxUsers": 0,
                    "maxEndDevices": 0,
                    "maxGateways": 0,
                    "geolocationExpirationDate": 0,
                    "name": "string",
                    "logo": "string",
                    "links": [
                        {
                            "rel": "string",
                            "href": "string"
                        }
                    ],
                    "id": 0,
                    "geolocationAuthorized": True,
                    "billing": True
                }
            },
            "hexa": True,
            "pushEnabled": True,
            "name": "string",
            "geolocEnabled": True,
            "links": [
                {
                    "rel": "string",
                    "href": "string"
                }
            ],
            "id": 0,
            "customer": {
                "maxUsers": 0,
                "maxEndDevices": 0,
                "maxGateways": 0,
                "geolocationExpirationDate": 0,
                "name": "string",
                "logo": "string",
                "links": [
                    {
                        "rel": "string",
                        "href": "string"
                    }
                ],
                "id": 0,
                "geolocationAuthorized": True,
                "billing": True
            },
            "geolocExpirationDate": 0
        },
        "altitude": 0,
        "appSKey": "string",
        "lastDataUpDataRate": "string",
        "downlinkSlotFreq": 0,
        "nwkSKey": "string",
        "latitude": 0,
        "fcntUp": 0,
        "adrEnabled": True,
        "fNwkSIntKey": "string",
        "cfList": [
            "string"
        ],
        "devNonceCounter": True,
        "lastDataUpDate": 0,
        "links": [
            {
                "rel": "string",
                "href": "string"
            }
        ],
        "appKey": "string",
        "rx1DrOffset": 0,
        "longitude": 0,
        "downlinkSlotDr": "string",
        "rx1Delay": 0,
        "rfRegion": "string",
        "rx2Dr": 0,
        "profile": "string",
        "rx2Freq": 0,
        "lastDataDownDate": 0,
        "sNwkSIntKey": "string",
        "rxWindows": "string",
        "regParamsRevision": "string",
        "name": "string",
        "appEui": "string",
        "activation": "string",
        "macVersion": "string",
        "fcntDown": 0,
        "dwellTime": True,
        "classType": "string",
        "status": "string",
        "geolocation": "string"
    },
    "historic": [
        {
            "date": 0,
            "event": "string",
            "status": "string"
        }
    ],
    "gwEui": "string",
    "ttl": 0,
    "nbAttempts": 0,
    "maxAttempts": 0,
    "fCntDown": 0,
    "encodingType": "string",
    "links": [
        {
            "rel": "string",
            "href": "string"
        }
    ],
    "id": "string",
    "dlParameters": [
        {
            "rxWindow": "string",
            "freq": 0,
            "dataRate": "string"
        }
    ],
    "event": "string",
    "status": "string",
    "timestamp": 0
             }  # Payload for extracting value C

# Define your endpoints
login_endpoint = "https://sharedwmc.wanesy.com/gms/application/login"
downlink_endpoint = "https://sharedwmc.wanesy.com/gms/application/dataDown"

# Function to perform login
def perform_login():
    response = requests.post(login_endpoint, json=login_payload)
    if response.status_code == 200:
        return response.json()["token"]  # Assuming token is returned upon successful login
    else:
        print("Login failed.")
        return None

# Function to perform downlink request with payload
def perform_downlink_request(payload, token):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"  # Assuming token is required for authorization
    }
    response = requests.post(downlink_endpoint, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()  # Assuming you want to return the response JSON
    else:
        print("downlink request failed.")
        return None

# Main function to execute workflow
def main():
    token = perform_login()
    if token:
        result_a = perform_downlink_request(payload_k, token)
        time.sleep(2)  # Delay for 2 seconds
        result_b = perform_downlink_request(payload_eb, token)
        time.sleep(2)  # Delay for 2 seconds
        result_c = perform_downlink_request(payload_vi, token)
        # Process results if needed
    else:
        print("Unable to proceed without a valid token.")

if __name__ == "__main__":
    main()
