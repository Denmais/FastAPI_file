import pandas as pd

url = "https://storage.yandexcloud.net/s3-sprint3/cohort_32/Denmais09/TWpBeU5DMHhNUzB5T1ZReU1Eb3hNem93TlFsRVpXNXRZV2x6TURrPQ==/user_order_log.csv"

c = pd.read_csv(url)
c.to_csv('user_order_log.csv')



print(c)