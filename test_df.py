test_df = [['UC 01.Transfer self', '01.08. - Проверка СМС и исполнение платежа', '01.08.01. - /transfer/v1/self/transfer/huid/check', '25.08.2022 17:49:55.364', '500', 'VDI-P162', 'POST https://balancer-gateway-load1.omni.homecredit.ru:8112/transfer/v1/self/transfer/78112470-48b6-4379-9ada-89afbeff6dd6/check', '{"error":"INTERNAL_SERVER_ERROR","description":"Неизвестная ошибка взаимодействия","links":[]}'], ['UC 01.Transfer self', '01.00. - Генерация данных', '01.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:00:03.773', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 04.Transfer and type self', '04.00. - Генерация данных', '04.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:00:03.804', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 04.Transfer and type self', '04.00.- Генерация данных', '04.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:00:03.924', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 04.Transfer and type self', '04.00. - Генерация данных', '04.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:00:04.049', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 04.Transfer and type self', '04.00. - Генерация данных', '04.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:00:04.166', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 01.Transfer self', '01.00. - Генерация данных', '01.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:00:04.497', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 04.Transfer and type self', '04.05. - Повторное создание сессии (self)', '04.05.01 - /transfer/v1/self/transfer', '25.08.2022 18:03:07.666', '500', 'VDI-P162', 'GET https://balancer-gateway-load1.omni.homecredit.ru:8112/transfer/v1/self/transfer', '{"resultCode":"Error","resultText":"Системная ошибка","links":[]}'], ['UC 04.Transfer and type self', '04.00. - Генерация данных', '04.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:07:31.403', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 04.Transfer and type self', '04.00. - Генерация данных', '04.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:07:31.522', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 04.Transfer and type self', '04.00. - Генерация данных', '04.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:07:31.650', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 02.Transfer card', '02.00. - Генерация данных', '02.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:07:31.697', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 04.Transfer and type self', '04.00. - Генерация данных', '04.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:07:31.766', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 02.Transfer card', '02.05. - Подтверждение платежа', '02.05.01. - /transfer/v1/card/transfer/huid/confirm', '25.08.2022 18:08:28.989', '400', 'VDI-P162', 'POST https://balancer-gateway-load1.omni.homecredit.ru:8112/transfer/v1/card/transfer/6e918f66-072c-4edb-836c-f3738a9d198d/confirm', 'Non-TEXT response data, cannot record: ()'], ['UC 01.Transfer self', '01.08. - Проверка СМС и исполнение платежа', '01.08.01. - /transfer/v1/self/transfer/huid/check', '25.08.2022 18:09:27.991', '500', 'VDI-P162', 'POST https://balancer-gateway-load1.omni.homecredit.ru:8112/transfer/v1/self/transfer/9502dff6-c6b6-4881-a83a-4b73b09bab26/check', '{"error":"INTERNAL_SERVER_ERROR","description":"Неизвестная ошибка взаимодействия","links":[]}'], ['UC 02.Transfer card', '02.05. - Подтверждение платежа', '02.05.01. - /transfer/v1/card/transfer/huid/confirm', '25.08.2022 18:12:59.145', '400', 'VDI-P162', 'POST https://balancer-gateway-load1.omni.homecredit.ru:8112/transfer/v1/card/transfer/67eeb4a7-3983-4bfb-b2f3-4087e654a19a/confirm', 'Non-TEXT response data, cannot record: ()'], ['UC 04.Transfer and type self', '04.00. - Генерация данных', '04.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:14:09.564', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 04.Transfer and type self', '04.00. - Генерация данных', '04.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:14:09.672', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 01.Transfer self', '01.00. - Генерация данных', '01.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:14:09.681', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 04.Transfer and type self', '04.00. - Генерация данных', '04.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:14:09.684', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 02.Transfer card', '02.00. - Генерация данных', '02.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:14:09.771', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 04.Transfer and type self', '04.00. - Генерация данных', '04.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:14:09.794', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 02.Transfer card', '02.05. - Подтверждение платежа', '02.05.01. - /transfer/v1/card/transfer/huid/confirm','25.08.2022 18:15:07.382', '400', 'VDI-P162', 'POST https://balancer-gateway-load1.omni.homecredit.ru:8112/transfer/v1/card/transfer/954aba24-1c6f-407c-b892-4b3bff20eccd/confirm', 'Non-TEXT response data, cannot record: ()'], ['UC 01.Transfer self', '01.08. - Проверка СМС и исполнение платежа', '01.08.01. - /transfer/v1/self/transfer/huid/check', '25.08.2022 18:15:24.308', '500', 'VDI-P162', 'POST https://balancer-gateway-load1.omni.homecredit.ru:8112/transfer/v1/self/transfer/98c016cc-a5e0-44f3-ada5-0c730ad74d98/check', '{"error":"INTERNAL_SERVER_ERROR","description":"Неизвестная ошибка взаимодействия","links":[]}'], ['UC 04.Transfer and type self', '04.02. - Создание сессии (self)', '04.02.01 - /transfer/v1/self/transfer', '25.08.2022 18:17:11.042', '500', 'VDI-P162', 'GET https://balancer-gateway-load1.omni.homecredit.ru:8112/transfer/v1/self/transfer', '{"resultCode":"Error","resultText":"Системная ошибка","links":[]}'], ['UC 04.Transfer and type self', '04.00. - Генерация данных', '04.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:20:47.359', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 04.Transfer and type self', '04.00. - Генерация данных', '04.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:20:47.486', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 01.Transfer self', '01.00. - Генерация данных', '01.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:20:47.507', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 04.Transfer and type self', '04.00. - Генерация данных', '04.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:20:47.597', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 04.Transfer and type self', '04.00. - Генерация данных', '04.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:20:47.717', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 04.Transfer and type self', '04.00. - Генерация данных', '04.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:20:47.837', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}'], ['UC 04.Transfer and type self', '04.02. - Создание сессии (self)', '04.02.01 - /transfer/v1/self/transfer', '25.08.2022 18:21:07.141', '500', 'VDI-P162', 'GET https://balancer-gateway-load1.omni.homecredit.ru:8112/transfer/v1/self/transfer', '{"resultCode":"Error","resultText":"Системная ошибка","links":[]}'], ['UC 02.Transfer card', '02.07. - Проверка СМС и исполнение платежа', '02.07.01. - /transfer/v1/card/transfer/huid/check', '25.08.2022 18:21:22.934', '500', 'VDI-P162', 'POST https://balancer-gateway-load1.omni.homecredit.ru:8112/transfer/v1/card/transfer/976e3074-d7f0-4231-9fea-a774bb14967e/check', '{"error":"INTERNAL_SERVER_ERROR","description":"Неизвестная ошибка взаимодействия","links":[]}'], ['UC 01.Transfer self', '01.08. - Проверка СМС и исполнение платежа', '01.08.01. - /transfer/v1/self/transfer/huid/check', '25.08.2022 18:22:02.343', '500', 'VDI-P162', 'POST https://balancer-gateway-load1.omni.homecredit.ru:8112/transfer/v1/self/transfer/9fdd63d1-71f0-4fcc-9cdd-8ad830a65eff/check', '{"error":"INTERNAL_SERVER_ERROR","description":"Неизвестная ошибка взаимодействия","links":[]}'], ['UC 01.Transfer self', '01.08. - Проверка СМС и исполнение платежа', '01.08.01. - /transfer/v1/self/transfer/huid/check', '25.08.2022 18:22:44.724', '500', 'VDI-P162', 'POST https://balancer-gateway-load1.omni.homecredit.ru:8112/transfer/v1/self/transfer/17441787-e5c2-4a7c-819b-00c5e7f7bc46/check', '{"error":"INTERNAL_SERVER_ERROR","description":"Неизвестная ошибка взаимодействия","links":[]}'], ['UC 01.Transfer self', '01.02. - Создание сессии (self)', '01.02.01 - /transfer/v1/self/transfer', '25.08.2022 18:24:41.353', '500','VDI-P162', 'GET https://balancer-gateway-load1.omni.homecredit.ru:8112/transfer/v1/self/transfer', '{"resultCode":"Error","resultText":"Системная ошибка","links":[]}'], ['UC 01.Transfer self', '01.02. - Создание сессии (self)', '01.02.01 - /transfer/v1/self/transfer', '25.08.2022 18:26:02.100', '500', 'VDI-P162', 'GET https://balancer-gateway-load1.omni.homecredit.ru:8112/transfer/v1/self/transfer', '{"resultCode":"Error","resultText":"Системная ошибка","links":[]}'], ['UC 01.Transfer self', '01.00. - Генерация данных', '01.00.01. - (http) - getDataPoolNextVal (transfer)', '25.08.2022 18:27:25.798', '500', 'VDI-P162', 'POST https://qad.load.homecredit.ru:8081/api/datapool/getitem', '{"statusCode":500,"error":"Internal Server Error","message":"Row or pool is empty!"}']]



# import time  

# time_stamp = str(time.time()).replace('.', '')
# print("Timestamp:", time_stamp)

# l1= [1,2,3]

# l2 = ['a', 'b', 'c']

# for l in l1:
#     print(l)
#     for l_l in l2:
#         print(l_l)


# li = [1, 2, 3, {'a':'a', 'b':'b'}]

# for l in li:
#     print(l)

from jinja2 import Environment, FileSystemLoader
from datetime import datetime

report_template_path = "jmeter_log_parser/static/"
template_file_name = "accordion_thread_list.html"
# template_file_name = "index_copy.html"
report_file_name = f'jmeter_log_parser/reports/report_test_{int(datetime.timestamp(datetime.now()))}.html'
report_name = 'Report'

l1 = [1,2,3,4]

def from_data_frame_to_html_report(df, report_template_path, template_file_name, report_file_name, report_name):

	environment = Environment(loader=FileSystemLoader(report_template_path))
	template = environment.get_template(template_file_name)


	report_file_name = report_file_name
	report_name = report_name


	content = template.render(df=df, report_name=report_name)


	with open(report_file_name, mode="w", encoding="utf-8") as report:
		report.write(content)

from_data_frame_to_html_report(df=l1, report_template_path=report_template_path, template_file_name=template_file_name, report_file_name=report_file_name, report_name=report_name)
print('Done')