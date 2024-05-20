FROM dhna/mpi4py

RUN groupadd -g 20 -o user \
    && useradd -s /bin/bash -u 501 -d /home/user -m -k /etc/skel -g 20 user


WORKDIR /home/user/proj



RUN mkdir /home/user/.vscode-server
RUN mkdir /home/user/.vscode-server/extensions

RUN chown -R 501:20 /home/user/proj*
RUN chown -R 501:20 /home/user/.vscode-server*

VOLUME /home/user/.vscode-server/extensions
VOLUME /home/user/proj
USER 501:20

COPY --chown=501:20 .* /home/user/proj

RUN pip3 install ipykernel pyopencl numba numpy==1.24.4






