use role accountadmin;

-- Storage integration
CREATE OR REPLACE STORAGE INTEGRATION S3_INT
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = 'S3'
ENABLED = TRUE
-- STORAGE_AWS_ROLE_ARN = <iam_role_arn>
STORAGE_ALLOWED_LOCATIONS = ('s3://<bucket>/<prefix>/');
desc INTEGRATION S3_INT;

-- create a database
create or replace database snowpipe;

-- create a stage
create or replace stage snowpipe.public.snowstage
url = 's3://<bucket>/<prefix>/'
storage_integration = S3_INT;
show stages;

-- create target table for json data
create or replace table snowpipe.public.snowtable(jsontext variant);

-- create the pipe
create or replace pipe snowpipe.public.snowpipe auto_ingest=true as
copy into snowpipe.public.snowtable
from @snowpipe.public.snowstage
file_format = (type = 'JSON');
show pipes;

-- check pipe status
select SYSTEM$pipe_status('snowpipe.public.snowpipe');

-- data in table
select * from snowpipe.public.snowtable;

select * from table(information_schema.copy_history(table_name=>'snowpipe.public.snowtable', start_time=>dateadd(hours, -1, current_timestamp())));
