# Rusia

This one wasn't very hard. First I defined a list of tuples that included each router's position and range and then another list with the routers to be queried. Then the program goes for each one of this queries, first get's the queried router (position and range), and then it goes for each router, first checking if it's the same router and then (if it's not the same) it checks if that router's range (the whole range from it's position and the range first substracted and then added) is inside the original router's range. Then it just adds each one that is in position and returns the value of routers in range for each query.

Given that it's not that big of a query and there are not so many routers, this challenge could be easily solved with pen and paper. It would, however be pretty boring that way.

## Answer

4400444444