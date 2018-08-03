Run the data in RStudio by selecting Project.R

It is adivsed you clear the workspace, select all and run to see the results

(Note that results for mapreduce is outputed as null because of % in datasets)

Running Mapper & Reducer on the election dataset

`cd C:\R Analysis of 2016 US Elections`
`type C:\R Analysis of 2016 US Elections\election.csv`
`type C:\R Analysis of 2016 US Elections\election.csv | C:\R Analysis of 2016 US Elections\topTenStatesMapper.py`
`type C:\R Analysis of 2016 US Elections\election.csv | C:\R Analysis of 2016 US Elections\topTenStatesMapper.py | sort`
`type C:\R Analysis of 2016 US Elections\election.csv | C:\R Analysis of 2016 US Elections\topTenStatesMapper.py | sort | C:\R Analysis of 2016 US Elections\topTenStatesReducer.py`
`type C:\R Analysis of 2016 US Elections\election.csv | C:\R Analysis of 2016 US Elections\topTenStatesMapper.py | sort | C:\R Analysis of 2016 US Elections\topTenStatesReducer.py >> C:\R Analysis of 2016 US Elections\TopTenElection.txt`

Running Mapper & Reducer on the election dataset

`cd C:\R Analysis of 2016 US Elections
type C:\R Analysis of 2016 US Elections\primaries.csv 
type C:\R Analysis of 2016 US Elections\primaries.csv | C:\R Analysis of 2016 US Elections\topTenStatesMapper.py 
type C:\R Analysis of 2016 US Elections\primaries.csv | C:\R Analysis of 2016 US Elections\topTenStatesMapper.py | sort 
type C:\R Analysis of 2016 US Elections\primaries.csv | C:\R Analysis of 2016 US Elections\topTenStatesMapper.py | sort | C:\R Analysis of 2016 US Elections\topTenStatesReducer.py 
type C:\R Analysis of 2016 US Elections\primaries.csv | C:\R Analysis of 2016 US Elections\topTenStatesMapper.py | sort | C:\R Analysis of 2016 US Elections\topTenStatesReducer.py >> C:\R Analysis of 2016 US Elections\TopTenPrimaries.txt`
