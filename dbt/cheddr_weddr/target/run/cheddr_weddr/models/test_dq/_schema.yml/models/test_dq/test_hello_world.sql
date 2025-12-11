-- Build actual result given inputs
with dbt_internal_unit_test_actual as (
  select
    "HELLO", 'actual' as "actual_or_expected"
  from (
    select 'world' as hello
  ) _dbt_internal_unit_test_actual
),
-- Build expected result
dbt_internal_unit_test_expected as (
  select
    "HELLO", 'expected' as "actual_or_expected"
  from (
    select 
    
        try_cast('world' as character varying(5))
     as "HELLO"
  ) _dbt_internal_unit_test_expected
)
-- Union actual and expected results
select * from dbt_internal_unit_test_actual
union all
select * from dbt_internal_unit_test_expected