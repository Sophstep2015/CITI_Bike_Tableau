filenames = ['202001-citibike-tripdata.csv', '202002-citibike-tripdata.csv', '202003-citibike-tripdata.csv', '202004-citibike-tripdata.csv', '202005-citibike-tripdata.csv', '202006-citibike-tripdata.csv', '202007-citibike-tripdata.csv', '202008-citibike-tripdata.csv', '202009-citibike-tripdata.csv', '202010-citibike-tripdata.csv', '202011-citibike-tripdata.csv', '202012-citibike-tripdata.csv' ]
with open('2020new.csv', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())