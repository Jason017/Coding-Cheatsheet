import java.util.*;

// Built-in sort method in java: O(Nlog(N)) O(log(N))
public class Sort {
    public static void main(String[] args) {
        // 1. sort a string array in ascending order
        String[] strArr = { "Java", "Python", "Perl", "C++", "C#", "AS400" };
        Arrays.sort(strArr);
        System.out.println(printStrArr(strArr)); // {AS400, C#, C++, Java, Perl, Python}

        // 2-1. sort a string list in ascending order
        ArrayList<String> strList = new ArrayList<String>();
        strList.add("LeetCode");
        strList.add("is");
        strList.add("lots");
        strList.add("of");
        strList.add("fun");
        Collections.sort(strList);
        System.out.println(strList); // [LeetCode, fun, is, lots, of]

        // 2-2. sort a string list in descending order
        Collections.sort(strList, Collections.reverseOrder());
        System.out.println(strList); // [LeetCode, fun, is, lots, of]

        // 3. sort a list of integer array by the second element in ascending order
        ArrayList<int[]> arrList = new ArrayList<>();
        arrList.add(new int[] { 1, 5 });
        arrList.add(new int[] { 2, 6 });
        arrList.add(new int[] { 4, 2 });
        arrList.add(new int[] { 5, 7 });
        Collections.sort(arrList, (a, b) -> a[1] - b[1]);
        System.out.println(printArrList(arrList));
        // [{4, 2}, {1, 5}, {2, 6}, {5, 7}]

        // 4. sort an array of integer array by the first element in ascending order
        int[][] nestedArr1 = new int[][] { { 5, 7 }, { 1, 5 }, { 4, 2 }, { 2, 6 } };
        Arrays.sort(nestedArr1, (a, b) -> a[0] - b[0]);
        System.out.println(printNestedArr(nestedArr1));
        // {{1, 5}, {2, 6}, {4, 2}, {5, 7}}

        // 5-1. sort a list of string by ascii order in ascending order
        List<String> stringList = new ArrayList<>();
        stringList.add("a");
        stringList.add("bb");
        stringList.add("A");
        stringList.add("B");
        Collections.sort(stringList, (a, b) -> a.charAt(0) - b.charAt(0));
        System.out.println(stringList); // [A, B, a, bb]

        // 5-2. sort by length of the string in descending order
        Collections.sort(stringList, (a, b) -> b.length() - a.length());
        System.out.println(stringList); // [bb, A, B, a]

        // 5-3. sort by ascii in ascending order and
        // character frequency in descending order
        List<int[]> freqList = new ArrayList<>();
        freqList.add(new int[] { 1, 'A' });
        freqList.add(new int[] { 1, 'a' });
        freqList.add(new int[] { 2, 'b' });
        Collections.sort(freqList, (a, b) -> a[0] == b[0] ? a[1] - b[1] : b[0] - a[0]);
        // If the frequency are the same, order by ascii order,
        // otherwise order by frequency.
        // Therefore, prioritize the order of 1) frequency 2) ascii order
        System.out.println(printArrList(freqList));
        // [{2, 98}, {1, 65}, {1, 97}]
    }

    public static String printStrArr(String[] arr) {
        StringBuilder sb = new StringBuilder("{");
        for (int i = 0; i < arr.length; i++) {
            sb.append(arr[i] + ", ");
        }
        return sb.substring(0, sb.length() - 2).toString() + "}";
    }

    public static String printArrList(List<int[]> arrList) {
        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < arrList.size(); i++) {
            int[] arr = arrList.get(i);
            StringBuilder temp = new StringBuilder("{");
            for (int j = 0; j < arr.length; j++) {
                temp.append(arr[j] + ", ");
            }
            sb.append(temp.substring(0, temp.length() - 2).toString() + "}, ");
        }
        return sb.substring(0, sb.length() - 2).toString() + "]";
    }

    public static String printNestedArr(int[][] nestedArr) {
        StringBuilder sb = new StringBuilder("{");
        for (int i = 0; i < nestedArr.length; i++) {
            int[] arr = nestedArr[i];
            StringBuilder temp = new StringBuilder("{");
            for (int j = 0; j < arr.length; j++) {
                temp.append(arr[j] + ", ");
            }
            sb.append(temp.substring(0, temp.length() - 2).toString() + "}, ");
        }
        return sb.substring(0, sb.length() - 2).toString() + "}";
    }
}
