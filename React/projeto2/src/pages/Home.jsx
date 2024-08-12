import { BrowserRouter, Routes } from "react-router-dom";
import Menu from "./Menu";

function Home() {
    <div>
        <h1>Home</h1>
        <BrowserRouter>
            <Routes>
                <Route path="/" elemente={<Home />}/>
                <Route path="/sobre" elemente={<Sobre />}/>
                <Route path="/contato" elemente={<Contato />}/>
            </Routes>
        </BrowserRouter>
    </div>
}

export default Home