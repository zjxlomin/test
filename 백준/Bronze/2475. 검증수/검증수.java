import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] ser = new int[5];
        int res = 0;

        for(int i=0;i<5;i++){
            ser[i] = sc.nextInt();
        }

        for(int i=0;i<5;i++){
            res+=ser[i]*ser[i];
        }

        System.out.println(res%10);
    }
}