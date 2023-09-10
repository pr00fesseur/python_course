import time
import os
import requests
import threading
import multiprocessing

def encrypt_file(path: str):
    print(f"Обработка изображения в процессе {os.getpid()}")
    _ = [i for i in range(100_000_000)]

def download_image(image_url):
    print(f"Скачивание изображения в потоке {threading.current_thread().name}")
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)

if __name__ == "__main__":
    start_time = time.perf_counter()

    encryption_process = multiprocessing.Process(target=encrypt_file, args=("rockyou.txt",))
    download_thread = threading.Thread(target=download_image, args=("https://picsum.photos/1000/1000",))

    encryption_process.start()
    download_thread.start()

    encryption_process.join()
    download_thread.join()

    end_time = time.perf_counter()

    print(f"Затраченное время: {end_time - start_time:.2f} секунд")
