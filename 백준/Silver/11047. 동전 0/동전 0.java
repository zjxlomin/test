import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();
        sc.nextLine();

        int[] coins =  new int[n];
        for(int i = 0; i < n; i++){
            coins[i]=sc.nextInt();
            sc.nextLine();
        }

        int res = 0;
        for(int j = n-1; j >= 0; j--){
            if(k>=coins[j]){
                res+=k/coins[j];
                k%=coins[j];
            }
        }
        System.out.println(res);
    }
}