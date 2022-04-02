# Iterator Pattern

> The Iterator Pattern allows traversal of the elements of an aggregate without exposing the underlying implementation.

It also places the task of traversal on the iterator object, not on the aggregate, which simplifies the aggregate
interface and implementation, and places the responsibility where it should be.

This not only keeps the aggregate interface and implementation simpler, it removes the responsibility for iteration from
the aggregate and keeps the aggregate focused on the things it should be focused on (managing a collection of objects),
not on iteration.

__Design Principle__

```
A class should have only one reason to change.
```

Every responsibility of a class is an area of potential change. More than one responsibility means more than one area of
change.

This principle guides us to keep each class to a __single responsibility__.

> The Composite Pattern allows you to compose objects into tree structures to represent part-whole hierarchies. 
> Composite lets clients treat individual objects and compositions of objects uniformly.
 
Compose objects into tree structures to represent part-whole hierarchies. 
Composite lets clients treat individual objects and compositions of objects uniformly

