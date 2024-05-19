from mpi4py import MPI

# определяем коммуникатор comm – группу процессов, которые участвуют в вычислениях
comm = MPI.COMM_WORLD
# rank применяется для указания номера процесса
rank = comm.rank
print("my rank is %i " % (rank))

# Для процесса rank, равного 1, отправляет и получает данные от процесса со значением
# rank равным 5
if rank == 1:
    data_send = "a"
    destination_process = 5
    sourse_process = 5
    comm.send(data_send, dest=destination_process)
    data_received = comm.recv(source=sourse_process)
    print("sending data %s " % data_send + "to process %d" % destination_process)
    print("data received is = %s" % data_received + "from process %d" % sourse_process)

# Процесс 5
if rank == 5:
    data_send = "b"
    destination_process = 1
    sourse_process = 1
    comm.send(data_send, dest=destination_process)
    data_received = comm.recv(source=sourse_process)
    print("sending data %s " % data_send + "to process %d" % destination_process)
    print("data received is = %s" % data_received + "from process %d" % sourse_process)
