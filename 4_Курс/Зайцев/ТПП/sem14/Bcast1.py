from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {"key1": [5, 1.72, 1 + 6j], "key2": ("123", "321")}
else:
    data = None
data = comm.bcast(data, root=0)
print(f"Process {rank}, data: {data}")
