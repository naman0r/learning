## Some OO style questions I should prepare for



1. Can you explain the difference between an abstract class and an interface in Java?
- An abstract class is a class that cannot be instantiated and may contain both abstract methods (without implementation) and concrete methods (with implementation). It's declared using the abstract keyword.
```java
abstract class Animal {
    String name;
    
    // Concrete method
    public void sleep() {
        System.out.println("Sleeping...");
    }
    
    // Abstract method
    abstract void makeSound();
}
```
- An interface is a contract that specifies what methods a class must implement, but traditionally didn't provide implementations (though Java 8+ added default and static methods). It's declared using the interface keyword.
```java
interface Flyable {
    void fly();  // Implicitly public and abstract
    
    // Java 8+ allows default methods
    default void glide() {
        System.out.println("Gliding...");
    }
}
```
* differences: 
  * Inheritance: A class can extend only one abstract class (single inheritance), but can implement multiple interfaces.
  * Constructors: Abstract classes can have constructors. Interfaces cannot.
  * Use case: Use abstract classes when classes share common code and have an "is-a" relationship. Use interfaces when you want to define a capability that unrelated classes can share (like a "can-do" relationship).


2. 4 pillars of OOPs:
- encapsulation (bundling fields into an object)
- Abstraction (hiding complex implementation details and showing only essential features)
- Inheritance (A mechanism where a new class (child/subclass) inherits properties and behaviors from an existing class (parent/superclass). This promotes code reusability)
- Polymorphism (the ability of an object to take multiple forms. the same method name can behave differently based on the object calling it.)

