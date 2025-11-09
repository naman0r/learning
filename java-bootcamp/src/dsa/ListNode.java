package dsa;

/**
 * Interface design for linked lists
 */
interface IListNode<T> {
  // actually dont need any things in here specifically
}


public class ListNode<T> implements IListNode {
  public T val;
  public IListNode<T> next;
  public ListNode(T val, IListNode<T> next) {
    this.val = val;
    this.next = next;
  }

}
