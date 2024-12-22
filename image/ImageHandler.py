from PIL import Image

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None

    def load_image(self):
        try:
            self.image = Image.open(self.image_path)
            return self.image
        except FileNotFoundError:
            print(f"Error: File not found at path: {self.image_path}")
            self.image = None
            raise FileNotFoundError

    def save_image(self, save_path):
        if self.image:
            self.image.save(save_path)
        else:
            print("Изображение не загружено!")

    def convert_to_jpg(self, output_path):
        if self.image:
            rgb_image = self.image.convert('RGB')
            rgb_image.save(output_path, format='JPEG')
            print(f"Image saved as {output_path} in JPG format.")
        else:
            print("Изображение не загружено!")

    def rotate_image(self, output_path, angle=45):
        if self.image:
            rotated_image = self.image.rotate(angle, expand=True)
            rotated_image.save(output_path)
            print(f"Image rotated by {angle} degrees and saved as {output_path}.")
        else:
            print("Изображение не загружено!")

    def get_image(self):
        if self.image:
            return self.image
        else:
            print("Изображение не загружено!")
            return None
