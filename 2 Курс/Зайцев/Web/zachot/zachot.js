let selectTown = document.getElementById('town')
let selectHotel = document.getElementById('hotel')
let a_out = false
let data = {
    'Москва': {
        'Отель Московский': 2000,
        'Победа': 6000,
        'Гранд Хотел': 12000,
    },
    'Cанкт-Петербург': {
        'Отель Питер': 3000,
        'Академический': 5000,
        'Царский': 10000,
    }
}

function init() {
    for (let key in data) {
        selectTown.innerHTML += `<option value="${key}">${key}</option>`
    }
    for (let key in data['Москва']) {
        selectHotel.innerHTML += `<option value="${key}">${key}</option>`
    }
}

function setHotels() {
    selectHotel.innerHTML = ''
    for (let key in data[selectTown.value]) {
        selectHotel.innerHTML += `<option value="${key}">${key}</option>`
    }
}

function getSum() {
    let days = document.getElementById('days').value;
    let town = selectTown.value
    let hotel = selectHotel.value
    let output = document.getElementById('output')
    let sum = data[town][hotel] * days
    if (a_out){
        alert(`Цена: ${sum}`)
        localStorage.setItem("sum",sum.toFixed(2));
        alert("Сохранено в localStorage");
        alert(localStorage.getItem("sum"))
    }
    output.innerText = `Цена: ${sum}`
}

function toBin() {
    let number = document.getElementById('number').value;
    let output = document.getElementById('output_number')
    output.innerText = dec2bin(number)
}
function fromBin() {
    let output = document.getElementById('output_number2')
    output.innerText = document.getElementById('number').value;
}
function alert_output(){
    a_out = !a_out
}

function dec2bin(dec) {
    return (dec >>> 0).toString(2);
}
