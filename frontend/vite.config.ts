import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],

  // Important: Set base to './' for Streamlit components
  base: './',

  build: {
    // Output directory - keep as 'build' to match CRA structure
    outDir: 'build',

    // Asset directory structure to match CRA output
    assetsDir: 'static',

    // Generate sourcemaps for debugging
    sourcemap: true,

    // Minify for production
    minify: 'terser',

    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html')
      },
      output: {
        // Match CRA's file naming convention
        entryFileNames: 'static/js/[name].[hash].js',
        chunkFileNames: 'static/js/[name].[hash].js',
        assetFileNames: (assetInfo) => {
          // CSS files
          if (assetInfo.name?.endsWith('.css')) {
            return 'static/css/[name].[hash][extname]'
          }
          // Other assets
          return 'static/[ext]/[name].[hash][extname]'
        }
      }
    }
  },

  server: {
    // Development server configuration
    port: 3000,
    host: 'localhost',

    // Enable CORS for Streamlit development
    cors: true,

    // HMR configuration
    hmr: {
      protocol: 'ws',
      host: 'localhost'
    }
  }
})
