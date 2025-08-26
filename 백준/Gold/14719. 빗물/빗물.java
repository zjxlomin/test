import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt();
        int w = sc.nextInt();
        sc.nextLine();

        int[] block = new int[w];

        for(int i=0;i<w;i++){
            block[i]=sc.nextInt();
        }
        sc.nextLine();

        int res=0;

        for(int i=1;i<w-1;i++){
            int leftMax=0;
            int rightMax=0;

            for(int j=0;j<i;j++){
                if(block[j]>leftMax){
                    leftMax=block[j];
                }
            }
            for(int j=i+1;j<w;j++){
                if(block[j]>rightMax){
                    rightMax=block[j];
                }
            }
            if(block[i]<leftMax && block[i]<rightMax){
                res+= leftMax>rightMax ? rightMax-block[i] : leftMax-block[i];
            }
        }

        System.out.println(res);
    }
}