package vehicle;


public class Car implements IVehicle {
  @Override
  public String getName() {
    return "This is a car";
  }

  // defaultly implements the .move() method in the interface......
  // cna override it here..
}
