import { useState, useContext } from 'react';
import authContext from '../../contexts/authContext'
import Timer from '../../components/Timer/Timer';
import styles from './Home.module.css'
// import Header from '../../components/Header/Header'

function HomePage() {
    const [showTimer, setShowTimer] = useState(false)
    const context = useContext(authContext)
    return (
        <>
        <h1 className={styles.h1}>
            {context.isAuthenticated ? 'Olá, você está autenticado' : 'Olá seja bem vindo'}
        </h1>
        {showTimer ? <Timer /> : null}
        <button
            onClick={function() {setShowTimer(!showTimer)}}>
            mostra/esconde
        </button>
        </>
    )
}

export default HomePage;