import random
import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

array_size = 3

recvdata = numpy.zeros(array_size,dtype=int)
# Формируем массивы с исходными данными размером array_size
senddata = (rank+2 * 2)*numpy.arange(array_size,dtype=int)
senddata[0] = random.randint(1, 99)
print(" process %s sending %s " %(rank , senddata))

# Применяем групповое суммирование каждого элемента во всех процессах  
comm.Reduce(senddata,recvdata,root=0,op=MPI.MIN)

# и выводим в нулевом результат
if rank == 0: 
  print ('Min is ',recvdata[0])