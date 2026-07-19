
import java.util.Scanner;

public class input {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter Your Age: ");
        int age = input.nextInt();

        System.out.println("You are " + age + " Old");

        

        System.out.print("Enter 1 Number: ");
        int a = input.nextInt();

        System.out.print("Enter 2 Number: ");
        int b = input.nextInt();

        System.out.println("Sum: "+ (a + b));

        System.out.print("Enter your name: ");
        String name = input.nextLine();

        input.close();
    }
}
