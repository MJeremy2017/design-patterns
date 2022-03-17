# Command Pattern

> The Command Pattern encapsulates a request as an object, thereby letting you parameterize other
> objects with different requests, queue or log requests, and support undoable operations.

A command object encapsulates a request by binding together a set of actions on a specific receiver. To achieve this, it
packages the actions and the receiver up into an object that exposes just one method, `execute()`. When
called, `execute()` causes the actions to be invoked on the receiver.

From the outside, no other objects really know what actions get performed on what receiver; they just know that if they
call the `execute()` method, their request will be serviced.

![img.png](../images/img.png)

### When to Use?
When you need to decouple an object making requests from the objects that know how to perform the requests, use the
Command Pattern.
> It wraps different requests in a common interface called Command, thus enables the decoupling between the invoker
> and the receiver.

## Examples

### Job Queue

Imagine a job queue: you add commands to the queue on one end, and on the other end sit a group of threads. Threads run
the following script: they remove a command from the queue, call its execute() method, wait for the call to finish, then
discard the command object and retrieve a new one.

### System Logging

The semantics of some applications require that we log all actions and be able to recover after a crash by re-invoking
those actions. The Command Pattern can support these semantics with the addition of two methods: store() and load().

How does this work? As we execute commands, we(invoker) store a history of them on disk. When a crash occurs, we reload
the command objects and invoke their execute() methods in batch and in order.
