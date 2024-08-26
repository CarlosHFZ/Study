import { useState } from 'react';
import Header from '../../components/Header/Header'
import Timer from '../../components/Timer/Timer';
import './Home.css'

function HomePage() {
    const [showTimer, setShowTimer] = useState(true)

    return (
        <>
        <Header />
        <h1>Olá seja bem vindo</h1>
        {showTimer ? <Timer /> : null}
        <button
            onClick={function() {setShowTimer(!showTimer)}}>
            mostra/esconde
        </button>
        </>
    )
}

export default HomePage;