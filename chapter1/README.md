# Design Principle
---

## Identify the aspects of your application that vary and separate them from what stays the same.

Take what varies and "encapsulate" it so it won’t affect the rest of your code.
The result? Fewer unintended consequences from code changes and more flexibility in your systems!

As simple as this concept is, it forms the basis for almost every design pattern. ***All patterns provide a way to let some part of a system vary independently of all other parts.***

## Program to an interface, not an implementation.
The point is to exploit polymorphism by programming to a supertype so that the actual runtime object isn’t locked into the code.