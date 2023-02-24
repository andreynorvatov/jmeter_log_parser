import pandas as pd

# columns = ["Thread name", "Parent name", " Sampler name", "Time stamp"]
# from test_df import test_df
# from global_settings import colunms
def row_data_to_data_frame(row_data, columns):
	df = pd.DataFrame(row_data, columns=columns)
	df = df.sort_values(by=['Thread name', 'Parent name', 'Sampler name', 'Time stamp'])
	# pivot_df = pd.pivot_table(df, index=["Thread name", "Parent name"])
	# print(pivot_df)
	return df

# print(row_data_to_data_frame(test_df, colunms))

# df = row_data_to_data_frame(test_df, colunms)
# print(df)
# print(df['Thread name'].value_counts().to_dict().get('UC 01.Transfer self'))
# print(df[df["Sampler name"].isin(['01.00.01. - (http) - getDataPoolNextVal (transfer)'])]["Time stamp"])
# print(df['Thread name'].unique())
# print(df[df['Thread name'].isin(['UC 01.Transfer self'])]['Parent name'].unique())
# print(df['Sampler name'].groupby('Parent name'))

# print(df[df['Thread name'].isin(['UC 01.Transfer self']) & df['Parent name'].isin(['01.00. - Генерация данных'])]['Sampler name'].unique())
# p_df = df.pivot_table(index=['Thread name', 'Sampler name'])
# p_df = df.pivot(columns=[])
# print(p_df)
# print(df.pivot_table(index=['Thread name', 'Parent name', 'Sampler name', 'Time stamp'])['Thread name'])

# pivot_df = pd.pivot_table(df, index=["Thread name", "Parent name", "Sampler name", "Time stamp"])
# print(pivot_df)
# print(pivot_df["Thread name"])
# for key,value in pivot_df.items():
	# print(key[0])
# print(pivot_df)
# colNames = ["Thread name", "Parent name", " Sampler name", "Time stamp"]
# print(pivot_df.to_html())

# dictTwo = {"Row 1":['UC 01.Transfer self 1-2', '01.08. - Проверка СМС и исполнение платежа', '01.08.01. - /transfer/v1/self/transfer/huid/check error', '1661435395364'],
# 		   "Row 2":['UC 01.Transfer self 1-3', '01.08. - Проверка СМС и исполнение платежа', '01.08.01. - /transfer/v1/self/transfer/huid/check error', '1661435395353'],
# 		   "Row 3":['UC 01.Transfer self 1-3', '01.08. - Проверка СМС и исполнение платежа', '01.08.01. - /transfer/v1/self/transfer/huid/check error', '16614353953111'],
# 		   "Row 4":['UC 04.Transfer and type self 4-11', '04.00. - Генерация данных', '01.00.01. - (http) - getDataPoolNextVal (transfer)', '16614353953111'],
           
#            }
# df = pd.DataFrame([
# 	['UC 01.Transfer self', '01.08. - Проверка СМС и исполнение платежа', '01.08.01. - /transfer/v1/self/transfer/huid/check error', '1661435395364'],
# 	['UC 01.Transfer self', '01.08. - Проверка СМС и исполнение платежа', '01.08.01. - /transfer/v1/self/transfer/huid/check error', '1661435395353'],
# 	['UC 01.Transfer self', '01.08. - Проверка СМС и исполнение платежа', '01.08.01. - /transfer/v1/self/transfer/huid/check error', '16614353953111'],
# 	['UC 04.Transfer and type self', '04.00. - Генерация данных', '01.00.01. - (http) - getDataPoolNextVal (transfer)', '16614353953111']],
# 	columns = ["Thread name", "Parent name", " Sampler name", "Time stamp"]
# )
# df = pd.DataFrame.from_dict(dictTwo, orient='index', columns=colNames)
# print(df)

# new_row = ['UC 99.New row', '99.00. - New row', '99.00.01. - (http) - New row', '99999999']
# df = df.append(new_row, ignore_index=True)
# print('------NEW DF:---------------------------------------------------')
# print(df)