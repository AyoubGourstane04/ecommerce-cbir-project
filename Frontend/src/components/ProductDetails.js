import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";

const ProductDetails = () => {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [quantity, setQuantity] = useState(1);

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        setLoading(true);
        const response = await fetch(`http://localhost:5000/product/${id}`);
        if (!response.ok) throw new Error("Failed to fetch product");
        const data = await response.json();
        setProduct(data);
        setError(null);
      } catch (err) {
        setError(err.message);
        console.error("Error fetching product:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchProduct();
  }, [id]);

  const handleAddToCart = () => {
    console.log(`Added ${quantity} of ${product.name} to cart`);
    // Add your cart logic here
  };

  if (loading) {
    return (
      <div className="container mt-5">
        <div className="row justify-content-center">
          <div className="col-md-8">
            <div className="text-center py-5">
              <div className="spinner-border text-primary" role="status">
                <span className="visually-hidden">Loading...</span>
              </div>
              <p className="mt-3">Loading product details...</p>
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (error || !product) {
    return (
      <div className="container mt-5">
        <div className="row justify-content-center">
          <div className="col-md-6">
            <div className="alert alert-danger">
              <h4 className="alert-heading">Error!</h4>
              <p>{error || "Product not found"}</p>
              <hr />
              <Link to="/" className="btn btn-outline-danger">
                ← Back to Products
              </Link>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="container py-5">
      {/* Container for both Breadcrumb and Button */}
      <div className="d-flex justify-content-between align-items-center mb-4">
        {/* Breadcrumb */}
        <nav aria-label="breadcrumb" className="m-0">
          <ol className="breadcrumb m-0">
            <li className="breadcrumb-item">
              <Link to="/" className="text-decoration-none">Home</Link>
            </li>
            <li className="breadcrumb-item active" aria-current="page">
              {product.name}
            </li>
          </ol>
        </nav>

        {/* Back Button (No extra margin needed here) */}
        <div>
            <Link to="/" className="btn btn-outline-secondary">
              <i className="bi bi-arrow-left me-2"></i>
              Back to Home
            </Link>
        </div>
      </div>

      <div className="row">
        {/* Product Image */}
        <div className="col-md-6 mb-4">
          <div className="card shadow-sm">
            <div className="card-body p-4">
              <img
                src={`http://localhost:5000/${product.image_path}`}
                alt={product.name}
                className="img-fluid rounded"
                style={{ maxHeight: "500px", objectFit: "contain" }}
              />
            </div>
          </div>
        </div>

        {/* Product Details */}
        <div className="col-md-6">
          <div className="card shadow-sm">
            <div className="card-body p-4">
              {/* Product Name */}
              <h1 className="h2 mb-3">{product.name}</h1>

              {/* Price */}
              <div className="mb-4">
                <h2 className="h3 text-primary mb-2">
                  {product.price} DH
                </h2>
              </div>

              {/* Description */}
              <div className="mb-4">
                <h5 className="mb-3">Description</h5>
                <p className="text-muted">{product.description}</p>
              </div>

              {/* Add to Cart Button */}
              <div className="mb-4">
                <button
                  className="btn btn-primary btn-lg w-100 py-3"
                  onClick={handleAddToCart}
                >
                  <i className="bi bi-cart-plus me-2"></i>
                  Add to Cart
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>


    </div>
  );
};

export default ProductDetails;