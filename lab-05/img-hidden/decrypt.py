import sys
from PIL import Image


def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""

    # Lấy bit LSB từ ảnh
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for channel in range(3):
                binary_message += format(pixel[channel], '08b')[-1]

    # Chuyển nhị phân về text
    message = ""
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        if char == '\0':  # Gặp ký tự kết thúc
            break
        message += char

    return message


def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    decoded_message = decode_image(sys.argv[1])
    print("Decoded message:", decoded_message)


if __name__ == "__main__":
    main()
