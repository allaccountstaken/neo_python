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