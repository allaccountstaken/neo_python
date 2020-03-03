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
