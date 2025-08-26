import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();
        int[] cases = new int[n];
        for(int i = 0; i < n; i++) {
            cases[i] = sc.nextInt();
            sc.nextLine();
        }
        int max = Arrays.stream(cases).max().getAsInt();

        int[] dp = new int[max];
        dp[0]=1;
        if(max>=2){
            dp[1]=2;
            if(max>=3){
                dp[2]=4;
                if(max>3){
                    for(int i = 3; i < max; i++) {
                        dp[i]=dp[i-1]+dp[i-2]+dp[i-3];
                    }
                }
            }
        }
        for(int x: cases) {
            System.out.println(dp[x-1]);
        }
    }
}