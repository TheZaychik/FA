### Installation
```bash
$ brew install llvm
```
### Running on MacOS
Compile as:
```bash
$ /usr/local/opt/llvm/bin/clang++ -fopenmp -L/usr/local/opt/llvm/lib <file>.cpp 
```

or with

```bash
alias ocpp="/usr/local/opt/llvm/bin/clang++ -fopenmp -L/usr/local/opt/llvm/lib"
```

compile and run as  
```bash
$ ocpp <file>.cpp && ./a.out   
```

### Structure
```bash
Общие задания:
sem<num>_<task>_<subtask(optional)>.cpp
Задания для самостоятельного решения:
sem<num>__<task>.cpp
```