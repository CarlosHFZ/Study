// import Header from "../../components/Header/Header";
import { useContext } from 'react';
import authContext from '../../contexts/authContext';
import styles from './About.module.css'

function AboutPage() {
    const context = useContext(authContext)

    return (
    <>
        <h1 className={styles.h1}>
            {context.isAuthenticated ? 'Olá, voce está autenticado na sobre' : 'Sobre'}
        </h1>
    </>
    )
}

export default AboutPage;
