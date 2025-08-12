import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        int res = 0;

        for(int i=0;i<n;i++) {
            int num = sc.nextInt();
            if(num==2){
                res++;
            }
            else if(num>1 && num%2!=0){
                boolean isPrime = true;
                int k = 2;
                while(k<num){
                    if(num%k==0){
                        isPrime = false;
                        break;
                    }
                    k++;
                }
                if(isPrime){
                    res++;
                }
            }
        }
        System.out.println(res);
    }
}