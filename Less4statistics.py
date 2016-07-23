# API to calculate basic statistics
# 7/23/16

def mean(L):
    #return float(sum(L)/len(L)) if len(L) > 1 else float('nan')
    return (0.0+sum(L)/len(L))

def my_min(L):
    #L.sort()
    #return L[0]
    min = L[0]
    for x in range(1,len(L)):
        if x < min:
            min = x
    return min

def my_max(L):
    #L.sort()
    #return L[len(L)-1]
    max = L[0]
    for x in range(1, len(L)):
        if x > max:
            max = x
    return max

def median(L):
    L.sort()
    return L[len(L)/2]

def midpoint(L):
    L.sort()
    return float((L[0] + L[len(L)-1])/2)

def mode(L):
    mode = L[0]
    freq = frequency(L)
    for numb in freq:
        if freq[numb] > mode:
            mode = numb
            
    return numb

def frequency(L):
    freq = dict((numb, 0) for numb in L)
    
    for x in freq:
        freq[x] = freq[x] + 1
        
    return freq

# def sec_frequency(freq):
#     most = (freq.keys()[0], freq.values()[0])
#     sec = ('', 0)
#     
#     for x in freq.keys():
#         if freq[x] > most[1]:
#             sec = most
#             most = (x, freq[x])
#         elif freq[x] < most[1]  and freq[x] > sec[1]:
#             sec = (x, freq[x])
#             
#         
#     return sec

def sec_freq_name():
    max = 0
    maxName = ''
    secMax = 0
    secMaxName = ''
    with open("yob1995.txt") as f:
        for line in f:
            (name, sex, freq) = line.split(',')
            freq = int(freq)
            if sex == 'F':
                if freq > max:
                    secMax = max
                    secMaxName = maxName
                    max = freq
                    maxName = name
                elif freq > secMax:
                    secMax = freq
                    secMaxName = name
            #names[key] = int(freq)
    return (secMaxName, secMax)
    
# L = [21,43,48,49,50,51,75,77,79,87,93]
# 
# mid = midpoint(L)
# med = median(L)
# print 'midpoint: ', mid
# print 'medain: ', med
# print 'mean: ', mean([mid, med])

# names = {}
# with open("yob1995.txt") as f:
#     for line in f:
#         (key, sex, freq) = line.split(',')
#         if sex == 'F':
#             names[key] = int(freq)
# print sec_frequency(names)

print sec_freq_name()
