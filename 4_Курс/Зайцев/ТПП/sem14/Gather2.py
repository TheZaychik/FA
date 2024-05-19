from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
data = []

if rank == 0:
    data = [int(num) for num in input().split(" ")]
    print("Start data:", data)

data = comm.scatter(data, root=0)

data += 1

data = comm.gather(data, root=0)

if rank == 0:
    print("Final data", data)
