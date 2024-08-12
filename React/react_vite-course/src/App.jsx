import Header from './components/Header/Header'
import InputWithText from './components/InputWithText/InputWithText'
import LoginForm from './components/LoginForm/LoginForm'
function App() {
  return (
    <>
    <Header hideMenu={true} name="Joao"/>
    {/* <InputWithText/> */}
    <LoginForm />
    </>
  )
}

export default App
