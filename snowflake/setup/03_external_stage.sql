create or replace storage integration s3_int
  type = external_stage
  storage_provider = 's3'
  enabled = true
  storage_aws_role_arn = 'arn:aws:iam::345204681263:role/snowflake_weather-cheddr-weddr-role'
  storage_allowed_locations = ('s3://weather-cheddr-weddr/raw')
  ;

desc integration s3_int;

-- storage_aws_iam_user_arn = 'arn:aws:iam::846206542736:user/3b2d1000-s'
-- storage_aws_external_id = 'SXC94440_SFCRole=4_5O2Qagj6XUKIl8/abR699NRWRDg='

use database RAW;
use schema CHEDDR_WEDDR;

create or replace stage my_s3_stage
  storage_integration = s3_int
  url = 's3://weather-cheddr-weddr/raw'
  file_format = (type = json)
;