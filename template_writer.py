from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import pandas as pd

# colunms = ["Thread name", "Parent name", "Sampler name", "Time stamp"]
# df = pd.DataFrame([
# 	['UC 01.Transfer self', '01.08. - Проверка СМС и исполнение платежа', '01.08.01. - /transfer/v1/self/transfer/huid/check error', '1661435395364'],
# 	['UC 01.Transfer self', '01.08. - Проверка СМС и исполнение платежа', '01.08.01. - /transfer/v1/self/transfer/huid/check error', '1661435395353'],
# 	['UC 01.Transfer self', '01.08. - Проверка СМС и исполнение платежа', '01.08.01. - /transfer/v1/self/transfer/huid/check error', '16614353953111'],
# 	['UC 04.Transfer and type self', '04.00. - Генерация данных', '01.00.01. - (http) - getDataPoolNextVal (transfer)', '16614353953111']],
# 	columns = colunms
# )

# print(df)

def from_data_frame_to_html_report(df, colunms, report_template_path, template_file_name, report_file_name, report_name):

	environment = Environment(loader=FileSystemLoader(report_template_path))
	template = environment.get_template(template_file_name)


	report_file_name = report_file_name
	report_name = report_name


	content = template.render(df=df, colunms=colunms, report_name=report_name)


	with open(report_file_name, mode="w", encoding="utf-8") as report:
		report.write(content)
