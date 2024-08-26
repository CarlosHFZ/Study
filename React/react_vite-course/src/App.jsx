import { createBrowserRouter, createRoutesFromElements, RouterProvider, Route } from 'react-router-dom'
import HomePage from './pages/Home/Home'
import AboutPage from './pages/About/About'
import RegisterPage from './pages/Register/Register'
import Layout from './components/Layout/Layout'
import NotFound from './components/NotFound/NotFound'


const browserRouter = createBrowserRouter(createRoutesFromElements(
  <Route path='/' element={<Layout />} errorElement={<NotFound />}>
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
