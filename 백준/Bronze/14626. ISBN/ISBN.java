import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s = sc.nextLine();
        String[] isbn = s.split("");
        int check = 0;
        int missing = 0;
        int res = 0;
        for(int i=0;i<12;i++){
            if(isbn[i].equals("*")){
                missing = i;
            }
            else {
                if(i%2==0){
                    check+=Integer.parseInt(isbn[i]);
                }
                else {
                    check+=Integer.parseInt(isbn[i])*3;
                }
            }
        }
        check+=Integer.parseInt(isbn[12]);
        if(missing%2==0){
            res = 10 - check%10;
        }
        else{
            for(int i=0;i<10;i++){
                if((check+i*3)%10==0){
                    res=i;
                    break;
                }
            }
        }
        System.out.println(res);
    }
}