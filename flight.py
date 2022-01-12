schedule1={
    'id': 'JT922',
    'Origin': 'Surabaya',
    'Destination': 'Denpasar',
    'Departure': '12:30',
    'Arrival': '14:25',
    'Date' : '13-01-2021'
}
schedule2={
    'id': 'JT337',
    'Origin': 'Palembang',
    'Destination': 'Jakarta',
    'Departure': '18:45',
    'Arrival': '19:50',
    'Date' : '13-01-2021'
}
schedule3={
    'id': 'JT229',
    'Origin': 'Batam',
    'Destination': 'Padang',
    'Departure': '14:20',
    'Arrival': '15:30',
    'Date' : '14-01-2021'
}
schedule4={
    'id': 'JT569',
    'Origin': 'Denpasar',
    'Destination': 'Yogyakarta',
    'Departure': '12:30',
    'Arrival': '12:55',
    'Date' : '14-01-2021'
}
schedule5={
    'id': 'JT12',
    'Origin': 'Jakarta',
    'Destination': 'Denpasar',
    'Departure': '12:00',
    'Arrival': '14:50',
    'Date' : '14-01-2021'
}

def returnSchedule(id):
    switcher = {
        1 : schedule1,
        2 : schedule2,
        3 : schedule3,
        4 : schedule4,
        5 : schedule5
    }
    return switcher.get(id, "Invalid Schedule ID")
def showSchedule(id):
    sched = returnSchedule(id)
    print('-------------- Schedule ', id, '--------------')
    print('Flight ID    : ', sched['id'])
    print('Origin       : ', sched['Origin'])
    print('Destination  : ', sched['Destination'])
    print('Departure    : ', sched['Departure'])
    print('Arrival      : ', sched['Arrival'])
    print('Date         : ', sched['Date'])
    
def showAllSchedule():
    for i in range (1, 6):
        sched = returnSchedule(i)
        print('-------------- Schedule ', i, '--------------')
        print('Flight ID    : ', sched['id'])
        print('Origin       : ', sched['Origin'])
        print('Destination  : ', sched['Destination'])
        print('Departure    : ', sched['Departure'])
        print('Arrival      : ', sched['Arrival'])
        print('Date         : ', sched['Date'])