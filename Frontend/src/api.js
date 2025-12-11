import axios from 'axios'

const API_URL = "http://localhost:5000"


export const searchByImage = async(imageFile) => {
    const formData = new FormData()
    formData.append('file', imageFile)

    const response = await axios.post(`${API_URL}/api/search_image`, formData);
    
    return response.data
}

export const getRandomProducts = async() => {
    const response = await axios.get(`${API_URL}/api/products`);
    console.log(response.data)
    return response.data
}

export const searchByText = async(value) => {
    const formData = new FormData()
    formData.append('search_value', value)
    
    const response = await axios.post(`${API_URL}/api/search_text`, formData);

    return response.data;
}