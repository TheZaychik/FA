from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = [int(num) for num in input().split(" ")]
else:
    data = None
data = comm.bcast(data, root=0)
print(f"Process {rank}, data: {data}")
