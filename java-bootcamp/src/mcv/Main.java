package mcv;

import java.io.InputStreamReader;

import javax.swing.text.View;

public class Main {

  public static void main(String[] args) {
    ITodoList model = new TodoListModel();
    IView view = new TDview(new InputStreamReader(System.in), System.out);
    IController controller = new TodoController(view, model);
    controller.run();
  }
}
