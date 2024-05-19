from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


# Массив отсылаемых значений
senddata = (rank+1)*numpy.arange(size,dtype=int)
# Массив для принимаемых значений
recvdata = numpy.empty(size,dtype=int)

print(" process %s sending %s" %(rank , senddata))

# Отсылаем индивидуальные сообщения от каждого процесса каждому процессу
# Нулевой процесс отсылает нулевой элемент себе, первый первому и т.д
# Первый процесс нулевой элемент нулевому процессу, первый себе и т.д
# Удобно транспонировать матрицу, отдав каждую строку исходной матрицы процессу и собрав резудьтирующие строки
comm.Alltoall(senddata,recvdata)
print(" process %s receiving %s" %(rank , recvdata))
