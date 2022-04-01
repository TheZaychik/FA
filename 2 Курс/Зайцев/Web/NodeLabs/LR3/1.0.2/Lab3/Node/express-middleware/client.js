const http = require("http");

http.get(
  {
    port: 3000,
    hostname: "localhost",
    path: "/users",
    headers: {},
  },
  (res) => {
    console.log("Соединение");
    res.on("data", (chunk) => {
      console.log("Данные: " + chunk);
    });
    res.on("end", () => {
      console.log("Нет больше данных");
    });
    res.on("close", () => {
      console.log("Разрыв соединения");
    });
  }
);
