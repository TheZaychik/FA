const http = require('http');

const productToDelete = {
  id: 1
}
const data = JSON.stringify(productToDelete)

const options = {
  hostname: 'localhost',
  port: 3000,
  path: `/products/${productToDelete.id}`,
  method: 'DELETE',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': data.length
  }
}

const request = http.request(options, (res) => {
  let body = '';
  res.on('data', (chunk) => { body += "" + chunk; })
  res.on('error', (err) => console.error('Ошибка:', err))
  res.on('end', () => { console.log('Ответ:', body) })
  res.on('close', () => { console.log('Соединение закрыто') })
})

request.end(data);
