import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int h=sc.nextInt();
        int m=sc.nextInt();
        int t=h*60+m;
        sc.nextLine();

        int c=sc.nextInt();
        t+=c;
        if(t>=1440){
            t-=1440;
        }
        System.out.println(t/60+" "+t%60);
    }
}