import java.util.Random;

public class generator_j {
    public static void main(String[] args) {
        int length = 128;
        String sequence = generateRandomBinaryString(length);
        System.out.println(sequence);
    }
    
    public static String generateRandomBinaryString(int length) {
        StringBuilder sequence = new StringBuilder();
        Random random = new Random();

        for (int i = 0; i < length; i++) {
            int randomBit = random.nextInt(2);
            sequence.append(randomBit);
        }

        return sequence.toString();
    }
}