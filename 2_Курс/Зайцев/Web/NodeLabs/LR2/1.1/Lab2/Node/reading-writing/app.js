const express = require('express')
const app = express()
const port = 3000

let bodyParser = require('body-parser');
app.use(bodyParser.json());

let products = [];

app.get('/products', (req, res) => {
  // *РЕАЛИЗОВАТЬ*
})

app.post('/products', function (req, res) {
  // *РЕАЛИЗОВАТЬ*
});

app.put('/products', function (req, res) {
  // *РЕАЛИЗОВАТЬ*
});

app.delete('/products/:id', function (req, res) {
  // *РЕАЛИЗОВАТЬ*
});

app.listen(port, () => console.log(`Прослушивание на порту ${port}!`))
  
