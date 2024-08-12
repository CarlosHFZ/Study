import { useState } from 'react'
import './InputWithText.css'

// Uma variavel que se mudada de uma maneira especial, o componente se atualiza.
// top-level declaration
function InputWithText() {
    const [inputValue, setInputValue] =  useState('')

    function OnChangeHandler(event){
        setInputValue(event.target.value)
        console.log(inputValue)
    }
    return (
        <div className='container'>
            <input type="text" placeholder='Digite aqui...' onChange={OnChangeHandler}/>
            <h1>{inputValue}</h1>
        </div>
    )
}

export default InputWithText