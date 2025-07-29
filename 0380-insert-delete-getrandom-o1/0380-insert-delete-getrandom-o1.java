import java.util.*;

class RandomizedSet {
    List<Integer> list;
    Map<Integer, Integer> map;  // value to index
    Random random;

    public RandomizedSet() {
        list = new ArrayList<>();
        map = new HashMap<>();
        random = new Random();
    }
    
    public boolean insert(int val) {
        if (map.containsKey(val)) {
            return false;
        }
        map.put(val, list.size());
        list.add(val);
        return true;
    }
    
    public boolean remove(int val) {
        if (!map.containsKey(val)) {
            return false;
        }

        int indexToRemove = map.get(val);
        int lastElement = list.get(list.size() - 1);

        // Swap with last element if it's not already the last
        list.set(indexToRemove, lastElement);
        map.put(lastElement, indexToRemove);

        // Remove the last element
        list.remove(list.size() - 1);
        map.remove(val);

        return true;
    }
    
    public int getRandom() {
        int randomIndex = random.nextInt(list.size());
        return list.get(randomIndex);
    }
}
