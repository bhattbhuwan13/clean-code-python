class Connector:
    def __init__(self, source):
        self.source = source
        self.__timeout = 60

    def connect(self):
        print("Connecting with {}".format(self.source))

conn = Connector('postgres')

conn.connect()

print(vars(conn))
print(conn._Connector__timeout) # to access the attributes with leading double underscores
    # we can use _<Class-name>__<attribute-name>

class Coordinate:
    def __init__(self, lat: float, long: float):
        self._latitude = self._longitude = None
        self.latitude = lat
        self.longitude = long

    @property
    def latitude(self) -> float:
        return self._latitude
    
    @latitude.setter
    def latitude(self, lat_value: float) -> None:
        if lat_value not in range(-90, 90+l):
            raise ValueError(f"{lat_value} is an invalid value for latitude")
        self._latitude = lat_value

    @property
    def longitude(self) -> float:
        return self._longitude

    @longitude.setter
    def longitude(self, long_value: float) -> None:
        if lat_value not in range(-180, 180+l):
            raise ValueError(f"{long_value} is an invalid value for longitude")
        self._longitude = long_value

