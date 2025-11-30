CREATE OR REPLACE STORAGE INTEGRATION s3_int
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = 'S3'
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::345204681263:role/snowflake_weather-cheddr-weddr-role'
  STORAGE_ALLOWED_LOCATIONS = ('s3://weather-cheddr-weddr/raw')
  ;

DESC INTEGRATION s3_int;

-- STORAGE_AWS_IAM_USER_ARN = 'arn:aws:iam::557702682990:user/x9g81000-s'
-- STORAGE_AWS_EXTERNAL_ID = 'AA85900_SFCRole=5_iLWgJ2SKDOgfJuj+owLoHClfVEo='

use database raw;
use schema cheddr_weddr;

CREATE OR REPLACE STAGE my_s3_stage
  STORAGE_INTEGRATION = s3_int
  URL = 's3://weather-cheddr-weddr/raw'
  FILE_FORMAT = (type = json)
;