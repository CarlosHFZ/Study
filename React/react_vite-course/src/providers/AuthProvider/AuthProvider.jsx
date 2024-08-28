import { useState } from 'react'
import { PropTypes } from 'prop-types'
import authContext from "../../contexts/authContext"

export default function AuthProvider(props) {
    const [isAuthenticated, setIsAuthenticated] = useState(false)

    return (
        <authContext.Provider value={{isAuthenticated, setIsAuthenticated}}>
            {props.children}
        </authContext.Provider>
    )
}

AuthProvider.propTypes = {
    children: PropTypes.node.isRequired,
}