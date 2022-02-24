# SOLID Principles
SOLID principles entail a series of good practices to achieve better quality software. SOLID stands for:  
1. S: Single responsibility  
2. O: Open Close principle  
3. L: Liskov's substitution principle  
4. I: Interface segregation principle  
5. D: Dependency Inversion Principle  

## Single Responsibility Principle
- A software component(a class or function in general) should have only one responsibility.
- A class should be in charge of doing just one concrete thing and hence it must have only one reason to change.
- Only if one thing on the domain problem changes will the class have to be updated.
- In all cases, avoid god objects i.e avoid objects with multiple responsibilities. These objects group different unrelated behaviours, thus making them harder to maintain.
- When looking at a class, if you find methods that are mutually exclusive and do not relate to each other, they are the different responsibilities and the class needs to be broken down into smaller classes.

### A class with too many responsibilities
Let us assume that a class, `SystemMonitor`, is responsible for reading information from the source(log files), identify actions corresponding to each particular log, and finally send these events to an external agent.  


| SystemMonitor      |
|--------------------|
| + load_activity()   |
| + identify_events() |
| + stream_events()   |


- The problem is that this class, i.e `SystemMonitor`, defines methods that correspond to actions that are orthogonal: each can be done independently of the rest.  
- The class is rigid and hence difficult to maintain, extend, and reuse. If we make any changes to a method, we need to modify the `SystemMonitor` class.
- The class has multiple responsibilities and each responsibility entails a reason why the class might need to be modified.

### Distributing the responsibilities
- Break each method into a separate class
![Distributing responsibilities throught classes](./images/class-breakdown.png)

- Now, each of the classes contains methods that are independent of the rest.
- Each class encapsulates a specific set of methods that are independent of the rest
- Changes to any of these classes do not impact the rest. Changes are now local, the impact is minimal, and each class is easier to maintain.
- The new classes define interfaces that are not only more maintainable but also reusable. We can now use the SystemMonitor class in a different module without importing any code related to ActivityWatcher and Output.  
- Each class may have multiple methods that correspond to the same logic.

**Note: The idea is to design software that can be easily extended and changed, and that can evolve toward a more stable version.**    

#### What are the right boundaries to separate responsibilities?

*Start writing a monolithic class, in order to understand what the internal collaborations are and how responsibilities are distributed. This will help you get a clearer picture of the new abstractions that need to be created.*  

## The Open Close Principle

Encapsulation is the bundling of data and the methods that operate on that data into a single unit. A class is a form of encapsulation. Encapsulation restricts the direct access to some components of an object.   
The open close principle states that:   

>When designing a class, for instance, we should carefully encapsulate the implementation details, so that it has good maintenance, meaning that we want it to be open to extension but closed to modification.    

- Open Close Principle, OCP, focuses on writing code that is easy to maintain and extensible.  
- When something changes in the domain problem, we want to add new changes without modifying the existing code.  

### Examples of not following the OCP  

![Design that is not closed for modification](./images/ocp_not_closed_for_modification.png)

- The above design appears extensible. Adding a new event involves creatinga  new subclass of Event class and that's it. 
    - This design isn't extensible. The identification of event is done in the `identify()` method inside the `SystemMonitor` class. The method relies on the actual implementation details of each event.

```python
@dataclass
class Event:
    raw_data: dict 
class UnknownEvent(Event):
    """A type of event that cannot be identified from its data."""
class LoginEvent(Event):
    """A event representing a user that has just entered the system."""
class LogoutEvent(Event):
    """An event representing a user that has just left the system."""
class SystemMonitor:
    """Identify events that occurred in the system."""
    def __init__(self, event_data):
        self.event_data = event_data
    def identify_event(self):
        if (
            self.event_data["before"]["session"] == 0
            and self.event_data["after"]["session"] == 1
        ):
            return LoginEvent(self.event_data)
        elif (
            self.event_data["before"]["session"] == 1
            and self.event_data["after"]["session"] == 0
        ):
            return LogoutEvent(self.event_data)
        return UnknownEvent(self.event_data)
```

- As you can see, adding a new event will require adding additional logic to the `identify()` method inside the `SystemMonitor` class.

But we want to be able to add new events without changing this method. How can we do that?  

### Refactoring the events system for extensibility  

- Issue with previous design: The `SystemMonitor` class ws interacting directly with the concrete classes.  
- To honor the OCP, we design towards abstraction.
- Delegate the logic for each particular type of event to its corresponding class   

![Design that is not closed for modification](./images/ocp_implemented_properly.png)

**Updated Code**  
```python
class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data
    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return False
class UnknownEvent(Event):
    """A type of event that cannot be identified from its data"""
class LoginEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
            event_data["before"]["session"] == 0
            and event_data["after"]["session"] == 1
        )
class LogoutEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
            event_data["before"]["session"] == 1
            and event_data["after"]["session"] == 0
        )
class SystemMonitor:
    """Identify events that occurred in the system."""
    def __init__(self, event_data):
        self.event_data = event_data
    def identify_event(self):
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meets_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                continue
        return UnknownEvent(self.event_data)

```

- Now supporting new classes only involves a new class that uses `Event` as the base class and implement its own `meets_condition()` method.  
- The above implementation now supports OCP principle.  
















