const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => res.send("Прикладная информатика"));

app.get("/users", (req, res) => {
  res.json([
    {
      id: 1,
      name: "Eldar",
    },
  ]);
});

app.get("/products", (req, res) => {
  res.json([
    {
      id: 1,
      name: "Молоко",
    },
    {
      id: 2,
      name: "Хлеб",
    },
  ]);
});

app.listen(port, () => console.log(`Приложение прослушивается на порту ${port}!`));
