import requests
import json


class IDPayAPI:

    def __init__(self, api_key, domain, sandbox = False):
        self.api_key = api_key
        self.domain = domain
        self.sandbox = sandbox


    def payment(self, order_id, amount, callback_page, payer = {}):

        url = 'https://api.idpay.ir/v1.1/payment'

        data = {
            'order_id': order_id,
            'amount': amount,
            'callback': self.domain + callback_page,
            'name': payer.get('name'),
            'phone': payer.get('phone'),
            'mail': payer.get('mail'),
            'desc': payer.get('desc'),
        }

        headers = {
            'Content-Type': 'application/json',
            'X-API-KEY': self.api_key,
            'X-SANDBOX': '1' if self.sandbox else '0'
        }

        request = requests.post(url, data = json.dumps(data), headers = headers)

        if request.status_code == 201:
            return request.json()

        else:
            response = request.json()
            message = "Http status Code : " + str(request.status_code) + "   |   " + "Error Code : " + str(response['error_code']) + "   |   " + "Description : " + str(response['error_message'])

        return {'message': message}


    def verify(self, id, order_id):


        url = 'https://api.idpay.ir/v1.1/payment/verify'

        data = {
            'id': id,
            'order_id': order_id,
        }

        headers = {
            'Content-Type': 'application/json',
            'X-API-KEY': self.api_key,
            'X-SANDBOX': '1' if self.sandbox else '0'
        }

        request = requests.post(url, data=json.dumps(data), headers=headers)

        if request.status_code == 200:
            response = request.json()
            response['message'] = "Status: " + str(response['status']) + " (" + self.get_status(response['status']) + ")"

            return response

        else:
            response = request.json()
            message = "Http status Code : " + str(request.status_code) + "   |   " + "Error Code : " + str(response['error_code']) + "   |   " + "Description : " + str(response['error_message'])

        return {'message': message}


    def inquiry(self, id, order_id):

        url = 'https://api.idpay.ir/v1.1/payment/inquiry'

        data = {
            'id': id,
            'order_id': order_id,
        }

        headers = {
            'Content-Type': 'application/json',
            'X-API-KEY': self.api_key,
            'X-SANDBOX': '1' if self.sandbox else '0'
        }

        request = requests.post(url, data=json.dumps(data), headers=headers)

        if request.status_code == 200:
            response = request.json()
            response['message'] = "Status: " + str(response['status']) + " (" + self.get_status(response['status']) + ")"

            return response

        else:
            response = request.json()
            message = "Http status Code : " + str(request.status_code) + "   |   " + "Error Code : " + str(response['error_code']) + "   |   " + "Description : " + str(response['error_message'])

        return {'message': message}


    def get_status(self, status):

        states = {
            1: 'Transaction created',
            2: 'Transaction failed',
            3: 'An error has occurred',
            4: 'Transaction blocked',
            5: 'Transaction rejected to payer',
            6: 'Transaction rejected',
            7: 'Transaction canceled',
            8: 'Redirected to IPG',
            10: 'Verify pending',
            100: 'Transaction verified',
            101: 'Verified again',
            200: 'Transaction settled',
        }

        if states[int(status)]:
            return states[int(status)]

        return False