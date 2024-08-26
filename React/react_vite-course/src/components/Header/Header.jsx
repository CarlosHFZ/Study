// import headerElement from '../HeaderWithoutJSX'
import './Header.css'
import PropTypes from 'prop-types'

function Header(props) {
    const hideMenu = props.hideMenu

    // return headerElement
    return (
    <header className="header">
        {hideMenu ? null : (
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="about/">Sobre</a></li>
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