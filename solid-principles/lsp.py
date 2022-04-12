from abc import ABCMeta, abstractmethod


class XMLEventParser(metaclass=ABCMeta):
    @abstractmethod
    def from_xml(self):
        "Parse an event from a source in XML representation."


class JSONEventParser(metaclass=ABCMeta):
    @abstractmethod
    def from_json(self):
        "Parse an event from a source in JSON representation."


class EventParser(XMLEventParser, JSONEventParser):
    """This will cause error because this class doesn't implement the method defined by the interface"""

    def from_json(self):
        pass

    def from_json(self):
        pass
