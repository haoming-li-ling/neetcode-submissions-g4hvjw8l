-- Write your query below
select 
    e.left_operand, 
    e.operator, 
    e.right_operand, 
    case e.operator
        when '<'
        then lv.value < rv.value
        when '='
        then lv.value = rv.value
        when '>'
        then lv.value > rv.value
    end as "value"
from expressions e
left join variables lv
on e.left_operand = lv.name
left join variables rv
on e.right_operand = rv.name
