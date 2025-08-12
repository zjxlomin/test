import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String sent=sc.nextLine();
        sent=sent.trim();
        if(sent.equals("")){
            System.out.println(0);
        }
        else{
            String[] words=sent.split(" ");
            System.out.println(words.length);
        }
    }
}