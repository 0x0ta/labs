select 
  cast('US' as varchar) as location,
  *
from
  ussales
where
  price > 50.00
union all
select
  cast('EU' as varchar) as location,
  *
from
  eusales
where
  price > 50.00