running in mac os:
brew install llvm

compile as
/usr/local/opt/llvm/bin/clang++ -fopenmp -L/usr/local/opt/llvm/lib <file>.cpp   
or with
alias ocpp="/usr/local/opt/llvm/bin/clang++ -fopenmp -L/usr/local/opt/llvm/lib"
compile as
ocpp <file>.cpp   