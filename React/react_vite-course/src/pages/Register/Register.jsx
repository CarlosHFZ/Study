import { useState } from "react";
import Input from "../../components/Input/Input";
import './Register.css'

export default function RegisterPage() {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [confirmPassword, setConfirmPassword] = useState('')

    function onEmailChangeHandler(event){
        setEmail(event.target.value)
    }

    function onPasswordChangeHandler(event){
        setPassword(event.target.value)
    }

    function onConfirmPasswordChangeHandler(event){
        setConfirmPassword(event.target.value)
    }

    function onSubmitHandler(event){
        event.preventDefault()
        // alert('teste')
        console.log(email)
        console.log(password)
        console.log(confirmPassword)
    }
    return (
        <div className="register-container" onSubmit={onSubmitHandler}>
            <form className="register-form">
                <Input
                label="Email"
                inputValue={email}
                onChange={onEmailChangeHandler}
                />

                <Input
                label="Senha"
                inputValue={password}
                onChange={onPasswordChangeHandler}
                />

                <Input
                label="Confirmar a senha"
                inputValue={confirmPassword}
                onChange={onConfirmPasswordChangeHandler}
                />

                <button type='submit'>Cadastrar</button>
            </form>
        </div>
    )
}