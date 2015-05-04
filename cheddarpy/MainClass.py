import requests

API_ROOT = 'http://api.cheddarcard.com/v0.1'

class Cheddar(object):

  def __init__(self, access_token):
    self.access_token = access_token

  def _requestHeaders(self):
    return {"Authorization": "Bearer %s" % self.access_token }

  def user(self):
    url = '{API_ROOT}/user'.format(API_ROOT=API_ROOT)
    response = requests.get(url, headers = self._requestHeaders())
    return response.json()

  def accounts(self):
    url = '{API_ROOT}/accounts'.format(API_ROOT=API_ROOT)
    response = requests.get(url, headers = self._requestHeaders())
    return response.json()

  def account(self, account_id):
    url = '{API_ROOT}/account/{account_id}'.format(API_ROOT=API_ROOT,
                                                   account_id=account_id)
    response = requests.get(url, headers = self._requestHeaders())
    return response.json()

  def transactions(self, account_id):
    url = '{API_ROOT}/account/{account_id}/transactions'.format(API_ROOT=API_ROOT,
                                                                account_id=account_id)
    response = requests.get(url, headers = self._requestHeaders())
    return response.json()

  def history(self, account_id):
    url = '{API_ROOT}/account/{account_id}/history'.format(API_ROOT=API_ROOT,
                                                           account_id=account_id)
    response = requests.get(url, headers = self._requestHeaders())
    return response.json()
