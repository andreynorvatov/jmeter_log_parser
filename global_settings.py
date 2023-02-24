from datetime import datetime

params_pars_dict = {
    "Thread name": "",
    "Grp Threads": "",
    "Parent name": "",
    "Sampler name": "",    
    "Time stamp": "",
    "Response Time":"",
    "End Time":"",
    "Connect Time":"",
    "Latency":"",
    "Idel Time":"",
    "Response code": "",
    "Host name": "",
    'Method':'',
    "URL": "",
    "Assertion Result":"",
    'Request Data':"",
    'Request Header':'',
    "Response Data": "",
    "Response Header":"",
}

colunms = [key for key in params_pars_dict]

report_template_path = "jmeter_log_parser/static/"
template_file_name = "base.html"
# template_file_name = "index_copy.html"
report_file_name = f'jmeter_log_parser/reports/report_{int(datetime.timestamp(datetime.now()))}.html'
report_name = 'Report'
