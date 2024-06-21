import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from sqlscriptgenerator import sql_script_generator

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

sqlscript = sql_script_generator('{"fields" : "identifier, name, security_type, exchange_code", "table_name" : "dev.public.quote_data"}')

# Script generated for node Amazon Redshift
AmazonRedshift_node1718853529753 = glueContext.create_dynamic_frame.from_options(connection_type="redshift", connection_options={"sampleQuery": sqlscript, "redshiftTmpDir": "s3://aws-glue-assets-180359220429-us-east-1/temporary/", "useConnectionProperties": "true", "connectionName": "Redshift connection"}, transformation_ctx="AmazonRedshift_node1718853529753")

# Script generated for node Amazon S3
AmazonS3_node1718854008616 = glueContext.write_dynamic_frame.from_options(frame=AmazonRedshift_node1718853529753, connection_type="s3", format="json", connection_options={"path": "s3://jw-wford-development/data-outputs/", "partitionKeys": []}, transformation_ctx="AmazonS3_node1718854008616")

job.commit()