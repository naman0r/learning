package exm1;


/**
 * This class represents a locker allocator at a beach location.
 *
 * This class assumes that the id of a locker is a function of
 * the approximate distance of that locker from the checkout counter.
 * In other words, lockers closer to the counter have a smaller ID
 * than those farther away.
 *
 * Furthermore it assumes that all locker numbers are within a
 * contiguous range (e.g. 2, 3, 4, 5, 6, 7, 8).
 * While the locker numbers should always be positive,
 * they can start and end at any number.
 *
 * In order to help their customers and also optimize the cleanup time
 * at the end of the day, this allocator always tries to allocate
 * a free locker that is closest to the checkout counter.
 *
 * One of the desired features of this allocator is that
 * it <b>quickly</b> finds a locker to be rented.
 *
 */
public class BeachLockerAllocator implements LockerAllocator<Bag> {


    /**
     * Construct a new beach locker allocator.
     * All numbers within the specified range are assumed
     * to be functional and rent-able.
     *
     * @param minLockerNumber the smallest locker number to be used (inclusive)
     * @param maxLockerNumber the largest locker number to be used (inclusive)
     * @throws IllegalArgumentException if the max locker number is not greater than the min locker number
     *                                  or any part of the given range is non-positive.
     */
    public BeachLockerAllocator(int minLockerNumber, int maxLockerNumber) throws IllegalArgumentException {

    }

    @Override
    public int rent() throws IllegalStateException {
        return 0;
    }

    @Override
    public void free(int id) throws IllegalArgumentException {

    }

    @Override
    public void deposit(int id, Bag equipment) throws IllegalArgumentException {

    }

    @Override
    public Bag get(int id) throws IllegalArgumentException {
        return null;
    }
}
