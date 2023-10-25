import hashlib
import time
import random

class Miner:
    def __init__(self, id):
        self.id = id
        self.coins = 0

    def mine(self, difficulty):
        while True:
            nonce = random.randint(0, 1000000)
            data = f"Block data + Nonce: {nonce}".encode()
            hash_attempt = hashlib.sha256(data).hexdigest()

            if hash_attempt[:difficulty] == '0' * difficulty:
                print(f"Miner {self.id} mined a block! Nonce: {nonce}")
                self.coins += 1
                print(f"Miner {self.id} now has {self.coins} coins.")
                break  # Exit the loop when a block is mined successfully

def main():
    num_miners = 4
    difficulty = 3
    simulation_duration = 10  # Run the simulation for 10 seconds

    miners = [Miner(i) for i in range(num_miners)]

    print("Starting serial mining simulation...")

    start_time = time.time()  # Start measuring time
    end_time = start_time + simulation_duration  # Calculate the end time

    while time.time() < end_time:
        for miner in miners:
            miner.mine(difficulty)

    elapsed_time = time.time() - start_time

    total_coins = sum(miner.coins for miner in miners)
    print(f"Serial simulation ended. Total coins mined: {total_coins}")
    print(f"Time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
