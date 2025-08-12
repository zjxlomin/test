import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] note = new int[8];
        for(int i=0;i<8;i++){
            note[i] = sc.nextInt();
        }
        if(note[0]==1){
            boolean isAsc = true;
            for(int j=1;j<8;j++){
                if(note[j]!=j+1){
                    isAsc = false;
                    break;
                }
            }
            if(isAsc){
                System.out.println("ascending");
            }
            else {
                System.out.println("mixed");
            }
        }
        else if(note[0]==8){
            boolean isDesc = true;
            for(int j=1;j<8;j++){
                if(note[j]!=8-j){
                    isDesc = false;
                    break;
                }
            }
            if(isDesc){
                System.out.println("descending");
            }
            else {
                System.out.println("mixed");
            }
        }
        else {
            System.out.println("mixed");
        }
    }
}