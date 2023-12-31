import logging
import time


class TimerContext:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.perf_counter()
        execution_time = self.end_time - self.start_time
        logging.info(f"Execution time: {execution_time:.4f} seconds")


# Set up logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

with TimerContext():
    time.sleep(2)
