import org.junit.Test;

import books.Book;
import books.Publication;

import static org.junit.Assert.assertEquals;

public class BookTest {

  @Test
  public void testApa(){
    Publication rushdie = new Book("Midnight's Children", "Salman Rushdie",
            "Jonathan Cape", "London", 1980);

    String expectedOutput =
            "Salman Rushdie (1980). Midnight's Children. London: Jonathan Cape.";
    assertEquals(expectedOutput,rushdie.citeApa());
  }
}
