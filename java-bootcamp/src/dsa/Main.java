package dsa;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Stack;

// data structures and algorithms
public class Main {

  public static void main(String[] args) {

  }


  public static void Arrays() {
    // must use the reference type Integer and cannot use the primitive type int
    List<Integer> myList = new ArrayList<Integer>();

    // an array is always initialized with 0s
    int[] myInts = new int[10]; // an array of size 10
    //System.out.println(myInts[10]); // throws an error

    int[] myInts2 = {1, 2, 3, 4, 5};

    for (int i: myInts2) {
      System.out.println(i);
    }

  }


  public static void StacksAndQueues() {
    Stack<Integer> myStack = new Stack<Integer>();
    // .push(_), .pop(), .peek(), .size(), etc etc
    // pretty straight forward

    // QUEUES: FIFO
    Queue<Integer> myQueue = new LinkedList<Integer>();
    myQueue.add(1);

    LinkedList<String> people = new LinkedList<>();



  }

  public static void myLinkedLIst() {
    IListNode<String> myll = new ListNode<String>("Naman", null);

  }
}
