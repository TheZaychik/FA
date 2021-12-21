
        //Задание 1
        function triangle(){
            let str="Задание 1 \n";
            for(var i =1;i<8;i++){
                str+="#".repeat(i)+"\n"
                
            }
            return(str)
        }
    
        console.log(triangle());
    // document.getElementById("hello").innerHTML = triangle();
    
         //Задание 2
            
         function FizzBuzz(){
        let str="Задание 2 \n";
        for(var i =1;i<101;i++){
                if ((i % 3 ==0)&& (i % 5 !=0)){
                    str +="Fizz"+"\n"
                }
                else if ((i % 5 ==0) && (i % 3 !=0)){
                    str +="Buzz"+"\n"
                }
                else if((i % 3 ==0) && (i % 5 ==0)  ){
                    str +="FizzBuzz"+"\n"
                }
                else{
                str+=i+"\n"
                }
            }
    
            return(str)
        }
    
        console.log(FizzBuzz());
        //Задание 3
        function desk(){
        let str="Задание 3 \n";
        for(var i =1;i<9;i++){
                if (i%2==0){
                    str+=" #".repeat(4)+"\n"
                }
                else{
                    str+="# ".repeat(4)+"\n"
                }
            }
    
            return(str)
        }
    
        console.log(desk());
        //Задание 4
        function min(ch1,ch2){
        let str="Задание 4 \n";
        let min=999999;
                if (ch1<=min){
                    min=ch1;
                }
                else{
                    min=ch2;
                }
        str=min
            return(str)
        }
    
        console.log(min(2,3));
        //Задание 5
        function Countbs(stroka){
        let str="Задание 5 на число букв B \n";
        count=0;
            for(var i=0;i<stroka.length;i++){
                if ("B" == stroka[i]){
                    count++;
                }
            }
            str+=count;
            return(str)
        }
    
        console.log(Countbs("asBBdBasdBsdweB"));
        function CountChar(stroka,simv){
        let str="Задание 5 на число вводимых букв \n";
        count=0;
            for(var i=0;i<stroka.length;i++){
                if (simv == stroka[i]){
                    count++;
                }
            }
            str+=count;
            return(str)
        }
    
        console.log(CountChar("qweqweqwe","q"));
    //Задание 6
    function rang(ch1,ch2,step=1){
        var arr= []
        var new_arr=[]
        var k=0;
        let str="Задание 6 диапазон \n";
            for(var i=0;i<100;i++){
                arr[i]=i;
            }
            if (step>0){
            for(i=ch1;i<ch2+1;i=i+step){
                new_arr[k]=arr[i];
                k++;
            }
            }
            else{
                for(i=ch1;i>=ch2-1;i=i+step){
                    new_arr[k]=arr[i];
                    k++;
                } 
            }

            return(new_arr)
        }
        console.log("Задание 6 диапазон \n");
        console.log(rang(12,36,2));

        function SumArr(arr){
        let str="Задание 6 на сумму в массиве \n";
        let sum=0;
            for(var i=0;i<arr.length;i++){
                sum+=arr[i]
            }
            str+=sum;
            return(str)
        }
        let arr=[1,2,3,4,5,6,7,8,9,10]
        console.log(SumArr(arr));
 //Задание 7
 function rev(arr){
    let new_arr= []
    let k=0
        for(var i=arr.length-1;i>0-1;i--){
            new_arr[k]=arr[i]
            k++
        }
        return(new_arr)
    }
    arr=["один","два","три","четыре"]
    console.log("Задание 7 обратный порядок \n");
    console.log(rev(arr));
        

 //Задание 8
    function ListNode(x) {
        this.value = x;
        this.next = null;
      }
      
      function arrayToList(arr){
        let list = new ListNode(arr[0]);
        
        let selectedNode = list;
        for(let i = 1; i < arr.length; i++){
          selectedNode.next = new ListNode(arr[i]);
          selectedNode = selectedNode.next
        } 
      
        return list
      }
      
      arr = [1,2,3];
      
    console.log("Задание 8 массив в список \n");
    console.log(arrayToList(arr));

    var list ={
        value: 1,
        next :{
            value:2,
            next :{
                value:3,
                next:null
            }                
        }
    }


      function ListToArray(list){
        var arr = [list.value]
        while(list.next !== null){
            list = list.next;
            arr.push(list.value)
        }
        return arr;
      }
    console.log("Задание 8 список в массив \n");
    console.log(ListToArray(list));

    function prepend(el,lastList){
        
        let list = new ListNode(el);
        
        let selectedNode = list;
        selectedNode.next = lastList
      
        return list
    }

    console.log("Добавляет элемент в начало списка \n");
    console.log(prepend(5,list,pos=1));
    function nth(el,lastList,iter=0){
        iter++;
        if(iter==el){
            return lastList.value;
        }
        else if(iter>el){
            return "undefined";
        }
        else{
            return nth(el,lastList.next,iter)
        }
    }

    console.log("Ищет элемент по позиции в списке \n");
    console.log(nth(1,list));
    