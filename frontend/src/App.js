import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Header from "./Components/Header";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Home from "./views/Home";
import About from "./views/About";
import Contacts from "./views/Contacts";
import Catalog from "./views/CatalogView/Catalog";
import Login from "./views/Login";
import Footer from "./Components/Footer";

function App() {
    return (
        <div>
            <div className="wrapper">
                <Header/>
                <BrowserRouter>
                    <Routes>
                        <Route path="/" element={<Home/>}/>
                        <Route path="/about" element={<About/>}/>
                        <Route path="/contacts" element={<Contacts/>}/>
                        <Route path="/catalog" element={<Catalog/>}/>
                        <Route path="/login" element={<Login/>}/>
                    </Routes>
                </BrowserRouter>
            </div>
            <Footer/>
        </div>
    );
}

export default App;
