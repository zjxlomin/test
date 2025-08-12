import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        int[] tshirt = new int[6];
        for(int i=0;i<6;i++){
            tshirt[i] = sc.nextInt();
        }
        int t = sc.nextInt();
        int p = sc.nextInt();
        sc.nextLine();

        int packs = 0;
        for(int i=0;i<6;i++){
            if(tshirt[i]!=0){
                packs += (tshirt[i]-1)/t+1;
            }
        }
        System.out.println(packs);
        System.out.print(n/p + " ");
        System.out.println(n%p);
    }
}