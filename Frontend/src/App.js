import React from 'react';
import Home from './home';
import ProductDetails from './components/ProductDetails';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={ <Home />}/>
          <Route path="/product/:id" element={ <ProductDetails />}/>          
        </Routes>
      </div>
    </Router>
  
  );
}

export default App;