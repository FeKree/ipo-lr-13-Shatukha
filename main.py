from image.ImageHandler import ImageHandler
from image.ImageProcessor import ImageProcessor
import os

def main_menu():
    print()
    print("1) Произвести конвертирование в JPG формат.")
    print("2) Повернуть изображение на 45 градусов.")
    print("3) Увеличить резкость изображения.")
    print("4) Добавить рамку к изображению (15 пикселей).")
    print("5) Сохранить полученное изображение.")
    print("6) Просмотреть изображение.")
    print("7) Завершение программы.")
    print()
    return input("Выберите действие: ")

def main():
    initial_image_path = "image_5.jpg"
    handler = ImageHandler(initial_image_path)
    try:
        handler.load_image()
        print("Изображение успешно загружено из пути:", initial_image_path)
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути: {initial_image_path}")
        return
    processor = ImageProcessor(handler.get_image())

    save_dir = "images"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    while True:
        flay = main_menu()
        if flay == "1":
            if handler.image:
                filename = os.path.basename(initial_image_path)
                name, ext = os.path.splitext(filename)
                save_path = os.path.join(save_dir, f"{name}.jpg")
                handler.convert_to_jpg(save_path)
                print(f"Изображение сконвертировано в JPG формат. Путь: {save_path}.")
            else:
                print("Изображение не загружено.")
        elif flay == "2":
            if handler.image:
                filename = os.path.basename(initial_image_path)
                name, ext = os.path.splitext(filename)
                save_path = os.path.join(save_dir, f"{name}_rotated{ext}")
                handler.rotate_image(save_path)
                processor.image = handler.get_image()
                print(f"Изображение повернуто на 45 градусов. Путь: {save_path}.")
            else:
                print("Изображение не загружено.")
        elif flay == "3":
            if handler.image:
                processor.apply_sharpen_filter()
                handler.image = processor.get_image()
                print("Фильтр резкости применён.")
            else:
                 print("Изображение не загружено.")
        elif flay == "4":
             if handler.image:
                processor.add_border()
                handler.image = processor.get_image()
                print("Рамка добавлена.")
             else:
                print("Изображение не загружено.")
        elif flay == "5":
            if handler.image:
                filename = os.path.basename(initial_image_path)
                name, ext = os.path.splitext(filename)
                save_path = os.path.join(save_dir, f"{name}_processed{ext}")
                handler.save_image(save_path)
                print(f"Изображение сохранено по пути {save_path}.")
            else:
                print("Изображение не загружено.")
        elif flay == "6":
            if handler.image:
                handler.image.show()
            else:
                print("Изображение не загружено.")
        elif flay == "7":
            print("Выход из программы.")
            break
        else:
            print("Некорректное введенное число!")
main()
