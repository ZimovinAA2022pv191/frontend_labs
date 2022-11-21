import React, {Component} from 'react';
import Carousel from 'react-bootstrap/Carousel';
import forest1Img from '../assets/slider/forest1.jpg';
import forest2Img from '../assets/slider/forest2.jpg';
import "./SliderBox.css"


class SliderBox extends Component {
    render() {
        return (
            <div>
                <Carousel>
                    <Carousel.Item>
                        <img
                            className="d-block w-100 slider"
                            src={forest1Img}
                            alt="Forest1"
                        />
                        <Carousel.Caption>
                            <h3>Forest Image 1</h3>
                        </Carousel.Caption>
                    </Carousel.Item>
                    <Carousel.Item>
                        <img
                            className="d-block w-100 slider"
                            src={forest2Img}
                            alt="Forest2"
                        />
                        <Carousel.Caption>
                            <h3>Forest Image 2</h3>
                        </Carousel.Caption>
                    </Carousel.Item>
                    <Carousel.Item>
                        <img
                            className="d-block w-100 slider"
                            src={forest1Img}
                            alt="Forest1"
                        />
                        <Carousel.Caption>
                            <h3>Forest Image 3</h3>
                        </Carousel.Caption>
                    </Carousel.Item>
                </Carousel>
            </div>
        );
    }
}

export default SliderBox;