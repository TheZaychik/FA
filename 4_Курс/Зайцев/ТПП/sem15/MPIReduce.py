import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

array_size = 3

recvdata = numpy.zeros(array_size,dtype=int)
# Формируем массивы с исходными данными размером array_size
senddata = (rank+1)*numpy.arange(array_size,dtype=int)

print(" process %s sending %s " %(rank , senddata))

# Применяем групповое суммирование каждого элемента во всех процессах  
comm.Reduce(senddata,recvdata,root=0,op=MPI.SUM)

# и выводим в нулевом результат
if rank == 0: 
  print ('on task',rank,'after Reduce:    data = ',recvdata)