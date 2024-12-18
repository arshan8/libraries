import time

L = range(100000)

st = time.time()
c = [i**2 for i in L]
en = time.time()
print(f"{en-st:.50f}") #use f string and :.50f to get 50 dec9mal places



# st = time.perf_counter()  RETURNS VALUE IN FRACTIONAL SECCONDS. I.E PERFORMANCE COUNTER I.E CLOCK WITH HIGHEST RESOLUTION AVIALBEL TO MEASURE SHORT TIME
# end = same ABOVE

#epoch: (when time started) platform dependend, for windows and some unix its 1970 jan 1 0:00:00
p =print(time.time())  #return float seconds after epoch
print(f"hi {p}")  #why output is None? somthing to do with print above?
print(time.ctime(5000))  #5k seconds after epoch, return type: time string
print(time.ctime())  #current time string 
# time.sleep(x) halts program for x seconds

print(time.localtime(5000))  #returns  struct time objext, 5k seconds after epoch, if no argument, it return current

q = (time.gmtime(p))   #converts time in seconds to struct rime, if no p. then after epoch
print(q)
# print(time.localtime(p))   #converts time in seconds to local time, donno whats this is.

#time.time_ns is same as time.time but returns int instead of float

print(time.asctime(q))   #converrts struct time to string