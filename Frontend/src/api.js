import axios from 'axios'

API_URL = "http://localhost:5000"


export const searchByImage = async(imageFile) => {
    const formData = new FormData()
    formData.append('file', imageFile)

    const response = await axios.post(`${API_URL}/api/search_image`, formData, {
        headers: {'Content-Type' : 'multipart/form-data'}
    });
    
    return response.data
}

export const getRandomProducts = async() => {
    const response = await axios.post(`${API_URL}/api/products`);
    return response.data
}