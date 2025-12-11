import React, { useState } from "react";
import { Form, Button, Image } from "react-bootstrap";

const ImageUploader = ({onSearch}) => {
    const [preview, setPreview] = useState(null);
    const [selectedFile, setSelectedFile] = useState(null);
    const [searchQuery, setSearchQuery] = useState("");

    const handleFileChange = (e) => {
        const file = e.target.files[0];
        if(file){
            setSelectedFile(file);
            setPreview(URL.createObjectURL(file));
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if(selectedFile || searchQuery.trim()){
            onSearch(selectedFile, searchQuery);
        }
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
                            onChange={handleFileChange}
                            accept="image/*"
                        />
                    </Form.Label>
                </Form.Group>
                {preview &&  (
                    <div className="mb-3">
                        <Image src={preview} thumbnail width={150}/>
                    </div>
                )}

                <Button
                    variant="success"
                    type="submit"
                    disabled={!selectedFile && ! searchQuery.trim()}
                >
                🔍 Search   
                </Button>
            </Form>
        </div>
    );
};

export default ImageUploader;