// import headerElement from '../HeaderWithoutJSX'
import { Link } from 'react-router-dom'
import './Header.css'
import PropTypes from 'prop-types'

function Header(props) {
    const hideMenu = props.hideMenu

    // return headerElement
    return (
    <header className="header">
        {hideMenu ? null : (
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="about/">Sobre</Link></li>
            </ul>
        )}
        {props.name}
        {props.children}
    </header>
    )
}

Header.propTypes = {
    hideMenu: PropTypes.bool,
    children: PropTypes.node,
    name: PropTypes.string
}

export default Header