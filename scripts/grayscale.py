import os
from PIL import Image

def convert_to_grayscale_preserving_alpha(input_folder):
    if not os.path.exists(input_folder):
        print(f"Error: Folder '{input_folder}' not found.")
        return

    print(f"Processing images in '{input_folder}'...")
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        if os.path.isfile(file_path):
            name, ext = os.path.splitext(filename)
            ext = ext.lower()

            if ext == '.png' and not name.endswith('-gray'):
                try:
                    img = Image.open(file_path)

                    if img.mode == 'RGBA':
                        gray_img = img.convert("LA")
                    elif img.mode == 'RGB':
                        gray_img = img.convert("L")
                    else:
                        print(f"  Skipping '{filename}': Unsupported image mode for grayscale conversion: {img.mode}")
                        continue

                    new_filename = f"{name}-gray{ext}"
                    new_file_path = os.path.join(input_folder, new_filename)
                    gray_img.save(new_file_path)
                    print(f"  Converted '{filename}' to '{new_filename}'")
                except IOError:
                    print(f"  Skipping '{filename}': Not a valid image file or corrupted.")
                except Exception as e:
                    print(f"  An error occurred processing '{filename}': {e}")
            elif ext == '.png' and name.endswith('-gray'):
                print(f"  Skipping '{filename}': Already a grayscale version.")
            else:
                print(f"  Skipping '{filename}': Not a PNG file.")

if __name__ == "__main__":
    folders_to_process = ["../png/"]

    for folder in folders_to_process:
        convert_to_grayscale_preserving_alpha(folder)

    print("\nGrayscale conversion complete for all specified PNG folders!")
