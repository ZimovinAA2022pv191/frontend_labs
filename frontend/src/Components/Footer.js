import React, {Component} from 'react';
import {Container, Navbar, NavbarBrand} from "react-bootstrap";

let container = {
    height: "50px",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
}


class Footer extends Component {
    render() {
        return (
            <div>
                <Navbar bg="dark" variant="dark">
                    <Container>
                        <NavbarBrand>
                            <div className={ container }>
                                <div>&copy; Patter Hause</div>
                                <div>+7(930)090-14-87</div>
                            </div>
                        </NavbarBrand>
                    </Container>
                </Navbar>
            </div>
        );
    }
}

export default Footer;