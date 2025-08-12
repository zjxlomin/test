import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n=sc.nextInt();
        sc.nextLine();

        int[] scores=new int[n];
        for(int i=0;i<n;i++){
            scores[i]=sc.nextInt();
        }
        int m=0;
        for(int i=0;i<n;i++){
            if(scores[i]>m){
                m=scores[i];
            }
        }
        double sum=0;
        for(int i=0;i<n;i++){
            sum+=(scores[i]/(double)m)*100;
        }
        System.out.println(sum/n);
    }
}