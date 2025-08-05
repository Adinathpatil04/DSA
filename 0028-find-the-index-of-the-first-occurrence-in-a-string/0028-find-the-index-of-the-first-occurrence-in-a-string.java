class Solution {
    public int strStr(String haystack, String needle) {
        if(needle.isEmpty()) {
            return 0;
        }

        int nl = needle.length();
        int hl = haystack.length();

        if(nl > hl) {
            return -1;
        }

        for(int i=0; i<=hl-nl; i++) {
            if(haystack.substring(i, i+nl).equals(needle)) {
                return i;
            }
        }

        return -1;
    } 
}



