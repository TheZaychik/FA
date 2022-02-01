var ANCESTRY_FILE = JSON.stringify([
{"bank": "VTB","money":20000,"procent":7},
{"bank": "SBER","money":10000,"procent":6.8},
{"bank": "ALPHA","money":30000,"procent":8},
{"bank": "TINK","money":15000,"procent":6.5},
{"bank": "IND","money":25000,"procent":8.5}
])

var ancestry = JSON.parse(ANCESTRY_FILE);

function sred(array) {
    let k = 0
    let sum = 0   
    array.forEach(function(person) {
        sum += person.procent
        k += 1
      });
    sum = sum/k
    return(sum)
}

function fun1() {
    let a=document.getElementById('sel1').value;
    ancestry.forEach(function(person) {
        if(a = person.bank){
            document.getElementById('tyx').value = person.money + "  "+ person.procent + "%";
        }
      });
  }

function main(){
    var rad=document.getElementsByName('viv');
        
            if (rad[0].checked) {
                alert('Средний процент вкладов: ' + sred(ancestry))
            }
            else{
                localStorage.setItem("myNumber",sred(ancestry));
                var number = parseInt(localStorage.getItem("myNumber"));
                console.log(number)
            }
        
}
