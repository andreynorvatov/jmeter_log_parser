from bs4 import BeautifulSoup
import time
from datetime import datetime

params_pars_dict = {
    "Thread name": "",
    "Parent name": "",
    "Sampler name": "",
    "Time stamp": "",
    "Response code" : "",
    "Host name" : "",
}

def xml_jmeter_log_parser(jmeter_xml_log_file_path: str, params_pars_dict) -> list:
    result_array = []

    jmeter_xml_log_file_path = jmeter_xml_log_file_path

    with open(jmeter_xml_log_file_path, encoding='utf-8') as file:
        src = file.read()
        soup = BeautifulSoup(src, "xml")

    testResults_tag = soup.select("testResults")
    # print(len(testResults_tag))

    # Лист из верхних транзакшн контроллеров
    sample = list(testResults_tag[0].children)
    sample_children = [i for i in sample if i!='\n']

    for parent_name in sample_children:

        # перебор TC и поиск TC со статусом fail
        parent = parent_name.find_all('sample', s="false")
        # print(parent[0]['tn'])
        # print(parent[0]['lb'])

        # Thread name (tn)
        # result_list.append(parent[0].get('tn'))
        thread_name_row = parent[0].get('tn').split(" ")
        thread_name = " ".join(thread_name_row[:-1])
        grp_thread = thread_name_row[-1]
        params_pars_dict['Thread name'] = thread_name
        params_pars_dict['Grp Threads'] = grp_thread
        # print(params_pars_dict['Thread name'])
        # Parent name (lb) (TC name)
        # result_list.append(parent[0].get('lb'))
        params_pars_dict['Parent name'] = parent[0].get('lb')

        # перебор зафейленных семплеров
        sample = parent[0].find_all(s="false")
        # Sampler name
        # result_list.append(sample[0].get('lb'))
        params_pars_dict['Sampler name'] = sample[0].get('lb')
        # time stamp
        # result_list.append(sample[0].get('ts'))
        time_start_unix_ms = sample[0].get('ts')
        response_time_ms = sample[0].get('t')
        params_pars_dict['Time stamp'] = datetime.fromtimestamp(int(time_start_unix_ms)/1000).strftime('%d.%m.%Y %H:%M:%S.%f')[:-3]
        params_pars_dict['Response Time'] = response_time_ms
        params_pars_dict['End Time'] = datetime.fromtimestamp((int(time_start_unix_ms) + int(response_time_ms))/1000).strftime('%d.%m.%Y %H:%M:%S.%f')[:-3]
        params_pars_dict['Connect Time'] = sample[0].get('ct')
        params_pars_dict['Latency'] = sample[0].get('lt')
        params_pars_dict['Idel Time'] = sample[0].get('it')
        
        # Response code
        # result_list.append(sample[0].get('rc'))
        params_pars_dict['Response code'] = sample[0].get('rc')
        # Host name
        # result_list.append(sample[0].get('hn'))
        params_pars_dict['Host name'] = sample[0].get('hn')

        # получеие атрибутов запроса/ответа
        # request_response_attr = sample[0].find('java.net.URL')
        # params_pars_dict['Request method, URL'] = " ".join([str(sample[0].find('method').get_text()), str(sample[0].find('java.net.URL').get_text())])
        params_pars_dict['Method'] = sample[0].find('method').get_text()
        params_pars_dict['URL'] = sample[0].find('java.net.URL').get_text()
        # print(params_pars_dict['Request method & URL'])
        failure_message_of_assertion_result = sample[0].find('failureMessage')
        params_pars_dict['Assertion Result'] = 'No assertion result' if failure_message_of_assertion_result is None else failure_message_of_assertion_result.get_text().strip()
        

        params_pars_dict['Request Data'] = sample[0].find('queryString').get_text().strip()
        params_pars_dict['Request Header'] = sample[0].find('responseHeader').get_text().strip()

        params_pars_dict['Response Data'] = sample[0].find('responseData').get_text().strip()
        params_pars_dict['Response Header'] = sample[0].find('responseHeader').get_text().strip()


        result_array.append([params for key, params in params_pars_dict.items()])

    return result_array


# print(xml_jmeter_log_parser('jmeter_log_parser/data/log2.xml', params_pars_dict=params_pars_dict))
xml_jmeter_log_parser('jmeter_log_parser/data/log2.xml', params_pars_dict=params_pars_dict)

