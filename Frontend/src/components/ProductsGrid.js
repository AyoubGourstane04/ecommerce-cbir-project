import React from "react";
import { Card, Col, Row, Button } from 'react-bootstrap';

const ProductGrid = ({products, title}) => {
    return (
        <div className="my-4">
            <h3>{title}</h3>
            <Row xs={1} md={3} lg={4} className="g-4">
                {products.map((product, idx) =>(
                    <Col key={idx}>
                        <Card className="h-100 shadow-sm">
                            {/* {console.log(product.image_path)} */}
                            <Card.Img variant="top" src={`http://localhost:5000/${product.image_path}`}/>
                            <Card.Body>
                                <Card.Title>{product.name || `Item #${idx}`}</Card.Title>
                                <Card.Text>{product.price || '0.00'} DH</Card.Text>
                                <Button variant="primary">View Details</Button>
                            </Card.Body>
                        </Card>
                    </Col>
                ))}
            </Row>
        </div>
    );
};

export default ProductGrid;