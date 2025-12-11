class Solution {
    public int[] searchRange(int[] nums, int target) {

        int[] arr = new int[2];
        arr[0] = arr[1] = -1;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {

                // first occurrence
                if (arr[0] == -1) arr[0] = i;

                // find last occurrence safely
                int j = i;
                while (j + 1 < nums.length && nums[j + 1] == target) {
                    j++;
                }
                arr[1] = j;
                
                break; // done
            }
        }

        return arr;
    }
}
