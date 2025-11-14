<<<<<<< HEAD
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
})
=======
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  server: {
    proxy: {
      'api': 'http://localhost:5555'
    }
  },
  plugins: [react()],
})
>>>>>>> e043172 (Added pages: Home, Patients, Appointments)
