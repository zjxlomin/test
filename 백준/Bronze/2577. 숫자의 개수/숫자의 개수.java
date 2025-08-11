import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        sc.nextLine();
        int b = sc.nextInt();
        sc.nextLine();
        int c = sc.nextInt();
        sc.nextLine();

        String res = Integer.toString(a*b*c);
        String[] res2 = res.split("");
        int[] count = {0,0,0,0,0,0,0,0,0,0};

        for(int i=0;i<res2.length;i++){
            int k = Integer.parseInt(res2[i]);
            count[k]++;
        }

        for(int i=0;i<10;i++){
            System.out.println(count[i]);
        }
    }
}