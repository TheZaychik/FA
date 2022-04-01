const express = require("express");
const app = express();
const port = 3000;

const products = [
  {
    id: 1,
    name: "Изучаем OpenCV 3",
    author: "Келер Адриан",
  },
  {
    id: 2,
    name: "Полный справочник по C++",
    author: "Герберт Шилдт",
  },
  {
    id: 3,
    name: "Глубокое обучение",
    author: "Бенджио Иошуа",
  },
];

app.get("/", (req, res) => res.send("Работает API!"));

app.get("/products/:id", (req, res) => {});

app.get("/products", (req, res) => {});

app.listen(port, () => console.log(`Прослушивается на порту ${port}!`));
