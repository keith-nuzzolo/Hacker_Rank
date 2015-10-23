'''
You are given time in AM/PM format. Convert this into a 24 hour format.

SAMPLE INPUT:
07:05:45PM
'''
def convert(time):
    ''' takes string that was inputed and turn it into 24 hour clock
    '''
    hh = time[0:2]
    mm = time[3:5]
    ss = time[6:8]

    if 'AM' in time:
        if '12' in hh:
            hh = '00'
    elif 'PM' in time:
        if '12' in hh:
            pass
        else:
            hh = int(hh)
            hh += 12
            hh = str(hh)
    return ('%s:%s:%s')%(hh,mm,ss)
print (convert(input()))
