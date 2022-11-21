import React, {Component} from 'react';
import {
    Button,
    Container,
    FormControl,
    Navbar,
    NavLink,
    Nav,
    Form
} from "react-bootstrap";
import logo from '../assets/logo.png';


class Header extends Component {
    render() {
        return (
            <>
                <Navbar collapseOnSelect expand="md" bg="dark" variant="dark">
                    <Container>
                        <Navbar.Brand href="/">
                            <img
                                src={logo}
                                height="30"
                                width='30'
                                className="d-inline-block align-top"
                                alt="logo"
                            /> Patter Hause
                        </Navbar.Brand>
                        <Navbar.Toggle aria-controls="responsive-navbar-nav"/>
                        <Navbar.Collapse id="responsive-navbar-nav">
                            <Nav className="me-auto">
                                <NavLink className="Catalog" href="/catalog"> Каталог </NavLink>
                                <NavLink className="Contacts" href="/contacts"> Контакты </NavLink>
                                <NavLink className="About" href="/about"> О нас </NavLink>
                                <NavLink className="log" href="/login"> Войти </NavLink>
                            </Nav>
                            <Form inline>
                                <FormControl
                                    type="text"
                                    placeholder="Поиск..."
                                    className={"me-3"}
                                />
                            </Form>
                            <Button variant="outline-info" className={'ms-2'}>Найти</Button>
                        </Navbar.Collapse>
                    </Container>
                </Navbar>
            </>
        );
    }
}

export default Header;