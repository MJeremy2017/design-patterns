# Decorator Pattern

The Decorator Pattern attaches additional responsibilities to an object dynamically. 
Decorators provide a flexible alternative to subclassing for extending functionality.

Don’t alter interface, but add responsibility

## Classes should be open for extension, but closed for modification.
Our goal is to allow classes to be easily extended to incorporate new behavior without 
modifying existing code. Decorator adds a wrapping on top of another without changing the interior code.
> Decorators are meant to add behavior to the object they wrap.

There are two key concepts in this pattern, `componet` and `decorator`. 
- The Decorator Pattern involves a set of `decorator` classes that are used to wrap `concrete components`.
- Decorator classes mirror the type of the components they decorate. (In fact, they are the same type as the components they decorate, either through inheritance or interface implementation.)
- Decorators change the behavior of their components by adding new functionality before and/or after (or even in place of) method calls to the component.

Example of `jave.io` classes

![ps](https://github.com/MJeremy2017/design-patterns/blob/master/images/decorator.png?raw=true)


## Downside

The downsides of the Decorator Pattern: designs using this pattern often result in a large number of small 
classes that can be overwhelming to a developer trying to use the Decorator-based API.