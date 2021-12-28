# SOLID Principles
SOLID principles entail a series of good practices to achieve better quality software. SOLID stands for:  
1. S: Single responsibility  
2. O: Open Close principle  
3. L: Liskov's substitution principle  
4. I: Interface segregation principle  
5. D: Dependency Inversion Principle  

## Single Responsibility Principle
- A software comoponent(a class or function in general) should have only one responsibility.
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
To make the solution more maintainable, we break down each method in the previous class into a spearate class.
![Distributing responsibilities throught classes](./images/class-breakdown.png)

- Now, each of the classes contains methods that are independent of the rest.
- Changes to any of these classes do not impact the rest. Changes are now local, the impact is minimal, and each class is easier to maintain.
- The new classes define interfaces that are not only more maintainable but also reusable.  

**What are the right boundaries to separate responsibilities?**  
Start writing a monolithic class, in order to understand what the internal collaborations are and how responsibilities are distributed. This will help you get a clearer picture of the new abstractions that need to be created.




