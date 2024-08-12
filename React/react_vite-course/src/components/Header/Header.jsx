import './Header.css'

function Header(props) {
    const hideMenu = props.hideMenu

    return (
    <header className="header">
        {hideMenu ? null : (
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="about/">Sobre</a></li>
            </ul>
        )}
        {props.name}
    </header>
    )
}


export default Header