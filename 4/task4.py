'''
Написать программу, которая скачивает изображения с заданных URL-адресов и
сохраняет их на диск. Каждое изображение должно сохраняться в отдельном
файле, название которого соответствует названию изображения в URL-адресе.
Например URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
Программа должна иметь возможность задавать список URL-адресов через аргументы 
командной строки.
Программа должна выводить в консоль информацию о времени скачивания каждого изображения 
и общем времени выполнения программы.
'''

import requests
import threading
from multiprocessing import Process
import asyncio
import aiofiles
import aiohttp
import time

START_TIME = time.time()
start_time_all = time.time()

urls = ["https://www.funnyart.club/uploads/posts/2022-12/1671883620_www-funnyart-club-p-samie-krasivie-ptitsi-krasivie-zhivotnie-28.jpg",
        "https://pofoto.club/uploads/posts/2022-01/1641116797_27-pofoto-club-p-samikh-redkikh-ptits-mira-foto-58.jpg",
        "https://zooblogi.ru/uploads/posts/2014-09/1410537765_samye-krasivye-ekzotpticy-1.jpg",
        "https://zooblog.ru/uploads/posts/2014-09/1410537765_samye-krasivye-ekzotpticy-1.jpg",
        ]

def download_images(url, prefix):
    try: 
        image = requests.get(url)
        if image.status_code == 200:
            temp = url.split("/")
            filename = prefix+"_"+temp[len(temp)-1]
            with open(filename, "wb") as f:
                for chunk in image.iter_content(1024):
                    f.write(chunk)
                print(f"Downloaded {filename} in {time.time()-START_TIME:.2f} seconds")
    except:
        print(f'Invalid link: {url}')

async def download_images_2(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    temp = url.split("/")
                    filename = "asyncio_"+temp[len(temp)-1]   
                    f = await aiofiles.open(filename, mode='wb')
                    await f.write(await response.read())
                    await f.close()
                    print(f"Downloaded {filename} in {time.time()-START_TIME:.2f} seconds")
    except:
        print(f'Invalid link: {url}')

def thread_approach():
    global START_TIME
    START_TIME = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_images, args=[url, 'thread'])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(f"Downloaded all files on threads in {time.time()-START_TIME:.2f} seconds")

def multiprocessing_approach():
    global START_TIME
    START_TIME = time.time()
    processes = []
    for url in urls:
        process = Process(target=download_images, args=(url,'multi'))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    print(f"Downloaded all files on multiprocessing in {time.time()-START_TIME:.2f} seconds")

async def asynchron_approach():
    global START_TIME
    START_TIME = time.time()
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_images_2(url))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print(f"Downloaded all files on asynchron in {time.time()-START_TIME:.2f} seconds")
    


if __name__ == '__main__':
    thread_approach()
    multiprocessing_approach()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.run(asynchron_approach())
    print(f"Downloaded all files in {time.time()-start_time_all:.2f} seconds")





