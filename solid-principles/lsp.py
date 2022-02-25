from abc import ABCMeta, abstractmethod


class XMLEventParser(metaclass=ABCMeta):
    @abstractmethod
    def from_xml(xml_data):
        "Parse an event from a source in XML representation."


class JSONEventParser(metaclass=ABCMeta):
    @abstractmethod
    def from_json(json_data: str):
        "Parse an event from a source in JSON representation."


class EventParser(XMLEventParser, JSONEventParser):
    """This will cause error because this class doesn't implement the method defined by the interface"""

    def from_json(xml_data):
        pass

    def from_json(json_data: str):
        pass
