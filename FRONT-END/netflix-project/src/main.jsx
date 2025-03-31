import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import GetStarted from './pages/GetStarted';

const router = createBrowserRouter([
  {
    path: "/",
    element: <GetStarted />,
  },
]);

const root = createRoot(document.getElementById('root'))
root.render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
