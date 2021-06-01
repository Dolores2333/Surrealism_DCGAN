# coding=utf-8
from time import sleep, ctime
import threading
import urllib.request
import os
import time

print("program start %s" % ctime())

genre = 'surrealism'
data_dir = os.path.join(os.getcwd(), '../data')

path = os.path.join(data_dir, genre)
if not os.path.exists(path):
    os.makedirs(path)


url_set = []
filename_set = []
temp_url_set = []
temp_filename_set = []
with open("wikiart_surrealism_images_urls.txt", 'r', encoding="utf8") as read_file:
    all_lines = read_file.readlines()
    print("number: ", len(all_lines))
    len_all_lines = len(all_lines)
    for index, line in enumerate(all_lines):
        url = line.strip()
        temp_url_set.append(url)
        file_name = path + "/" + str(url.split("/")[-1])
        #file_name = path + "/" + str(url.split("/")[-1]) + ".png"
        temp_filename_set.append(file_name)
        if (index + 1) % 10 == 0 or index == (len_all_lines - 1):
            url_set.append(temp_url_set)
            filename_set.append(temp_filename_set)
            temp_url_set = []
            temp_filename_set = []


def downloading_images(url, filename):
    #         print("start downloading", url)
    urllib.request.urlretrieve(url, filename=filename)
    sleep(1)
    print("end downloading", url)


if __name__ == '__main__':
    epoch = 1
    for (urls, filenames) in zip(url_set, filename_set):
        threads = []
        for (url, filename) in zip(urls, filenames):
            t = threading.Thread(target=downloading_images, args=(url, filename))
            threads.append(t)
        for i in range(len(threads)):
            threads[i].start()

        for i in range(len(threads)):
            threads[i].join()
        print("epoch %d finished in %s" % (epoch, ctime()))
        epoch += 1

    print('program end:%s' % ctime())
