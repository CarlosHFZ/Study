// import Titulo from "./Titulo";
import { BrowserRouter, Routes, Route } from "react-router-dom"
import Home from "./pages/Home"
import Sobre from "./pages/Sobre"
import Contato from "./pages/Contato"


function App(){
  return (
    <div>
      {/* <Titulo cor="red" nome="Dimitri" paragrafo={true}/>
      <Titulo cor="blue" nome="Carlos"/>
      <Titulo cor="purple"/>
      <Titulo cor="grey"/> */}
      <Home />
    </div>
  )
}

export default App