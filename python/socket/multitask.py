import time
import threading

def Toothbrush(brand):
    for i in range(10):
        print("tooth..ยี่ห้อ"+brand)
        time.sleep(0.3)

def Shower(soap,gel):
    for i in range(10):
        print("show..สบู่ {} ยาสระผม {}".format(soap,gel))
        time.sleep(0.5)

task1 = threading.Thread(target=Toothbrush,args=('colgate',))
task2 = threading.Thread(target=Shower,args=('นกแก้ว','คันหัว'))

start = time.time()
#Toothbrush()
#Shower()
task1.start()
task2.start()
task1.join()
task2.join()

end = time.time()
print('All time', end - start)
print("-----------")
print("go to school")

