from rpiatipo.Events import EventService, Event

def create():
    eventService = EventService()
    event = Event(type="weather", data={"temp": 10})
    response = eventService.create(event)
    print(response)

def getId():
    eventService = EventService()
    event = eventService.getId("5b0f95a36a520537e83a199a")
    print(event)

def getType():
    eventService = EventService()
    events = eventService.getType(type="weather", page=0, size=5)
    print(events)

#create()
#getId()
getType()