
def get_days(month):
  days = 30
  if(month == 2):
    days = 28
  elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    days = 31
  else:
    days = 30
  return (days)


  


def findAge(start_day, start_month, start_year):
  end_day = 20
  end_mon = 04
  end_year = 2015

  res_year  = end_year- start_year
  res_mon = 0
  res_day = 0
  
  if(end_mon >= start_month):
    res_mon = end_mon - start_month
  else:
    res_mon = end_mon - start_month
    res_mon = res_mon + 12
    res_year = res_year - 1
  if(end_day < start_day):
    res_mon = res_mon - 1
  
  

  if(end_day >= start_day):
    res_day = end_day - start_day
  else:
    prev_mon = end_mon - 1
    if(prev_mon == 0):
      prev_mon = 12
    res_day = end_day + get_days(prev_mon) - start_day

    

  print("Years: "+ str(res_year) + " Months: "+ str(res_mon)+" Days: "+ str(res_day))
 
  




#findAge(19, 02, 1978)
#findAge(7, 9, 1982)
#findAge(20, 8, 2009)
findAge(5,1, 2010)





