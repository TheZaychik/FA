from mpi4py import MPI

# определяем коммуникатор comm – группу процессов, которые участвуют в вычислениях
comm = MPI.COMM_WORLD
# rank применяется для указания номера процесса
rank = comm.Get_rank()
print("my rank is : " , rank)

# Для процесса rank, равного 0, устанавливаем destination_process и data (в данном случае data = 10000000) 
# для отправки в процесс-получатель (в данном случае destination_process = 4)
# Применяем функцию comm.send для отправки установленных ранее данных в процесс-получатель
# Процесс 0 отправляет 10000000 процессу 4
# Выводим на печать 
if rank==0: 
    data= 10000000 
    destination_process = 4
    comm.send(data,dest=destination_process, tag=0) 
    print ("sending data %s " %data + "to process %d" %destination_process)

# Процесс 1 отправляет hello процессу 8
if rank==1: 
    destination_process = 8 
    data= "hello" 
    comm.send(data,dest=destination_process) 
    print ("sending data %s :" %data + "to process %d" %destination_process)

# Процесс 4 получает данные в переменную data от процесса 0
# Печать полученных от процесса 0 данных
if rank==4: 
    data=comm.recv(source=0)
    print ("data received from process 0 is = %s" %data)

# Процесс 8 получает данные в переменную data от процесса 1
# Печать полученных от процесса 1 данных
if rank==8: 
    data=comm.recv(source=1)
    print ("data received from process 1 is = %s" %data)

