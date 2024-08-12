import { useState } from "react";
function Titulo({ cor }){
    // let nome = 'Dimitri Teixeira';
    // const soma = 10 + 10;
    // const urlImg = "https://img.freepik.com/fotos-gratis/respingo-colorido-abstrato-3d-background-generativo-ai-background_60438-2509.jpg?size=626&ext=jpg&ga=GA1.1.2008272138.1722729600&semt=sph"
    
    const [texto, setTexto] = useState("Título inicial");
    const [inputText, setInputText] = useState("");

    function clicou(){
        setTexto(inputText);

    }
    return (

        <div>
            <h1 style={{color: cor}}>{texto}</h1>
            <input value={inputText} onChange={(e)=>{setInputText(e.target.value)}} type="text"/>
            {/* <button onClick={()=>{setTexto("Mudei via botão")}}>Mudar</button> */}
            <button onClick={clicou}>Mudar</button>
            {/* <h1>Oi eu sou {soma}</h1> */}
            {/* <h1 style={{color:cor}}>Oi eu sou {nome ? nome : "Fulano"}</h1> */}
            {/* <img width={150} src={urlImg}/> */}
            {/* { paragrafo ?
                <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Eaque ipsam molestias cum ea quam, in cupiditate cumque quo fugiat consequatur hic accusamus facere, et doloremque, doloribus eos tempora aspernatur tenetur.</p>
                :
                <p>Nada</p>
            } */}
        </div>
    )
}

export default Titulo