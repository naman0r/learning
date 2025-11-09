package mcv;

public class TodoController implements IController{
  // needs to have a readable (the console)
  // an appendable (the 'view'
  // i lied just need access ot a view and model
  private final IView view;
  private final ITodoList todolist;

  public TodoController(IView view, ITodoList list) {
    this.view = view;
    this.todolist = list;
  }



  public void run() { // takes in no args

    System.out.println("Hi! Welcome to this simple MVC Todolist app");
    System.out.println("-------");
    while (true) {
      String input = view.getInput();
      view.show("---");
      // this could be a switch statement
      if (input == "q") { // exit clause
        view.show("Goodbye!");
        break;
      }
      else if (input.startsWith("add")) {
          this.todolist.addTask(input.replace("add", "").trim());
          view.show("Task added" + input.replace("add", "").trim() + "!!!");
      }
      else if (input.equals("clear")) {
        this.todolist.clearTasks();
      }

      else if (input.equals("list")) {
        // this just lists everything in the model
        this.view.show(this.todolist.getTasks());
      }
      else {
        view.show("Invalid input :"+  input);
      }

    }

  }
}
