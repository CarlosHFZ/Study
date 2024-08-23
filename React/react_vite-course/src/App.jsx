import { createBrowserRouter, createRoutesFromElements, RouterProvider, Route } from 'react-router-dom'
import HomePage from './pages/Home/Home'
import AboutPage from './pages/About/About'
import RegisterPage from './pages/Register/Register'


const browserRouter = createBrowserRouter(createRoutesFromElements(
  <Route path='/'>~
    <Route index={true} element={<HomePage />} />
    <Route path='about' element={<AboutPage />} />
    <Route path='register' element={<RegisterPage/>} />
  </Route>
))

function App() {
  return (
    <RouterProvider router={browserRouter} />
  )
}
// Prop Drilling
export default App
