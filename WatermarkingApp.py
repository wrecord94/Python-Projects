from PIL import Image, ImageFont, ImageDraw
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog
from PyQt5.QtGui import QFont


def show_file_dialog():
    # Use built-in functionality to open the file explorer and select a file
    fileName, _ = QFileDialog.getOpenFileName(None, "Upload Photo", "",
                                              "Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*)")
    # Checks if valid and then prints the file's name
    if fileName:
        print("Selected file:", fileName)
        # Call add_watermark with the selected file path
        add_watermark(fileName)


def add_watermark(file_path):
    # Location of the image
    img = Image.open(file_path)
    # size of the image
    print(img.size)
    # format of the image
    print(img.format)

    # 1. Create a copy of the original image
    img_watermark_copy = img.copy()

    # 2. Image is converted into editable form using
    # Draw function and assigned to draw
    draw = ImageDraw.Draw(img_watermark_copy)

    # ("font type", font size)
    font = ImageFont.truetype("Arial", size=100)

    # Decide the text, color, and font
    watermark_text = "WillRecord©"
    text_color = (255, 255, 255)  # White color text

    # Get the bounding box of the text
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)

    # Calculate the size of the text
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Get the size of the image
    image_width, image_height = img.size

    # Calculate the position to place the watermark in the middle
    x_position = (image_width - text_width) // 2
    y_position = (image_height - text_height) // 2

    # Draw the text at the calculated position
    draw.text((x_position, y_position), watermark_text, text_color, font=font)

    # Save or display the watermarked image
    img_watermark_copy.show()
    img_watermark_copy.save("watermarked_image.jpg")


def main():
    # ------ Set up application
    app = QApplication([])
    # ------------ Set up window
    window = QWidget()
    # Change window size
    window.setGeometry(100, 100, 200, 300)
    window.setWindowTitle("Watermarking Program")
    # ------------------ Layout
    layout = QVBoxLayout()
    # ------------------------ Label example
    label = QLabel(window)
    label.setText("Add a watermark using the button below!")
    label.setFont(QFont("Arial", 16))
    # ------------------------------ Button example
    button = QPushButton("Upload your photo here")
    button.clicked.connect(show_file_dialog)
    # ------------------ Layout add elements
    layout.addWidget(label)
    layout.addWidget(button)
    window.setLayout(layout)
    # Show the window
    window.show()
    # Run the app
    app.exec_()


if __name__ == '__main__':
    main()
