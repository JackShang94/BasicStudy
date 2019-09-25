#API Demonstration - Consuming API
#Carpark Availability - https://data.gov.sg/dataset/carpark-availability

#Note: Need to run 'pip install requests' from Windows command line(cmd). 
import requests
import json

carpark_data =[]
response = requests.get('https://api.data.gov.sg/v1/transport/carpark-availability')

if response.status_code != 200:
    # This means something went wrong.
    print('Something went wrong!')
else:
    data= json.loads(response.content.decode('utf-8'))
    
    for carpark in data['items'][0]['carpark_data']:
        number=carpark['carpark_number']
        total_lots=int(carpark['carpark_info'][0]['total_lots'])
        lots_available=int(carpark['carpark_info'][0]['lots_available'])
        carpark_data.append([number,total_lots,lots_available])

#Display carparks with more than 100 total lots and no available lots        
for info in carpark_data:
    if info[1]>100 and info[2]==0:
        print('Code:{:<8}Total:{:<6}Available:{:<6}'.format(info[0],info[1],info[2]))

#Question: What does the above displayed result suggest?
        
