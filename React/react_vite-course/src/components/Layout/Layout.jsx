import './layout.css'
import { Outlet } from "react-router-dom";
import Header from "../Header/Header";

export default function Layout() {
    return (
        <>
        <Header />
        <main className='main-content'>
            <Outlet />
        </main>
        <footer>footer</footer>
        </>
    )
}