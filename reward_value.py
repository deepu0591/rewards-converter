class RewardValue:
    CASH_TO_MILES_CONVERSION_RATE = 100  # Example conversion rate

    def __init__(self, value, value_type):
        """
        Initializes a RewardValue instance.
        
        :param value: The amount of the reward.
        :param value_type: The type of the reward ('cash' or 'miles').
        """
        self.value = value
        self.value_type = value_type

    def to_cash(self):
        """
        Converts the reward value to cash.
        
        :return: The value in cash.
        """
        if self.value_type == 'cash':
            return self.value
        elif self.value_type == 'miles':
            return self.value / self.CASH_TO_MILES_CONVERSION_RATE
        else:
            raise ValueError("Invalid value type")

    def to_miles(self):
        """
        Converts the reward value to miles.
        
        :return: The value in miles.
        """
        if self.value_type == 'miles':
            return self.value
        elif self.value_type == 'cash':
            return self.value * self.CASH_TO_MILES_CONVERSION_RATE
        else:
            raise ValueError("Invalid value type")

    def __str__(self):
        return f"{self.value} {self.value_type}"

# Example usage:
if __name__ == "__main__":
    cash_value = RewardValue(100, 'cash')
    print(f"{cash_value} in miles is {cash_value.to_miles()} miles")

    miles_value = RewardValue(10000, 'miles')
    print(f"{miles_value} in cash is ${miles_value.to_cash()}")
