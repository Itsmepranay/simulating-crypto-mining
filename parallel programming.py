import hashlib
import time
import random
import multiprocessing

class Miner:
    def __init__(self, id, total_coins_queue):
        self.id = id
        self.coins = 0
        self.total_coins_queue = total_coins_queue  # Reference to the shared total coins queue

    def mine(self, difficulty):
        while True:
            nonce = random.randint(0, 1000000)
            data = f"Block data + Nonce: {nonce}".encode()
            hash_attempt = hashlib.sha256(data).hexdigest()

            if hash_attempt[:difficulty] == '0' * difficulty:
                print(f"Miner {self.id} mined a block! Nonce: {nonce}")
                self.coins += 1
                self.total_coins_queue.put(1)  # Notify main process that a coin was mined

def mine_blocks(miner, difficulty):
    miner.mine(difficulty)

def main():
    num_miners = 4
    difficulty = 3



    total_coins_queue = multiprocessing.Queue()  # Shared total coins queue

    miners = [Miner(i, total_coins_queue) for i in range(num_miners)]
    processes = []

    print("Starting mining simulation...")

    start_time = time.time()  # Start measuring time

    for miner in miners:
        process = multiprocessing.Process(target=mine_blocks, args=(miner, difficulty))
        processes.append(process)
        process.start()

    time.sleep(10)  # Let the simulation run for 10 seconds

    for process in processes:
        process.terminate()

    # Count the total coins based on the notifications from miners
    total_coins = 0
    while not total_coins_queue.empty():
        total_coins += total_coins_queue.get()

    end_time = time.time()  # Stop measuring time
    elapsed_time = end_time - start_time

    print(f"Simulation ended. Total coins mined: {total_coins}")
    print(f"Time taken: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
