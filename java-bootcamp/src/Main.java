import vehicle.Car;
import vehicle.IVehicle;

public class Main {
  public static void main(String[] args) {
    System.out.println("Hello, World!");
    IVehicle cah = new Car();
    System.out.println(cah.getName());
  }
}
