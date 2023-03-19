# stack 2개를 이용해 queue만들기 : 선입선출
class Queue(object):
    def __init__(self):
        self.inputstack = []
        self.outputstack = []

    def input(self, element):
        self.inputstack.append(element)

    def output(self):
        if not self.outputstack:
            while self.inputstack:
                self.outputstack.append(self.inputstack.pop())
        return self.outputstack.pop()


# queue 2개를 이용해 stack 만들기 : top(마지막에 추가된 데이터)부터 출력
import queue
class Stack(object):
  def __init__(self):
    self.inQue = queue.Queue()
    self.outQue = queue.Queue()

  def input(self, element):
    self.inQue.put(element)

  def output(self):
    while self.inQue.qsize() > 1 :
      self.outQue.put(self.inQue.get())

    temp=self.inQue
    self.inQue = self.outQue
    self.outQue = temp

    return self.outQue.get()
      
      