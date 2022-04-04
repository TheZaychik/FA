const express = require('express')
const app = express()
const port = 3000

let bodyParser = require('body-parser');
const {request} = require("express");
app.use(bodyParser.json());

let products = [];

app.get('/products', (req, res) => {
    res.send(products)
})

app.post('/products', function (req, res) {
    let data = req.body
    data.id = products.length + 1
    products.push(data)
    res.send(products[products.length - 1])
});

app.put('/products', function (req, res) {
    products[req.body.id - 1].name = req.body.name
    res.send(products[req.body.id - 1])
});

app.delete('/products/:id', function (req, res) {
    const removed = products[req.body.id - 1]
    products = products.filter(item => item.id !== req.body.id)
    res.send(removed)
});

app.listen(port, () => console.log(`Прослушивание на порту ${port}!`))
  
