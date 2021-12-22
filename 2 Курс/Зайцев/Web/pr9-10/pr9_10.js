var ANCESTRY_FILE = JSON.stringify([
    {"name": "Carolus Haverbeke", "sex": "m", "born": 1832, "died": 1905, "father": "Carel Haverbeke", "mother": "Maria van Brussel"},
    {"name": "Emma de Milliano", "sex": "f", "born": 1876, "died": 1956, "father": "Petrus de Milliano", "mother": "Sophia van Damme"},
    {"name": "Maria de Rycke", "sex": "f", "born": 1683, "died": 1724, "father": "Frederik de Rycke", "mother": "Laurentia van Vlaenderen"},
    {"name": "Jan van Brussel", "sex": "m", "born": 1714, "died": 1748, "father": "Jacobus van Brussel", "mother": "Joanna van Rooten"},
    {"name": "Philibert Haverbeke", "sex": "m", "born": 1907, "died": 1997, "father": "Emile Haverbeke", "mother": "Emma de Milliano"},
    {"name": "Jan Frans van Brussel", "sex": "m", "born": 1761, "died": 1833, "father": "Jacobus Bernardus van Brussel", "mother":null},
    {"name": "Pauwels van Haverbeke", "sex": "m", "born": 1535, "died": 1582, "father": "N. van Haverbeke", "mother":null},
    {"name": "Clara Aernoudts", "sex": "f", "born": 1918, "died": 2012, "father": "Henry Aernoudts", "mother": "Sidonie Coene"},
    {"name": "Emile Haverbeke", "sex": "m", "born": 1877, "died": 1968, "father": "Carolus Haverbeke", "mother": "Maria Sturm"},
    {"name": "Lieven de Causmaecker", "sex": "m", "born": 1696, "died": 1724, "father": "Carel de Causmaecker", "mother": "Joanna Claes"},
    {"name": "Pieter Haverbeke", "sex": "m", "born": 1602, "died": 1642, "father": "Lieven van Haverbeke", "mother":null},
    {"name": "Livina Haverbeke", "sex": "f", "born": 1692, "died": 1743, "father": "Daniel Haverbeke", "mother": "Joanna de Pape"},
    {"name": "Pieter Bernard Haverbeke", "sex": "m", "born": 1695, "died": 1762, "father": "Willem Haverbeke", "mother": "Petronella Wauters"},
    {"name": "Lieven van Haverbeke", "sex": "m", "born": 1570, "died": 1636, "father": "Pauwels van Haverbeke", "mother": "Lievijne Jans"},
    {"name": "Joanna de Causmaecker", "sex": "f", "born": 1762, "died": 1807, "father": "Bernardus de Causmaecker", "mother":null},
    {"name": "Willem Haverbeke", "sex": "m", "born": 1668, "died": 1731, "father": "Lieven Haverbeke", "mother": "Elisabeth Hercke"},
    {"name": "Pieter Antone Haverbeke", "sex": "m", "born": 1753, "died": 1798, "father": "Jan Francies Haverbeke", "mother": "Petronella de Decker"},
    {"name": "Maria van Brussel", "sex": "f", "born": 1801, "died": 1834, "father": "Jan Frans van Brussel", "mother": "Joanna de Causmaecker"},
    {"name": "Angela Haverbeke", "sex": "f", "born": 1728, "died": 1734, "father": "Pieter Bernard Haverbeke", "mother": "Livina de Vrieze"},
    {"name": "Elisabeth Haverbeke", "sex": "f", "born": 1711, "died": 1754, "father": "Jan Haverbeke", "mother": "Maria de Rycke"},
    {"name": "Lievijne Jans", "sex": "f", "born": 1542, "died": 1582, "father":null, "mother":null},
    {"name": "Bernardus de Causmaecker", "sex": "m", "born": 1721, "died": 1789, "father": "Lieven de Causmaecker", "mother": "Livina Haverbeke"},
    {"name": "Jacoba Lammens", "sex": "f", "born": 1699, "died": 1740, "father": "Lieven Lammens", "mother": "Livina de Vrieze"},
    {"name": "Pieter de Decker", "sex": "m", "born": 1705, "died": 1780, "father": "Joos de Decker", "mother": "Petronella van de Steene"},
    {"name": "Joanna de Pape", "sex": "f", "born": 1654, "died": 1723, "father": "Vincent de Pape", "mother": "Petronella Wauters"},
    {"name": "Daniel Haverbeke", "sex": "m", "born": 1652, "died": 1723, "father": "Lieven Haverbeke", "mother": "Elisabeth Hercke"},
    {"name": "Lieven Haverbeke", "sex": "m", "born": 1631, "died": 1676, "father": "Pieter Haverbeke", "mother": "Anna van Hecke"},
    {"name": "Martina de Pape", "sex": "f", "born": 1666, "died": 1727, "father": "Vincent de Pape", "mother": "Petronella Wauters"},
    {"name": "Jan Francies Haverbeke", "sex": "m", "born": 1725, "died": 1779, "father": "Pieter Bernard Haverbeke", "mother": "Livina de Vrieze"},
    {"name": "Maria Haverbeke", "sex": "m", "born": 1905, "died": 1997, "father": "Emile Haverbeke", "mother": "Emma de Milliano"},
    {"name": "Petronella de Decker", "sex": "f", "born": 1731, "died": 1781, "father": "Pieter de Decker", "mother": "Livina Haverbeke"},
    {"name": "Livina Sierens", "sex": "f", "born": 1761, "died": 1826, "father": "Jan Sierens", "mother": "Maria van Waes"},
    {"name": "Laurentia Haverbeke", "sex": "f", "born": 1710, "died": 1786, "father": "Jan Haverbeke", "mother": "Maria de Rycke"},
    {"name": "Carel Haverbeke", "sex": "m", "born": 1796, "died": 1837, "father": "Pieter Antone Haverbeke", "mother": "Livina Sierens"},
    {"name": "Elisabeth Hercke", "sex": "f", "born": 1632, "died": 1674, "father": "Willem Hercke", "mother": "Margriet de Brabander"},
    {"name": "Jan Haverbeke", "sex": "m", "born": 1671, "died": 1731, "father": "Lieven Haverbeke", "mother": "Elisabeth Hercke"},
    {"name": "Anna van Hecke", "sex": "f", "born": 1607, "died": 1670, "father": "Paschasius van Hecke", "mother": "Martijntken Beelaert"},
    {"name": "Maria Sturm", "sex": "f", "born": 1835, "died": 1917, "father": "Charles Sturm", "mother": "Seraphina Spelier"},
    {"name": "Jacobus Bernardus van Brussel", "sex": "m", "born": 1736, "died": 1809, "father": "Jan van Brussel", "mother": "Elisabeth Haverbeke"}
  ])
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

    //Задание 9
    function deepEqual(obj1, obj2) {
        if (obj1 === obj2) {
            return true;
        }
     
        if (obj1 == null || typeof(obj1) != "object" || obj2 == null || typeof(obj2) != "object")
        {
            return false;
        }
     
        var kolsvForObj1 = 0, kolsvForObj2 = 0;
        for (var kolsv in kolsvForObj1) {
            kolsvForObj1 += 1;
        }
        for (var kolsv in obj2) {
            kolsvForObj2 += 1;
            if ((kolsv in obj1)==false || deepEqual(obj1[kolsv], obj2[kolsv])==false) {
                return false;        
            }
        }        
        return kolsvForObj1 == kolsvForObj1;
    }
    var obj = {one: {this: "qweqwe"}, two: 2};

    console.log("Задание 9 глубокое сравнение \n");
    console.log(deepEqual(obj, obj)); 
    console.log(deepEqual(obj, {this: 1, two: 2}));
    console.log(deepEqual(obj, {one: {this: "qweqwe"}, two: 2}));
     //Задание 10
     function conc(arr) {
        var new_arr=[]
        new_arr=arr.reduce(function(a, b) {return a.concat(b);});
        return(new_arr)
    }
    arr=[[1,2,3],[4,5,6]]
    console.log("Задание 10 свертка \n");

    console.log(conc(arr));
    //Задание 13

    function every(arr, isEvery) {
        for (i = 0; i < arr.length; i++) {
          if (!isEvery(arr[i])) {
            return false;
          }
        }
        return true;
      }
      
      function some(array, isSome) {
        for (i = 0; i < array.length; i++) {
          if (isSome(array[i])) {
            return true;
          }
        }
        return false; 
      }
       
       
      
    console.log("Задание 13 every и some \n");
      console.log(every(["aasd", "qweqwe", "asdqwe"], isNaN));
      // → true
      console.log(every(["123", "adasd", 4123], isNaN));
      // → false
      console.log(some(["asd", 123, 3453], isNaN));
      // → true
      console.log(some([234, "1234", 1234], isNaN));
      // → false  

    //Задание 11
    var ancestry = JSON.parse(ANCESTRY_FILE);

    function average(array) {
    function plus(a, b) { return a + b; }
    return array.reduce(plus) / array.length;
    }

    var byName = {};
    ancestry.forEach(function(person) {
    byName[person.name] = person;
    });

    var diff = ancestry.filter(
    function(person) {
        return byName[person.mother] != null;
    }).map(
        function(person) {
        return person.born - byName[person.mother].born
        });

    console.log("Задание 11 средняя разница в возрасте между матерями и детьми \n");
    console.log(average(diff).toFixed(1));
    //Задание 12
      function groupBy(array, centryGroup) {
        var groups = {};
        array.forEach(function(person) {
          var centryName = centryGroup(person);
          if (centryName in groups) {
            groups[centryName].push(person.died - person.born);
          }
          else {
            groups[centryName] = [person.died - person.born];
          }
        });
        return groups;
      }
      
      var resGroup = groupBy(ancestry, function(person) {
        return Math.ceil(person.died / 100);
      });
      
    console.log("Задание 12 продолжительность жизни \n");
      for (arr in resGroup) {
        console.log(arr + ': ' + average(resGroup[arr]).toFixed(1));  
      }
