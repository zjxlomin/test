import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str=sc.nextLine();
        String[] num=str.split("");
        Arrays.sort(num);
        for(int i=num.length-1;i>=0;i--){
            System.out.print(num[i]);
        }
    }
}