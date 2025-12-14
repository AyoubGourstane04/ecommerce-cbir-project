import React, { useState } from "react";
import { Form, Button, Image } from "react-bootstrap";

const ImageUploader = ({ onSearch }) => {
    const [preview, setPreview] = useState(null);
    const [selectedFile, setSelectedFile] = useState(null);
    const [searchQuery, setSearchQuery] = useState("");

    const handleFileChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            setSelectedFile(file);
            setPreview(URL.createObjectURL(file));
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (selectedFile || searchQuery.trim()) {
            onSearch(selectedFile, searchQuery);
        }
    };

    const handleClear = () => {
        setPreview(null);
        setSelectedFile(null);
        setSearchQuery("");
    };

    return (
        <div className="text-center p-5 bg-light border rounded">
            <h4>Search Product</h4>
            <Form onSubmit={handleSubmit}>
                <Form.Group className="mb-3">
                    <Form.Control
                        type="text"
                        placeholder="Search by product name..."
                        value={searchQuery}
                        onChange={(e) => setSearchQuery(e.target.value)}
                    />
                </Form.Group>
                
                <div className="text-muted mb-2">- OR -</div>
                
                <Form.Group className="mb-3">
                    <Form.Label className="btn btn-outline-secondary w-100">
                        📷 Upload Image for Visual Search
                        <Form.Control
                            type="file"
                            hidden
                            key={selectedFile ? "file-selected" : "file-empty"} 
                            onChange={handleFileChange}
                            accept="image/*"
                        />
                    </Form.Label>
                </Form.Group>

                {preview && (
                    <div className="mb-3 position-relative d-inline-block">
                        <Image src={preview} thumbnail width={150} />
                        <Button 
                            variant="danger" 
                            size="sm" 
                            className="position-absolute top-0 start-100 translate-middle rounded-circle"
                            onClick={() => {
                                setPreview(null);
                                setSelectedFile(null);
                            }}
                            style={{ width: '24px', height: '24px', padding: 0, lineHeight: '1' }}
                        >
                            &times;
                        </Button>
                    </div>
                )}

                <div className="d-flex gap-2 justify-content-center">
                    <Button
                        variant="success"
                        type="submit"
                        disabled={!selectedFile && !searchQuery.trim()}
                    >
                        🔍 Search
                    </Button>

                    {/* Main Clear Button */}
                    {(selectedFile || searchQuery) && (
                        <Button
                            variant="outline-danger"
                            type="button"
                            onClick={handleClear}
                        >
                            ✕ Clear
                        </Button>
                    )}
                </div>
            </Form>
        </div>
    );
};

export default ImageUploader;