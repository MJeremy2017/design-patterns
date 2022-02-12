# Strategy Pattern

---
> The Strategy Pattern defines a family of algorithms, 
encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently of clients that use it.


## Identify the aspects of your application that vary and separate them from what stays the same.

Take what varies and "encapsulate" it so it won’t affect the rest of your code.
The result? Fewer unintended consequences from code changes and more flexibility in your systems!

As simple as this concept is, it forms the basis for almost every design pattern. ***All patterns provide a way to let some part of a system vary independently of all other parts.***

## Program to an interface, not an implementation.
The point is to exploit polymorphism by programming to a supertype so that the actual runtime object isn’t locked into the code.

## Favor composition over inheritance.
Creating systems using composition gives you a lot more flexibility. Not only does it let you encapsulate
a family of algorithms into their own set of classes, but it also lets __you change behavior at runtime__.

With composition instead of inheritance, you can encapsulate the methods that you like instead of inherit
all of them.

> Inheritance is not the only way to REUSE!