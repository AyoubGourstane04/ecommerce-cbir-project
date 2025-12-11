import React, { useEffect, useState } from 'react';
import { Container, Spinner, Alert } from 'react-bootstrap';
import ImageUploader from './components/ImageUploader';
import ProductGrid from './components/ProductsGrid';
import { getRandomProducts, searchByImage, searchByText } from './api';

const Home = () => {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [viewTitle, setViewTitle] = useState("Recommended for You");

    useEffect(() => {
        loadRandomProducts();
    }, []);

    const loadRandomProducts = async () => {
        setLoading(true);
        try{
            const data = await getRandomProducts();
            setProducts(data);
            console.log(data);
            if(!data){
                console.log("kdjf")
            }
        } catch (err) {
            console.error("Failed to load products", err);
            setError("Could not load products. Is the backend running?");
        } finally {
            setLoading(false);
        }
    };

    const handleSearch = async (file, text) => {
        setLoading(true);
        setError(null);
        setProducts([]);

        try{
            let results;

            if(file){
                console.log("Searching by Image...");
                results = await searchByImage(file);
                setViewTitle("Visual Search Results");
            }else if(text){
                console.log("Searching by Text...");
                results = await searchByText(text);
                setViewTitle(`Results for "${text}"`);
            }

            if (results){
                setProducts(results);
            }
        }catch (err) {
            console.error("Search error:", err);
            setError("Search failed. Please try again.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <Container className="py-5">
            <h1 className="text-center mb-4">Visual E-Commerce Search</h1>

            <ImageUploader onSearch={handleSearch}/>

            {error && <Alert variant="danger" className="mt-3">{error}</Alert>}

            {loading && (
                <div className="text-center mt-5">
                    <Spinner animation="border" role="status">
                        <span className="visually-hidden">Loading...</span>
                    </Spinner>
                    <p className="mt-2">Analyzing...</p>
                </div>
            )}
            {!loading && !error && (
                <ProductGrid products={products} title={viewTitle}/>
            )}
        
        </Container>
    );
};

export default Home;