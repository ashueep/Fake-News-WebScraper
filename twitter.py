import re 
import json

twt_list = {}

bodies = json.load(open('Final.json','r'))

pattern = re.compile(r'\(@.*?\)')

c = 0

for body in bodies:
    try:
        matches = pattern.findall(string = body['Body'])

        if matches is None:
            continue 

        for match in matches:
            handle = match[1:len(match) - 1]
            if handle in twt_list.keys():
                twt_list[handle] += 1
            else:
                twt_list[handle] = 1
            print(f'{handle} : {twt_list[handle]}')
    except:
        s = body['Body']
        print(f'Error in {s} : {c}')
    c += 1

with open('twt_handles.json','w') as file:
    json.dump(twt_list, file)