import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int res = 0;

        int k = n%10;
        if(k%2==0){
            if(k==0){
                res = n/5;
            }
            else{
                res = (n-k)/5 + (k/2);
            }
        }
        else{
            switch(k){
                case 1:
                    res = n>=11 ? (n-6)/5+3 : -1;
                    break;
                case 3:
                    res = n>=13 ? (n-8)/5+4 : -1;
                    break;
                case 5:
                    res = n/5;
                    break;
                case 7:
                    res = (n-2)/5 + 1;
                    break;
                case 9:
                    res = (n-4)/5 + 2;
                    break;
            }
        }
        System.out.println(res);
    }
}