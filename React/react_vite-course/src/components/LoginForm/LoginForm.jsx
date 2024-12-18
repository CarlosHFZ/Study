import { useContext, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import './LoginForm.css'
import authContext from '../../contexts/authContext'

function LoginForm() {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const context = useContext(authContext)
    const navigate = useNavigate()
    const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    function onEmailChangeHandler(event){
        setEmail(event.target.value)
    }

    function onPasswordChangeHandler(event){
        setPassword(event.target.value)
    }

    function isInputValid(){
        if (!email || !password) return false
        if (!regex.test(email)) return false
        return true
    }

    function OnSubmitHandler(event) {
        event.preventDefault()
        if (isInputValid()){
            console.log('Seu email é:', email)
            console.log('Sua senha é:', password)
            context.setIsAuthenticated(true)
            navigate('/')
        } else {
            console.log('Campos inválidos')
        }
    }


    return (
        <form className='container' onSubmit={OnSubmitHandler}>
            <div className='input-container'>
                <label htmlFor='email'>Email</label>
                <input type='text'id='email' placeholder='Email' onChange={onEmailChangeHandler} />
            </div>
            <div className='input-container'>
                <label htmlFor='password'>Senha</label>
                <input type='password' id='password' placeholder='Senha' onChange={onPasswordChangeHandler}/>
            </div>
            <button typeof='submit'>Login</button>
            {context.isAuthenticated ? 'autenticado' : 'não autenticado'}
        </form>

    )
}

export default LoginForm