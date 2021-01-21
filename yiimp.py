import requests
import fire


class PublicApi:

    def __init__(self, pool=None):
        if pool is None:
            self.pool = "http://api.zergpool.com:8080"
        else:
            self.pool = pool

    def request(self, method, path):
        url = self.pool + path

        s = requests.Session()
        response = s.request(method, url)

        if response.status_code == 200:
            return response.json()
        elif response.content:
            raise Exception(str(response.status_code) + ": " + response.reason + ": " + str(response.content))
        else:
            raise Exception(str(response.status_code) + ": " + response.reason)

    def get_wallet(self, wallet):
        return self.request('GET', '/api/wallet?address=' + wallet)

    def get_wallet_ex(self, wallet):
        return self.request('GET', '/api/walletEx?address=' + wallet)

    def get_status(self):
        return self.request('GET', '/api/status')

    def get_currencies(self):
        return self.request('GET', '/api/currencies')

    def get_blocks(self):
        return self.request('GET', '/api/blocks')

    def get_blocks_coin(self, sym):
        return self.request('GET', '/api/blocks?coin=' + sym)

    def get_miners(self):
        return self.request('GET', '/api/miners')


if __name__ == '__main__':
    fire.Fire(PublicApi)
