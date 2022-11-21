import React, {Component} from 'react';
import './Catalog.css'
import axios from "axios";


export default class Catalog extends Component {
    constructor(props) {
        super(props);
        this.state = {
            viewCompleted: false,
            activeItem: {
                id: 0,
                name: "",
                price: 0,
                description: "",
                type_product: 0
            },
            products: []
        };
    }

    componentDidMount() {
        axios
            .get("http://127.0.0.1:8000/api/v1/core/product")
            .then(
                (result) =>{
                    this.setState({
                        isLoaded: true,
                        products: result.data
                    });
                },
                (error) => {
                    this.setState({
                        isLoaded: true,
                        error
                    });
                }
            )
    }


    render() {
        const {error, isLoaded, products} = this.state;
        if (error){
            return <p> Error {error.message} </p>
        }else if(!isLoaded){
            return <p> Loading... </p>
        }else{
            return <div className="product">
                {products.map(product=>(
                    <li key={product.name}>
                        {product.name}
                    </li>
                ))}
            </div>
        }
    }
};