
# TEST OUTCOMES
```
D:\nd303c1\starter>python test_neo_database.py
test_find_unique_number_between_dates (__main__.TestNEOSearchUseCases) ... ok
test_find_unique_number_between_dates_with_diameter (__main__.TestNEOSearchUseCases) ... ok
test_find_unique_number_between_dates_with_diameter_and_hazardous (__main__.TestNEOSearchUseCases) ... ok
test_find_unique_number_between_dates_with_diameter_and_hazardous_and_distance (__main__.TestNEOSearchUseCases) ... ok
test_find_unique_number_neos_on_date (__main__.TestNEOSearchUseCases) ... ok
test_find_unique_number_neos_on_date_with_diameter (__main__.TestNEOSearchUseCases) ... ok
test_find_unique_number_neos_on_date_with_diameter_and_hazardous (__main__.TestNEOSearchUseCases) ... ok
test_find_unique_number_neos_on_date_with_diameter_and_hazardous_and_distance (__main__.TestNEOSearchUseCases) ... ok

----------------------------------------------------------------------
Ran 8 tests in 14.475s

OK
```

# DEMONSTRATION

#### 1. NEOs which approached Earth between 1st and 10th January 2020
```
D:\nd303c1\starter>main.py display -n 10 --start_date 2020-01-01 --end_date 2020-01-10 --return_object NEO --filter "is_hazardous:=:False"
- 1 ----------------

NearEarthObject (2019 WD5) -> [
        ID: 3893736
        Name: (2019 WD5)
        Min. Diameter(km): 0.1160259082
        Orbits:
                2020-01-06 (Miss Distance in km: 8905752.461976795)
]

- 2 ----------------

NearEarthObject 416591 (2004 LC2) -> [
        ID: 2416591
        Name: 416591 (2004 LC2)
        Min. Diameter(km): 0.5303407233
        Orbits:
                2020-01-02 (Miss Distance in km: 30662108.158951942)
]

- 3 ----------------

NearEarthObject (2012 BU61) -> [
        ID: 3596491
        Name: (2012 BU61)
        Min. Diameter(km): 0.1332155667
        Orbits:
                2020-01-05 (Miss Distance in km: 14950560.117533928)
]

Press key to continue...
```
