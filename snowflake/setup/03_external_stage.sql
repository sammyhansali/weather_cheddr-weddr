create or replace storage integration s3_int
  type = external_stage
  storage_provider = 's3'
  enabled = true
  storage_aws_role_arn = 'arn:aws:iam::345204681263:role/snowflake_weather-cheddr-weddr-role'
  storage_allowed_locations = ('s3://weather-cheddr-weddr/raw')
  ;

desc integration s3_int;

-- storage_aws_iam_user_arn = 'arn:aws:iam::953751537377:user/01ve1000-s'
-- storage_aws_external_id = 'RWC99468_SFCRole=2_qR5sl1LQQo/iQqSBY0wryIGAlS8='

use database RAW;
use schema CHEDDR_WEDDR;

create or replace stage my_s3_stage
  storage_integration = s3_int
  url = 's3://weather-cheddr-weddr/raw'
  file_format = (type = json)
;