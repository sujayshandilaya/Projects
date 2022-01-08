# main.py
import argparse
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions



'''
def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", dest="input", required=True)
    parser.add_argument("--error", dest="error", required=True)
    parser.add_argument("--output", dest="output", required=True)
    app_args, pipeline_args = parser. parse_known_args()
	
    lines = pipeline | 'ReadMyFile' >> beam.io.ReadFromText(
    'gs://some/inputData.txt')
    
    
	with beam.Pipeline(options=PipelineOptions(pipeline_args)) as p:
		data = load_apache_logs(p, app_args.input)
		output = data | "FILTER" >> beam.Filter(filter_cart_requests)
		output | "WRITE" >> beam.io.WriteToText(app_args.output)
        
'''

if __name__ == '__main__':
    #run()
    input_filename = 'gs://cms_medicare_poc/raw/MUP_DPR_RY21_P04_V10_DY17_NPIBN_1.csv'
    output_filename = 'gs://cms_medicare_poc/raw/MUP_DPR_RY21_P04_V10_DY17_NPIBN_1_output.csv'
    
    options = PipelineOptions()
    p = beam.Pipeline(options=options)
    csv_lines = (p | ReadFromText(input_filename, skip_header_lines=1) | beam.ParDo(Split()) )

    output= (csv_lines | WriteToText(output_filename))