import os
import settings
import shutil
import zipfile


class FileManager:
    def __init__(self, root_dir):
        self.ROOT_DIR = root_dir
        os.path = root_dir

    def show_dir(self):
        for f in os.scandir(os.path):
            if f.is_dir():
                print('<dir> -', f.name)
            else:
                print('<file> -', f.name)

    def create_dir(self):
        print('Введите название папки')
        dirname = input()
        os.mkdir(f'{os.path}/{dirname}', 777)

    def delete_dir(self):
        print('Введите название папки')
        dirname = input()
        os.rmdir(f'{os.path}/{dirname}')

    def change_dir(self):
        print('Введите название папки или ..')
        dirname = input()
        os.chdir(f'{os.path}/{dirname}')
        if self.ROOT_DIR in os.getcwd():
            os.path = os.getcwd()
        else:
            os.chdir(self.ROOT_DIR)
            os.path = os.getcwd()
            print('Запрещенная директория!')

    def create_file(self):
        print('Введите название файла')
        filename = input()
        f = open(f'{os.path}/{filename}', 'w')
        f.close()

    def read_file(self):
        print('Введите название файла для чтения')
        filename = input()
        if os.path.exists(f'{os.path}/{filename}'):
            with open(f'{os.path}/{filename}', 'r') as f:
                for line in f.readlines():
                    print(line)
        else:
            print('Файла не существует')

    def write_file(self):
        print('Введите название файла для записи')
        filename = input()
        if os.path.exists(f'{os.path}/{filename}'):
            with open(f'{os.path}/{filename}', 'w') as f:
                print('Построчная запись. Для остановки пропишите input_stop')
                line = input()
                while line != 'input_stop':
                    f.write(line + '\n')
                    line = input()
        else:
            print('Файла не существует')

    def delete_file(self):
        print('Введите название файла')
        filename = input()
        if os.path.exists(f'{os.path}/{filename}'):
            os.remove(f'{os.path}/{filename}')
        else:
            print('Файла не существует')

    def copy_file(self):
        print('Введите название копируемого файла и итогового файла через пробел')
        filename, cp_name = input().split(' ')
        if os.path.exists(f'{os.path}/{filename}'):
            shutil.copy2(f'{os.path}/{filename}', f'{os.path}/{cp_name}')
        else:
            print('Файла не существует')

    def move_file(self):
        print('Введите название перемещаемого файла и итоговой директории через Enter')
        filename = input()
        mv_dirname = input()
        if os.path.exists(f'{os.path}/{filename}'):
            shutil.move(f'{os.path}/{filename}', f'{mv_dirname}/{filename}')
        else:
            print('Файла не существует')

    def rename_file(self):
        print('Введите название файла и его новое имя через пробел')
        filename, new_filename = input().split(' ')
        if os.path.exists(f'{os.path}/{filename}'):
            shutil.move(f'{os.path}/{filename}', f'{os.path}/{new_filename}')
        else:
            print('Файла не существует')

    def create_zip(self):
        print('Введите название архива')
        zip_name = input()
        print('Введите название файла(-ов) для архивации через пробел')
        files = input().split(' ')
        zip_file = zipfile.ZipFile(f'{os.path}/{zip_name}.zip', 'w')
        for f in files:
            zip_file.write(f'{os.path}/{f}', compress_type=zipfile.ZIP_DEFLATED)
        zip_file.close()

    def unpack_zip(self):
        print('Введите название архива')
        zip_name = input()
        zip_file = zipfile.ZipFile(f'{os.path}/{zip_name}')
        zip_file.extractall(f'{os.path}')
        zip_file.close()

    def main(self):
        while True:
            print('Директория:', os.path, '\n------------------------')
            self.show_dir()
            print('\n------------------------\n'
                  'Команды:\n1. Создать папку\n2. Удалить папку\n3. Переход по папкам\n4. Создать файл\n'
                  '5. Записать текст в файл\n6. Чтение из файла\n7. Удалить файл\n8. Скопировать файл\n'
                  '9. Переместить файл\n10. Переименовать файл\n11. Создать архив\n12. Разархивировать файл\n'
                  '13. Выход')
            cmd = input()
            if cmd == '1':
                self.create_dir()
            elif cmd == '2':
                self.delete_dir()
            elif cmd == '3':
                self.change_dir()
            elif cmd == '4':
                self.create_file()
            elif cmd == '5':
                self.write_file()
            elif cmd == '6':
                self.read_file()
            elif cmd == '7':
                self.delete_file()
            elif cmd == '8':
                self.copy_file()
            elif cmd == '9':
                self.move_file()
            elif cmd == '10':
                self.rename_file()
            elif cmd == '11':
                self.create_zip()
            elif cmd == '12':
                self.unpack_zip()
            elif cmd == '13':
                break
            else:
                print('Неверная команда!')


if __name__ == '__main__':
    FileManager(settings.ROOT_DIR).main()
