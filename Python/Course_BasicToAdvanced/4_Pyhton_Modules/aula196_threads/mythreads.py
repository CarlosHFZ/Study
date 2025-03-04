from time import sleep
from threading import Thread, Lock


# class MyThread(Thread):
#     def __init__(self, text, temp):
#         self.text = text
#         self.temp = temp

#         super().__init__()

#     def run(self):
#         sleep(self.temp)
#         print(self.text)


# t1 = MyThread("Thread 1", 5)
# t1.start()

# t2 = MyThread("Thread 2", 3)
# t2.start()

# t3 = MyThread("Thread 3", 2)
# t3.start()

# for i in range(20):
#     print(i)
#     sleep(1)


def it_will_take_time(text, time):
    sleep(time)
    print(text)


# t1 = Thread(target=it_will_take_time, args=('Olá mundo!', 5))
# t1.start()
# t2 = Thread(target=it_will_take_time, args=('Olá mundo!', 1))
# t2.start()
# t3 = Thread(target=it_will_take_time, args=('Olá mundo!', 2))
# t3.start()


# for i in range(20):
#     print(i)
#     sleep(.5)


# t1 = Thread(target=it_will_take_time, args=('Olá mundo 1!', 10))
# t1.start()


# while t1.is_alive():
#     print('Esperando a thread.')
#     sleep(2)
# print("Thread acabou")


class Tickets:
    def __init__(self, stock):
        self.stock = stock
        self.lock = Lock()

    def buy(self, amount):
        self.lock.acquire()

        if self.stock < amount:
            print('Não temos ingressos suficientes')
            self.lock.release()
            return

        sleep(1)

        self.stock -= amount
        print(f'Você comprou {amount} ingresso(s). '
              f"Ainda temos {self.stock} em estoque")

        self.lock.release()


if __name__ == '__main__':
    tickets = Tickets(10)

    for i in range(1, 20):
        t = Thread(target=tickets.buy, args=(i,))
        t.start()

    print(tickets.stock)
