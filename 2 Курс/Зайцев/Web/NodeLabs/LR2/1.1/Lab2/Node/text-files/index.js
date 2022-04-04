const fs = require("fs").promises;

async function findSalesFiles(folderName) {
    // массив будет содержать файлы продаж по мере их обнаружения
    let salesFiles = [];

    async function findFiles(folderName) {
        // чтение всех элементов в текущей папке
        const items = await fs.readdir(folderName, { withFileTypes: true });
        // перебор каждого найденного элемента
        for (item of items) {
            // если элемент является каталогом, в нем нужно будет искать файлы
            // рекурсивно искать в этом каталоге файлы
            if (item.isDirectory()) {
                // если это папка, то этот метод вызывается снова и передается
                // рекурсивно сформированный путь к каталогу для поиска
                findFiles(`${folderName}/${item.name}`);
            }
            // Убедитесь, что обнаруженный файл является файлом sales.json
            if (item.name === "sales.json") {
                // сохранить путь к файлу в массиве salesFiles
                salesFiles.push(`${folderName}/${item.name}`);
            }
        }
    }

    // найти файлы продаж
    await findFiles(folderName);

    // вернуть массив найденных путей к файлам
    return salesFiles;
}

async function main() {
    const salesFiles = await findSalesFiles("stores");
    console.log(salesFiles);
}

main()
