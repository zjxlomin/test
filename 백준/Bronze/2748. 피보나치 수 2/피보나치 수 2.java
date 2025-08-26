import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        long a=0;
        long b=1;
        int i=1;
        long res=1;
        while(i<n){
            i++;
            res=a+b;
            a=b;
            b=res;
        }
        System.out.println(res);
    }
}