-- Write your query below
select 
    left_operand, 
    operator, 
    right_operand, 
    case 
        when operator = '<'
        then  left_value < right_value
        when operator = '='
        then  left_value = right_value
        when operator = '>'
        then left_value > right_value
    end as "value"
from (select v.value as left_value, vv.value as right_value, left_operand, operator, right_operand
from expressions e
left join variables v
on e.left_operand = v.name
left join variables vv
on e.right_operand = vv.name
)
