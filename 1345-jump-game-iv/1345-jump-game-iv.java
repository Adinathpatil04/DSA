import java.util.*;

public class Solution {
    public static int minJumps(int[] rooms) {
        int n = rooms.length;
        if (n == 1) return 0;

        // Map each category to all its indices
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n; i++) {
            graph.computeIfAbsent(rooms[i], k -> new ArrayList<>()).add(i);
        }

        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[n];
        queue.add(0);
        visited[0] = true;

        int steps = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();

            for (int s = 0; s < size; s++) {
                int i = queue.poll();

                if (i == n - 1) return steps;

                // Move left
                if (i - 1 >= 0 && !visited[i - 1]) {
                    visited[i - 1] = true;
                    queue.add(i - 1);
                }

                // Move right
                if (i + 1 < n && !visited[i + 1]) {
                    visited[i + 1] = true;
                    queue.add(i + 1);
                }

                // Jump to same category rooms
                if (graph.containsKey(rooms[i])) {
                    for (int j : graph.get(rooms[i])) {
                        if (!visited[j]) {
                            visited[j] = true;
                            queue.add(j);
                        }
                    }
                    // Clear to avoid redundant future processing
                    graph.remove(rooms[i]);
                }
            }
            steps++;
        }

        return -1; // should not reach here
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of rooms (n): ");
        int n = sc.nextInt();

        int[] rooms = new int[n];
        System.out.println("Enter the room categories (space separated): ");
        for (int i = 0; i < n; i++) {
            rooms[i] = sc.nextInt();
        }

        int result = minJumps(rooms);
        System.out.println("Minimum number of jumps: " + result);
    }
}
