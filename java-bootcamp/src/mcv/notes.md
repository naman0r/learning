# These are my notes on MVC

## Overview

MVC (Model-View-Controller) is a widely used architectural pattern in Java for designing user interfaces and organizing code by dividing an application into three interconnected components. This separation of concerns aids in reducing code complexity, increasing modularity, and improving maintainability and scalability.

## Core Components

### Model

- Represents the **data** and defines the **business logic** of the application.
- Responsible for:
    - Managing application data.
    - Handling rules/validation and state changes.
    - Interfacing with databases or data storage.
    - Notifying the view (and sometimes the controller) when data changes.
- Example:

```java
public class Student {
  private String name;
  private String rollNo;


  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public String getRollNo() {
    return rollNo;
  }

  public void setRollNo(String rollNo) {
    this.rollNo = rollNo;
  }
}
```


### View

- Represents the **presentation layer** – the user interface that displays data to the user.
- Responsible for:
- Rendering data from the model in a user-friendly format.
- Collecting user input (typically through UI controls).
- Sending user actions to the controller for processing.
- Example:



```java
public class StudentView {
  public void printStudentDetails(String studentName, String studentRollNo) {
    System.out.println("Student:");
    System.out.println("Name: " + studentName);
    System.out.println("Roll No: " + studentRollNo);
  }
}
```


### Controller

- Acts as the **intermediary** between Model and View.
- Responsible for:
- Receiving inputs from the View.
- Processing/validating user input and updating the Model accordingly.
- Refreshing the View to reflect the updated state of the Model.
- Coordinating application workflow.
- Example:



```java
public class StudentController {
  private Student model;
  private StudentView view;


  public StudentController(Student model, StudentView view) {
    this.model = model;
    this.view = view;
  }

  public void setStudentName(String name) {
    model.setName(name);
  }

  public String getStudentName() {
    return model.getName();
  }

  public void setStudentRollNo(String rollNo) {
    model.setRollNo(rollNo);
  }

  public String getStudentRollNo() {
    return model.getRollNo();
  }

  public void updateView() {
    view.printStudentDetails(model.getName(), model.getRollNo());
  }
}
```


## MVC Flow and Interactions

1. **User interacts with the View:** Example – clicks a button or enters data.
2. **View sends input to Controller:** The View passes user actions to the Controller.
3. **Controller processes input:** Controller interprets input, updates Model, or makes decisions.
4. **Model updates data/state:** If needed, Model state changes and may notify View.
5. **View updates UI:** View requests updated data from Model to refresh the user interface.

This workflow enforces a **clear separation of concerns**, where changes in business logic (Model) do not force changes in UI (View), and vice versa.

## Example: Putting It All Together



