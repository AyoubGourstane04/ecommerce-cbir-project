# E-commerce CBIR Project

### *Mini-Projet DataScience 2025–2026*

This repository contains a complete e-commerce web application integrating **Content-Based Image Retrieval (CBIR)**.
Instead of searching with keywords, users can upload an image, and the system retrieves visually similar products from the database.

---

## Overview

The goal of this project is to improve the online shopping experience by bridging the gap between **seeing a product** and **finding it online**.
Through deep learning and computer vision, the system analyzes an uploaded image and suggests matching products from the catalog.

---

## Key Features

* **Dynamic Home Page**
  Random products are displayed at each visit/refresh to create a discovery-like experience.

* **Visual Search Engine**
  Users can upload an image or use their camera to search for similar items.

* **Intelligent Matching System**
  A pre-trained CNN (MobileNetV2, ResNet50, etc.) extracts feature vectors used to identify visually similar products.

* **Responsive Design**
  Built with React + Bootstrap to ensure a smooth UI on all devices.

* **PostgreSQL Product Database**
  All product data and precomputed image embeddings are stored in a PostgreSQL-powered backend.

* **Separated Backend Folder**
  Backend logic (Flask API, feature extraction, similarity search) is organized in its own directory.

---

## CBIR Pipeline (How It Works)

The system follows a 4-step Content-Based Image Retrieval process:

### **1. Feature Extraction**

* Each product image is converted into a **feature vector** instead of raw pixels.
* A pre-trained CNN (MobileNetV2, ResNet50…) is used with its classification layer removed.
* This produces a compact representation capturing shapes, textures, and colors.

### **2. Processing the Query Image**

When a user uploads an image:

* The backend receives and preprocesses it.
* The CNN extracts the feature vector representing the image.

### **3. Similarity Matching**

* The query vector is compared with product vectors stored in the database.
* Metrics like **cosine similarity** or **Euclidean distance** are used.
* Matching is performed efficiently using NumPy, scikit-learn, or Faiss.

### **4. Retrieval**

* Items are ranked by similarity score.
* The most similar products are returned to the frontend.

---

## Technologies Used

### **Frontend**

* **React**
* **Bootstrap**
* Responsive UI & dynamic product grid

### **Backend**

* **Flask (Python)**
* **PostgreSQL** (product storage + embeddings)
* Dedicated `/backend` folder for API and logic

### **Computer Vision & ML**

* **TensorFlow / Keras** (CNN models: ResNet, MobileNet)
* **OpenCV** (image preprocessing)
* **NumPy** (vector computations)
* **Scikit-learn** (similarity metrics)

---

## Usage (High-Level)

* Visit the home page to browse random product suggestions.
* Upload an image or use the camera to launch a visual search.
* The system extracts features, computes similarity, and displays the closest matches.

---

