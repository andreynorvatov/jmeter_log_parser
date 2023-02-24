import global_settings
from xml_jmeter_log_parser import xml_jmeter_log_parser
from data_frame import row_data_to_data_frame
from template_writer import from_data_frame_to_html_report


def main(jmeter_xml_log_file_path):

    row_data = xml_jmeter_log_parser(
        jmeter_xml_log_file_path=jmeter_xml_log_file_path,
        params_pars_dict=global_settings.params_pars_dict)

    df = row_data_to_data_frame(
        row_data=row_data, columns=global_settings.colunms)

    from_data_frame_to_html_report(
        df=df,
        colunms=global_settings.colunms,
        report_template_path=global_settings.report_template_path,
        template_file_name=global_settings.template_file_name,
        report_file_name=global_settings.report_file_name,
        report_name=global_settings.report_name
    )

    print('Done')


if __name__ == "__main__":
    jmeter_xml_log_file_path = 'jmeter_log_parser/data/test_log.xml'
    main(jmeter_xml_log_file_path)
