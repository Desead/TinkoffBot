import datetime

from tinkoff.invest import Client, MoneyValue

from lib.func import GetAccountSandbox, CloseAccountSandbox

TOKEN = 't.coN1FzanFdy9xNTMlkbBo7qM1h2knHd-wfy12kkEkMoeLtYVUfLkBu76pJabUXPSsLHzQN7ajTdIJkzNrY9pDg'
APP_NAME = ''
SANDBOX = True
LOT_1 = 1
LOT_2 = 1
ACCOUNT_ID = ''


def main():
    with Client(token=TOKEN, app_name=APP_NAME) as client:
        acc = client.instruments.trading_schedules(from_=datetime.datetime.utcnow(), to=datetime.datetime.utcnow())
        exchange = ['FORTS']
        for i in acc.exchanges:
            if i.exchange in exchange:
                print(i)
                print('=============')
                print(i.days[0].is_trading_day)
                print(i.days[0].start_time)
                print(i.days[0].end_time)
                print(i.days[0].evening_start_time)
                print(i.days[0].evening_end_time)
                print('=============')
                print(i.days[0].start_time.timestamp())
                print(datetime.datetime.utcnow().timestamp())
                print(i.days[0].start_time.timestamp() > datetime.datetime.utcnow().timestamp())


if __name__ == '__main__':
    main()
