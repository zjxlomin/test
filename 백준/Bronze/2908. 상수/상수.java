import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        sc.nextLine();


        StringBuffer aBuff = new StringBuffer(Integer.toString(a));
        StringBuffer bBuff = new StringBuffer(Integer.toString(b));

        a = Integer.parseInt(aBuff.reverse().toString());
        b = Integer.parseInt(bBuff.reverse().toString());

        System.out.println(Math.max(a, b));
    }
}