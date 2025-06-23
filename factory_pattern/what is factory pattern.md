## Factory pattern:
We separate the object creation to some centralized place. The code which wants the objects calls this centralized place to get the object and use it's methods.


## Why do we need it?
### Intuition:
Suppose we are creating some objects at muliple places in the project and then using their methods. Those objects are of some type and we are creating objects based on that type using some logic at every one of these places. This logic of creation is duplicated at all of these places.
Why don't we write some method that takes this type as input and give me the object I want? And at all of those places we just call this method to get the required object and then use it's methods. Great! this is factory pattern.

## What did we gain?
- Code to create objects based on their type is now at single place. So, we avoided writing it at multiple places in the project.
- If some new class is getting added and we need to use that class's object also, then we can update our central method to create the new class object, and that's it. So the changes are minimized now, because earlier we would have to add this new class object creation at muliple places.
