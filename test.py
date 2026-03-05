#读取csv文件
import pandas as pd

df_153 = pd.read_csv("C:\\Users\\xxx\\Downloads\\logs-insights-results (1).csv")
df_lambda = pd.read_csv("C:\\Users\\xxx\\Downloads\\logs-insights-results (2).csv")
not_exist = df_153[~df_153['request_id'].isin(df_lambda['http_request_ip'])]
print(not_exist)