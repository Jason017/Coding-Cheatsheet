import java.util.*;

public class Convert {
    public static void main(String[] args) {

        // array to list
        Integer[] nums = new Integer[] { 1, 2, 3 };
        List<Integer> list1 = Arrays.asList(nums);
        System.out.println(list1);

        // only workable for Integer arrays, int arrays will cause error:
        // incompatible types: Object[] cannot be converted to Integer[]

        // same for List<Integer> list2 = Arrays.asList(new int[] { 5, 9, 7 });
        System.out.println(Arrays.asList(new int[] { 5, 9, 7 })); // but this works

        // list to array
        List<Integer> list3 = new ArrayList<>();
        list3.add(5);
        list3.add(9);
        list3.add(7);
        // nums = list3.toArray() will cause incompatible error:
        // incompatible types: Object[] cannot be converted to Integer[]
        System.out.println(list3.toArray(new Integer[list3.size()]));

        // converting the String to a Array/List of characters,
        // has a cost of O(n), because we are adding n characters
        // to the end of a Array/List
        String s = "leetcodeee";
        char[] chars = s.toCharArray();

        List<String> strList = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        sb.append(chars[0]);
        for (int i = 1; i < chars.length; i++) {
            if (chars[i] != chars[i - 1]) {
                strList.add(sb.toString());
                sb = new StringBuilder();
            }
            sb.append(chars[i]);
        }
        strList.add(sb.toString());
        System.out.println(strList);
    }
}
