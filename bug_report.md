# BUG FIXES

### Error with NEO and OrbitPath attributes

###### Issue: 

Initially implemented instance variables with arbitrary names, and these caused errors as test cases were 
using predefined variables like `.diameter_min_km` and `.is_potentially_hazardous_asteroid`.

###### Resolution:

Changed instance variables to be same as those defined in tests. The update can be verified here: https://github.com/ayivima/neo_python/commit/dac040a285086b9b58eba7a0c0085f7b98d02931


### Query object had empty filters

###### Issue: 

Testing my `Query.build_query` returned an object with no filters even though filters had been provided. 

###### Resolution:

I had set the `filter` instance variable to reference the `return_object` argument from `kwargs`. 
I changed it to reference the `filter` argument from `kwargs`. https://github.com/ayivima/neo_python/commit/4c2bedccc88e67f1d5d6baf3c279ae0584011d99


### Unbound Local Error

###### Issue: 

There was an error which referred to using filter_dict before it had been assigned. 

###### Resolution:

This was a bit strange. But I resolved it by initially assigning `filter_dict` to an empty set before assigning it to the output of `Filter.create_filter_options`. https://github.com/ayivima/neo_python/commit/42618a6dcbb736f504b98656ccb92f8a5e5fa7e8


### Error in accessing Filters from Query

###### Issue
Error message was that `query.filters` had no method get, even though it is supposed to be a `defaultdict`.

###### Resolution
+ Checked whether `Query.filters` was empty, in which case it contained an empty set. If it was empty there wouldn't be an attempt to get filters.

+ In `Filter.create_filter_options`, if a NearEarthObject or OrbitPath didn't have filters, the respective keys would contain an empty list. 

https://github.com/ayivima/neo_python/commit/ca52eb4af3b87b1ea2ebfa00af90e2d4f17a46bc


### NEOSearcher.get_objects always returning None

###### Issue
NEOSearcher.get_objects always returning None. I identified that the return object identifiers i provided were `NearEarthObject` and `OrbitPath`.

###### Resolution
Implemented checks for equality between `Query.return_object` and `NearEarthObject` and `OrbitPath` objects.

https://github.com/ayivima/neo_python/commit/c7c834e7a65dcbde7f687e7fe41d9a4f70d16009
