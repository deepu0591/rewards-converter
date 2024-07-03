package main.java;

public class RewardValueTest {
    public static void main(String[] args) {
        // Create an instance using the cash value constructor
        RewardValue rewardFromCash = new RewardValue(100.0); // 100 dollars
        System.out.println("Reward from Cash:");
        System.out.println("Cash Value: $" + rewardFromCash.getCashValue());
        System.out.println("Miles Value: " + rewardFromCash.getMilesValue() + " miles");

        // Create an instance using the miles value constructor
        RewardValue rewardFromMiles = new RewardValue(50000); // 50,000 miles
        System.out.println("Reward from Miles:");
        System.out.println("Cash Value: $" + rewardFromMiles.getCashValue());
        System.out.println("Miles Value: " + rewardFromMiles.getMilesValue() + " miles");
    }
}
