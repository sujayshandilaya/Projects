#https://medium.com/@SadeeqAkintola/loading-data-from-multiple-csv-files-in-gcs-into-bigquery-using-cloud-dataflow-python-a695648e9c63
#https://www.cloudskillsboost.google/focuses/3460?parent=catalog
import argparse
import logging
import re

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def schema(input_file):
    f = open(input_file, 'r')
    line = f.readline()
    columns=line.split(',')
    schema=''
    for column in columns:
        schema+=',{}:STRING'.format(column)
    return schema
    
class DataTransformation:

    def parse_method(self, string_input):

        values = re.split(",", re.sub('\r\n', '', re.sub('"', '',
                                                         string_input)))
        row = dict(
            zip(('Prscrbr_NPI','Prscrbr_Last_Org_Name','Prscrbr_First_Name','Prscrbr_City','Prscrbr_State_Abrvtn','Prscrbr_State_FIPS','Prscrbr_Type','Prscrbr_Type_Src','Brnd_Name','Gnrc_Name','Tot_Clms','Tot_30day_Fills','Tot_Day_Suply','Tot_Drug_Cst','Tot_Benes','GE65_Sprsn_Flag','GE65_Tot_Clms','GE65_Tot_30day_Fills','GE65_Tot_Drug_Cst','GE65_Tot_Day_Suply','GE65_Bene_Sprsn_Flag','GE65_Tot_Benes'),
                values))
        return row    
    
def run(argv=None):

    schema='Prscrbr_NPI:STRING,Prscrbr_Last_Org_Name:STRING,Prscrbr_First_Name:STRING,Prscrbr_City:STRING,Prscrbr_State_Abrvtn:STRING,Prscrbr_State_FIPS:STRING,Prscrbr_Type:STRING,Prscrbr_Type_Src:STRING,Brnd_Name:STRING,Gnrc_Name:STRING,Tot_Clms:STRING,Tot_30day_Fills:STRING,Tot_Day_Suply:STRING,Tot_Drug_Cst:STRING,Tot_Benes:STRING,GE65_Sprsn_Flag:STRING,GE65_Tot_Clms:STRING,GE65_Tot_30day_Fills:STRING,GE65_Tot_Drug_Cst:STRING,GE65_Tot_Day_Suply:STRING,GE65_Bene_Sprsn_Flag:STRING,GE65_Tot_Benes:STRING'

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--input',
        dest='input',
        required=False,
        help='Input file to read. This can be a local file or '
        'a file in a Google Storage Bucket.',
        default='gs://python-dataflow-example/data_files/head_usa_names.csv')

    parser.add_argument('--output',
                        dest='output',
                        required=False,
                        help='Output BQ table to write results to.',
                        #default='lake.usa_names')
                        default='cms_medicare_poc.cms_detailed')

    # Parse arguments from the command line.
    known_args, pipeline_args = parser.parse_known_args(argv)
    
    data_ingestion = DataTransformation()

    p = beam.Pipeline(options=PipelineOptions(pipeline_args))

    (p | 'Read from a File' >> beam.io.ReadFromText(known_args.input,
                                                  skip_header_lines=1)
     | 'String To BigQuery Row' >>
     beam.Map(lambda s: data_ingestion.parse_method(s)) |
     'Write to BigQuery' >> beam.io.Write(
         beam.io.BigQuerySink(
             known_args.output,
             schema=schema,
             create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
             write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE)))
    
    p.run().wait_until_finish()


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()