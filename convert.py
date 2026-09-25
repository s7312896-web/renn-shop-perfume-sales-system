sval = '123'
print(f"Before {sval} is type:{sval}")
try:
    ival = int(sval)
    print(f"After {ival} is type:{ival}")
    print(ival + 1)
except:
    print("cannot convert 'hello bob' to int")