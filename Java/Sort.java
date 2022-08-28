import java.util.*;

import javax.xml.transform.Source;

public class Sort {
    public static void main(String[] args) {
        // sort a string array
        String[] strArr = { "Java", "Python", "Perl", "C++", "C#", "AS400" };
        Arrays.sort(strArr);
        System.out.println(printStrArr(strArr));

        // sort a string list
        ArrayList<String> strList = new ArrayList<String>();
        strList.add("LeetCode");
        strList.add("is");
        strList.add("lots");
        strList.add("of");
        strList.add("fun");
        Collections.sort(strList);
        System.out.println(strList);

        // sort a list of integer array
        ArrayList<int[]> arrList = new ArrayList<>();
        arrList.add(new int[] { 1, 5 });
        arrList.add(new int[] { 2, 6 });
        arrList.add(new int[] { 4, 2 });
        arrList.add(new int[] { 5, 7 });
        Collections.sort(arrList, (a, b) -> a[1] - b[1]); // sort by the second element
        System.out.println(printArrList(arrList));

        int[][] nestedArr = new int[][] { { 5, 7 }, { 1, 5 }, { 4, 2 }, { 2, 6 } };
        Arrays.sort(nestedArr, (a, b) -> a[0] - b[0]); // sort by the first element
        System.out.println(printNestedArr(nestedArr));
    }

    public static String printStrArr(String[] arr) {
        StringBuilder sb = new StringBuilder("{");
        for (int i = 0; i < arr.length; i++) {
            sb.append(arr[i] + ", ");
        }
        return sb.substring(0, sb.length() - 2).toString() + "}";
    }

    public static String printArrList(ArrayList<int[]> arrList) {
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
