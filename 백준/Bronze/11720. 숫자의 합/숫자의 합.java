import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        String num = sc.nextLine();
        String[] num2 = num.split("");
        int res = 0;

        for(int i=0;i<n;i++){
            int k = Integer.parseInt(num2[i]);
            res += k;
        }

        System.out.println(res);
    }
}