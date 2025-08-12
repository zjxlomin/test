import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n=sc.nextInt();
        sc.nextLine();

        int cycle=0;
        int first=n;
        int k;

        while(true){
            k=n/10+n%10;
            n=(n%10)*10+k%10;
            cycle++;
            if(n==first){
                break;
            }
        }
        System.out.println(cycle);
    }
}