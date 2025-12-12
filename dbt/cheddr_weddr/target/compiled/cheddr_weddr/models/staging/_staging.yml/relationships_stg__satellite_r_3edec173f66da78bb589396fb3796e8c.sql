
    
    

with child as (
    select location_id as from_field
    from DEV.CHEDDR_WEDDR.stg__satellite_radiation
    where location_id is not null
),

parent as (
    select location_id as to_field
    from DEV.CHEDDR_WEDDR.seed__locations
)

select
    from_field

from child
left join parent
    on child.from_field = parent.to_field

where parent.to_field is null


