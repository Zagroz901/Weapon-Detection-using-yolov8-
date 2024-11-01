# Weapon Detection with YOLOv8 and FastAPI

This project is a weapon detection system built with **YOLOv8** for detecting weapons in images. The system uses **FastAPI** as a backend server, **OpenCV** to draw bounding boxes around detected objects, and a simple HTML frontend for uploading images and displaying results.

## Features

- Upload an image for weapon detection.
- Display bounding boxes around detected weapons.
- Show labels and confidence scores for each detected weapon.
- Real-time response with FastAPI and YOLOv8.

## Prerequisites

Ensure you have the following installed:

- **Python 3.7+**
- **Git** (optional, for cloning the repository)

## Installation

1. **Clone the repository**:
   ```bash
   git clone [URL]
   cd [NAME-OF-DIR]
   ```

2. **Set up a virtual environment (optional but recommended)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   The main dependencies are:
   - **FastAPI**: To create the API for uploading images and returning results.
   - **Uvicorn**: A server to run the FastAPI app.
   - **Torch** and **Ultralytics**: For YOLOv8 and PyTorch support.
   - **OpenCV** and **Pillow**: To handle images and draw bounding boxes.

4. **Download the YOLOv8 model weights**:
   - Place your model weights file (e.g., `weapon_weight.pt`) in the `app/Weights/` folder.
   - If you don’t have a weights file, you may need to train a model with YOLOv8 or obtain a pre-trained model.

## Project Structure

```plaintext
weapon-detection-yolov8/
├── app/
│   ├── model.py            # YOLOv8 model loading and prediction code
│   ├── main.py             # FastAPI app and endpoints
│   ├── templates/
│   │   └── index.html      # Frontend webpage for uploading images
│   └── Weights/
│       └── weapon_weight.pt # YOLOv8 model weights (add your model here)
├── requirements.txt        # Project dependencies
└── README.md               # Documentation (this file)
```

## Usage

1. **Run the FastAPI Application**:
   Start the server using Uvicorn:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

   The server will start at `http://localhost:8000`.

2. **Open the Webpage**:
   Go to `http://localhost:8000` in your browser.

3. **Upload an Image**:
   - Use the file upload feature on the page to upload an image.
   - Click "Detect Weapon" to see the image with bounding boxes and labels displayed.

4. **Results**:
   - The processed image with bounding boxes around detected weapons will be shown on the page.
   - Each detected object will display a label and confidence score.

## Example

Here’s what the output might look like:

- **Original Image**: The user uploads an image of a scene with a weapon.
- **Detected Image**: The page displays the image with boxes drawn around each detected weapon, showing the label (e.g., "pistol") and confidence score.

## Troubleshooting

- **YOLOv8 Model Compatibility**: Ensure that your model weights are compatible with YOLOv8.
- **CORS Issues**: If you encounter CORS errors, double-check your FastAPI CORS settings in `main.py`.
- **Dependency Issues**: Use the specified versions in `requirements.txt` to avoid compatibility issues.

## License

This project is open source and available under the MIT License.

## Contributing

If you’d like to contribute, feel free to fork the repository and submit a pull request.

## Acknowledgments

- [YOLOv8 by Ultralytics](https://ultralytics.com/yolov8) for object detection.
- [FastAPI](https://fastapi.tiangolo.com/) for the API framework.
- [OpenCV](https://opencv.org/) for image processing.
