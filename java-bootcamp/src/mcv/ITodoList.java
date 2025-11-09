package mcv;

/**
 * This is an interface for a model for a todo list app.
 */
public interface ITodoList {
  void addTask(String task);
  String getTasks();
  void clearTasks();

}
