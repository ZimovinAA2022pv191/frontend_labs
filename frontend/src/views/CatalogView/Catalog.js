import React, {Component} from 'react';
import './Catalog.css'
import axios from "axios";
import picture1 from "../../assets/conditioners/Рисунок1.jpeg"
import {Button, Container} from "react-bootstrap";

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
            return <Container style={{width: '800px'}}>
                {products.map(product=>(
                    <div className="catalog-list" key={product.name}>
                        <div className="image-div">
                             <img src={picture1} className="img-settings"/>
                        </div>

                        <div className="about">
                            <div className="catalog-name">
                                {product.name}
                            </div>
                            <div className="about-price"></div>
                            <div>
                                {product.price}₽
                                <div>{(product.price/12).toFixed()}₽/мес.</div>
                            </div>
                            <div className="about-price">
                                <div className="in-stock">{product.description}</div>
                                <Button variant="primary" type="submit" className={"my-btn"}>Купить</Button>
                            </div>
                        </div>
                    </div>
                ))}
            </Container>
        }
    }
};