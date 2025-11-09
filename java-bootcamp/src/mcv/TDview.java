package mcv;

import java.io.IOException;
import java.util.Scanner;

public class TDview implements IView {

  private final Scanner in;
  private final Appendable out;

  public TDview(Readable in, Appendable out) {
    this.in = new Scanner(in);
    this.out = out;
  }


  @Override
  public void show(String message) {
    try {
      out.append(message).append("\n");
    } catch (IOException e) {
      throw new RuntimeException(e);
    }
  }

  @Override
  public String getInput() {
    return in.nextLine();
  }
}
