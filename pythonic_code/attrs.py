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
