# CBIR-Based E-Commerce Platform

A full-stack e-commerce platform integrating **Content-Based Image Retrieval (CBIR)**, allowing users to search for products simply by uploading an image. The system identifies visual features in the uploaded image and returns similar products from the database.

---

## What the Platform Does

Users can:

* Upload or take a picture of an item
* View visually similar products retrieved automatically
* Browse dynamically displayed items on the homepage

The backend extracts deep visual features from images, compares them with stored product vectors, and returns the closest matches that exist in the catalog.

---

## System Architecture Overview

The project is designed around a separation of concerns:

### Backend-Image (Flask)

Responsible for:

* Image processing
* Feature extraction using **MobileNetV2**
* Matching using similarity metrics (cosine and Euclidean)
* Returning ranked product image results

Pre-extracted features and corresponding image paths are stored for fast similarity search.

---

### Backend-DB (PostgreSQL Integration)

Responsible for:

* Persistent storage of product metadata
* Product listing
* Associating extracted images with product entities
* Returning information-rich product objects to the frontend

This layer allows data consistency and future extensibility (categories, price, user preferences, etc.).

---

### Frontend (React)

Responsible for:

* Image upload UI
* Camera access capability
* Dynamic homepage recommendations
* Grid-based product visualization
* Displaying similarity scores

Built with React and styled using Bootstrap and custom CSS.

---

## Project Structure (High-Level)

```
ecommerce-cbir-project/
├── backend-image/      # Feature extraction and similarity engine
├── backend-db/         # PostgreSQL data backend and product services
└── frontend/           # UI and display logic
```

Each folder is modular and can run independently, allowing future deployment flexibility.

---

## Core System Workflow

1. User uploads or captures an image
2. Flask backend extracts the feature vector
3. It computes similarity against pre-indexed vectors
4. Best matches are sent back to the frontend
5. The frontend queries the PostgreSQL backend
6. Product metadata is added to the results
7. Results are displayed in a responsive grid

This hybrid approach allows both:

✔ **deep visual similarity**, and
✔ **structured product information**

---

## Technology Overview

### Backend-Image

* Flask
* TensorFlow/Keras (MobileNetV2)
* NumPy
* OpenCV & Pillow

### Backend-DB

* PostgreSQL
* ORM (SQLAlchemy or equivalent)

### Frontend

* React
* Axios
* Bootstrap
* Custom CSS components

---

## Main Advantages of the Platform

* Image-based product search (no keywords needed)
* Modular architecture
* Real database integration instead of static files
* Mobile-friendly UI
* Extensible for:

  * recommendation engines
  * multi-category catalogs
  * user personalization

---

**Built to showcase practical CBIR usage in a real e-commerce context, combining AI vision, data storage, and clean UI interaction.**
