package mcv;

import java.util.ArrayList;
import java.util.List;

public class TodoListModel implements ITodoList {

  // making this field final means we are finalizing it's spot in
  private final List<String> tasks = new ArrayList<>();

  @Override
  public void addTask(String task) {
    this.tasks.add(task);
  }

  @Override
  public String getTasks() {
    return String.join("\n", tasks); // using the in built method
  }

  @Override
  public void clearTasks() {
    this.tasks.clear();
  }
}
