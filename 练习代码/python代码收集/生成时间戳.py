def get_timestamp(start_end,trade_in_one_second):
    timestamp=[]
    for index in xrange(len(start_end)):
        [start_h,start_m,start_s]=start_end[index][0].split(':')
        [end_h,end_m,end_s]=start_end[index][1].split(':')
        start_temp_date=datetime.datetime(100,1,1,int(start_h),int(start_m),int(start_s))
        end_temp_date=datetime.datetime(100,1,1,int(end_h),int(end_m),int(end_s))
        temp_datetime=start_temp_date
        while temp_datetime<=end_temp_date:
            for i in xrange(trade_in_one_second):
                timestamp.append(str(temp_datetime.time()))
            temp_datetime=temp_datetime+datetime.timedelta(seconds=1)
    return timestamp
