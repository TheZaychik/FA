import sys
from mpi4py import MPI
from numpy import empty, array, int32, float64, dot

# определяем коммуникатор comm – группу процессов, которые участвуют в вычислениях
comm = MPI.COMM_WORLD
# rank применяется для указания номера процесса
rank = comm.Get_rank()


numprocs = comm.Get_size()

if rank == 0:
    f1 = open("/home/user/proj/sem13/MPIMess/in.dat", "r")
    N = array(int32(f1.readline()))
    M = array(int32(f1.readline()))
    f1.close()
else:
    N = array(0, dtype=int32)
    M = array(0, dtype=int32)

if rank == 0:
    comm.send(M, dest=1, tag=0)
    print(f"Variable N on process {rank} is: {N}")
    print(f"Variable M on process {rank} is: {M}")
elif rank == 1:
    N = comm.recv(source=0, tag=0)
    print(f"Variable N on process {rank} is: {N}")
    print(f"Variable M on process {rank} is: {M}")
else:
    sys.exit(0)
