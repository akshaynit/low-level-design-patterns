## Singleton pattern

Singleton pattern is used to create classes where we want to enforce that only a single object of that class will be created even if multiple lines of codes are trying to create the object from multiple locations in the project.

## Why do we want to do that?
Great question, let's say we have a logger class in our project which is used to log messages to a file or terminal. but if someone added new code and initialized new logger what would happen? There will be another logger object doing same thing, which is redundant code and it used extra memory also.

## Follow up:
Usually we create logger once in app initialization and pass it to every method, right? In that case, we may not need to make it singleton since we are controlling the creation and passing of the object. But we can not stop someone to initialize it again, so it is still helpful. Also, a thread-safe implementation ensures even in concurrency, only a single object of logger is created.

## That's all. :)
