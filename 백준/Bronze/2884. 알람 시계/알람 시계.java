import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int h = sc.nextInt();
        int m = sc.nextInt();
        int t = h*60+m;
        if(t<45){
            t+=1440;
        }
        t-=45;
        h=t/60;
        m=t%60;

        System.out.println(h+" "+m);
    }
}