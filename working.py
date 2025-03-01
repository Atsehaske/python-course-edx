import re
import sys

def main():
    ''' main function '''
    print(convert(input("Hours: ")))

def validate(s):
    ''' validates input '''
    if hours:=re.search(r'([0-9][0-2]?):?([0-5][0-9])? (AM|PM)? to ([0-9][0-2]?):?([0-5][0-9])? (AM|PM)?', s):
        if int(hours.group(1)) > 12 or int(hours.group(4)) > 12:
            raise ValueError
    else:
            raise ValueError
    
    return hours

def h12_to_h24(h, m, t):
    ''' returns formatted time '''
    if t == 'AM':
        if h == 12:
            h = 0
    else:
        if h != 12:
            h += 12
    if m == None:
        m = '00'
    result = f"{h:02}"+":"+str(m)
    return result

def convert(s):
    ''' converts 12h to 24h '''
    s = s.strip()
    hours = validate(s)

    h1 = h12_to_h24(int(hours.group(1)), hours.group(2), hours.group(3))
    h2 = h12_to_h24(int(hours.group(4)), hours.group(5), hours.group(6))

    return h1+' to '+h2


if __name__ == "__main__":
    main()
