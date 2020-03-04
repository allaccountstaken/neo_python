
The Near Earth Object database is a searchable Python 3 command-line interface (CLI) project which is part of the final projects of the Intermediate Python Nanodegree by Udacity.

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

#### 1. Non-Hazardous NEOs which approached Earth between 1st and 10th January 2020
```
D:\nd303c1\starter>main.py display -n 10 --start_date 2020-01-01 --end_date 2020-01-10 --return_object NEO --filter "is_hazardous:=:False"
- 1 ----------------

NearEarthObject (2019 YH) -> [
        ID: 3942360
        Name: (2019 YH)
        Min. Diameter(km): 0.1214940408
        Hazardous: False
        Orbits:
                2020-01-08 (Miss Distance in km: 28007862.81927)
]

- 2 ----------------

NearEarthObject (2019 YF4) -> [
        ID: 3959226
        Name: (2019 YF4)
        Min. Diameter(km): 0.0105816886
        Hazardous: False
        Orbits:
                2020-01-10 (Miss Distance in km: 1427829.150964908)
                2016-08-22 (Miss Distance in km: 72389217.2223729)
]

- 3 ----------------

NearEarthObject (2020 AW2) -> [
        ID: 3985572
        Name: (2020 AW2)
        Min. Diameter(km): 0.058150704
        Hazardous: False
        Orbits:
                2020-01-08 (Miss Distance in km: 13506390.346349558)
]

Press key to continue...
```

#### 2. Non-Hazardous NEOs, with minimum diameter greater than 0.02km, which approached Earth between 1st and 10th January 2020
```
D:\nd303c1\starter>main.py display -n 10 --start_date 2020-01-01 --end_date 2020-01-10 --filter "is_hazardous:=:False" "diameter:>:0.02"
- 1 ----------------

NearEarthObject (2020 AW2) -> [
        ID: 3985572
        Name: (2020 AW2)
        Min. Diameter(km): 0.058150704
        Hazardous: False
        Orbits:
                2020-01-08 (Miss Distance in km: 13506390.346349558)
]

- 2 ----------------

NearEarthObject (2020 AL2) -> [
        ID: 3978223
        Name: (2020 AL2)
        Min. Diameter(km): 0.0201629919
        Hazardous: False
        Orbits:
                2020-01-10 (Miss Distance in km: 2383363.853898758)
]

- 3 ----------------

NearEarthObject (2019 YC4) -> [
        ID: 3959224
        Name: (2019 YC4)
        Min. Diameter(km): 0.0921626549
        Hazardous: False
        Orbits:
                2020-01-08 (Miss Distance in km: 41823402.10070427)
]

Press key to continue...
```

#### 3. Non Hazardous NEOs, with minimum diameter greater than 0.02km and a miss distance greater than or equal to 50000, which approached Earth between 1st and 10th January 2020
```
D:\nd303c1\starter>main.py display -n 10 --start_date 2020-01-01 --end_date 2020-01-10 --filter "is_hazardous:=:False" "diameter:>:0.02" "distance:>=:50000"
- 1 ----------------

NearEarthObject (2020 AW2) -> [
        ID: 3985572
        Name: (2020 AW2)
        Min. Diameter(km): 0.058150704
        Hazardous: False
        Orbits:
                2020-01-08 (Miss Distance in km: 13506390.346349558)
]

- 2 ----------------

NearEarthObject (2020 AL2) -> [
        ID: 3978223
        Name: (2020 AL2)
        Min. Diameter(km): 0.0201629919
        Hazardous: False
        Orbits:
                2020-01-10 (Miss Distance in km: 2383363.853898758)
]

- 3 ----------------

NearEarthObject (2019 YC4) -> [
        ID: 3959224
        Name: (2019 YC4)
        Min. Diameter(km): 0.0921626549
        Hazardous: False
        Orbits:
                2020-01-08 (Miss Distance in km: 41823402.10070427)
]

Press key to continue...
```

#### 4. Hazardous NEOs, with minimum diameter greater than 0.02km and a miss distance greater than or equal to 50000, which approached Earth between 1st and 10th January 2020
```
D:\nd303c1\starter>main.py display -n 10 --start_date 2020-01-01 --end_date 2020-01-10 --filter "is_hazardous:=:True" "diameter:>:0.02" "distance:>=:50000"
- 1 ----------------

NearEarthObject (2008 LW16) -> [
        ID: 3414251
        Name: (2008 LW16)
        Min. Diameter(km): 0.2658
        Hazardous: True
        Orbits:
                2020-01-04 (Miss Distance in km: 16984671.826704316)
                2019-07-03 (Miss Distance in km: 25973986.02363487)
]

- 2 ----------------

NearEarthObject (2019 WD5) -> [
        ID: 3893736
        Name: (2019 WD5)
        Min. Diameter(km): 0.1160259082
        Hazardous: True
        Orbits:
                2020-01-06 (Miss Distance in km: 8905752.461976795)
]

- 3 ----------------

NearEarthObject 416591 (2004 LC2) -> [
        ID: 2416591
        Name: 416591 (2004 LC2)
        Min. Diameter(km): 0.5303407233
        Hazardous: True
        Orbits:
                2020-01-02 (Miss Distance in km: 30662108.158951942)
]

Press key to continue...
```
