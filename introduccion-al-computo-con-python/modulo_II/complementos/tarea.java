import java.util.Scanner;
/**
 * Chart One Bar lab
 * @author Victoria Aguilar
 * @since 3/21/2021
 */
public class ChartOneBar {
    public static void main (String [] args) {
        makeChart();
     } //ends main

    public static void makeChart() {

        Scanner scan = new Scanner (System.in);
        System.out.println("Number to chart:");

        int number = scan.nextInt();
        int i = 0;

        System.out.println(number);

        String equal = "=";

        while(i <= number) {
            if (i == number) {
                System.out.println(number + equal.repeat(number));
            }
        i ++;
        }

    } //ends loop method
 } //ends class