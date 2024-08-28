import { createBrowserRouter, createRoutesFromElements, RouterProvider, Route } from 'react-router-dom'
import HomePage from './pages/Home/Home'
import AboutPage from './pages/About/About'
import RegisterPage from './pages/Register/Register'
import Layout from './components/Layout/Layout'
import NotFound from './components/NotFound/NotFound'
import LoginPage from './pages/Login/Login'
import AuthProvider from './providers/AuthProvider/AuthProvider'


const browserRouter = createBrowserRouter(createRoutesFromElements(
  <Route>
    <Route path='/' element={<Layout />} errorElement={<NotFound />}>
      <Route index element={<HomePage />} />
      <Route path='about' element={<AboutPage />} />
      <Route path='register' element={<RegisterPage/>} />
    </Route>
    <Route path='/login' element={<LoginPage />} />
  </Route>
))

function App() {
  return (
    <AuthProvider>
        <RouterProvider router={browserRouter} />
    </AuthProvider>
  )
}
// Prop Drilling
export default App
