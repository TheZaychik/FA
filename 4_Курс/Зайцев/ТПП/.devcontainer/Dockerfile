FROM dhna/mpi4py

RUN groupadd -g 1000 -o user \
    && useradd -s /bin/bash -u 1000 -d /home/user -m -k /etc/skel -g 1000 user


WORKDIR /home/user

COPY . /proj

RUN chown -R user:user /home/user

USER 1000:1000

WORKDIR /home/user/proj
