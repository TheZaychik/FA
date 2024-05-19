from mpi4py import MPI
import statistics
import random
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


# Массив отсылаемых значений
senddata = (random.randint(1,99))*numpy.arange(size,dtype=int)
# Массив для принимаемых значений
data_rcv = numpy.empty(size,dtype=int)

print(" process %s sending %s" % (rank, senddata))

comm.Alltoall(senddata, data_rcv)

print(data_rcv)
mean = numpy.empty(size,dtype=int)
mean[0] = statistics.mean(data_rcv)
print(" process %s receiving senddata %s" % (rank, senddata))

mean_rcv = numpy.empty(size,dtype=int)

comm.Alltoall(mean, mean_rcv)
print(" process %s receiving mean_rcv %s" % (rank, mean_rcv))
